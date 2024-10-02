import streamlit as st
from dotenv import load_dotenv
import os
from utils import *
import constants

# Load environment variables from .env file
load_dotenv()

# Get the API keys from environment variables
huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')

# Creating Session State Variable
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] = huggingface_api_key
if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['Pinecone_API_Key'] = pinecone_api_key

st.title('🤖 AI Assistance For Website')

#********SIDE BAR Functionality started*******
st.sidebar.title("😎🗝️")
st.session_state['HuggingFace_API_Key'] = st.sidebar.text_input(
    "What's your HuggingFace API key?", 
    type="password", 
    value=st.session_state['HuggingFace_API_Key'] or ""
)
st.session_state['Pinecone_API_Key'] = st.sidebar.text_input(
    "What's your Pinecone API key?", 
    type="password", 
    value=st.session_state['Pinecone_API_Key'] or ""
)

# Set Pinecone API key as environment variable
os.environ["PINECONE_API_KEY"] = st.session_state['Pinecone_API_Key']

load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

# Button click logic
if load_button:
    if st.session_state['HuggingFace_API_Key'] and st.session_state['Pinecone_API_Key']:
        # Fetch, split, and push data to Pinecone
        site_data = get_website_data(constants.WEBSITE_URL)
        st.write("Data pull done...")

        chunks_data = split_data(site_data)
        st.write("Splitting data done...")

        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")

        push_to_pinecone(
            st.session_state['Pinecone_API_Key'], 
            constants.PINECONE_ENVIRONMENT, 
            constants.PINECONE_INDEX, 
            embeddings, 
            chunks_data
        )
        st.write("Pushing data to Pinecone done...")

        st.sidebar.success("Data pushed to Pinecone successfully!")
    else:
        st.sidebar.error("Ooopssss!!! Please provide API keys.....")

#********SIDE BAR Functionality ended*******

prompt = st.text_input('How can I help you my friend ❓', key="prompt")
document_count = st.slider('No.Of links to return 🔗 - (0 LOW || 5 HIGH)', 0, 5, 2, step=1)

submit = st.button("Search")

if submit:
    if st.session_state['HuggingFace_API_Key'] and st.session_state['Pinecone_API_Key']:
        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")

        index = pull_from_pinecone(
            st.session_state['Pinecone_API_Key'], 
            constants.PINECONE_ENVIRONMENT, 
            constants.PINECONE_INDEX, 
            embeddings
        )
        st.write("Pinecone index retrieval done...")

        relevant_docs = get_similar_docs(index, prompt, document_count)
        st.write(relevant_docs)

        st.success("Please find the search results:")
        for doc in relevant_docs:
            st.write(f"👉**Result {relevant_docs.index(doc) + 1}**")
            st.write(f"**Info**: {doc.page_content}")
            st.write(f"**Link**: {doc.metadata['source']}")
    else:
        st.sidebar.error("Ooopssss!!! Please provide API keys.....")
