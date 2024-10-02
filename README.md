# AI Assistance for Job Findings

This project is designed to assist users in finding job listings from the website [ExcelCult Jobs](https://jobs.excelcult.com/). The application fetches job data from the website, processes it, and allows users to search through the listings using natural language queries.

## Features

- Fetch job listings from the specified website.
- Store and manage job data using Pinecone.
- Utilize Hugging Face's API for enhanced search capabilities.
- User-friendly interface built with Streamlit.

## Requirements

To run this project, you will need the following:

1. **Hugging Face API Key**: This is required to access the Hugging Face models for processing the job data.
2. **Pinecone API Key**: This key allows you to store and manage your job data efficiently.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Akashkalasagond/AI-ChatBot-on-Job-Findings
   cd AI-ChatBot-on-Job-Findings
2.  **Install the required packages**:
    ```bash
    pip intall -r requirements.txt
3. **Create a .env file**
   ```bash
   HUGGINGFACE_API_KEY=<your_hugging_face_api_key>
   PINECONE_API_KEY=<your_pinecone_api_key>
4. **Run the application**
   ```bash
   streamlit run app.py

