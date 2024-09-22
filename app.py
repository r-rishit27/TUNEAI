import streamlit as st
import fitz  # PyMuPDF
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file uploaded via Streamlit."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def create_chat_openai_instance(api_key: str) -> ChatOpenAI:
    return ChatOpenAI(
        openai_api_key=api_key,
        base_url="https://proxy.tune.app/",
        model="openai/gpt-4o",
    )

def format_prompt(document_text: str, job_description: str) -> ChatPromptTemplate:
    system_message = (
        "You are an expert in crafting professional cold emails for job applications. "
        "Your task is to help the user write an effective cold email to a hiring manager. "
        "The email should include the following elements:\n"
        "1. A brief introduction of the user.\n"
        "2. The specific job role they are interested in, based on the provided job description.\n"
        "3. An overview of their educational background.\n"
        "4. A highlight of relevant skills.\n"
        "5. A showcase of notable projects and previous work experience.\n"
        "6. Mention of extracurricular activities.\n"
        "7. A statement of their areas of interest related to the job.\n"
        "Use the following job description as a reference: " + job_description + "\n\n"
    )
    return ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("user", "{input_text}"),
        ]
    )

def generate_response(api_key: str, document_text: str, job_description: str) -> str:
    llm = create_chat_openai_instance(api_key)
    prompt_template = format_prompt(document_text, job_description)
    output_parser = StrOutputParser()
    chain = prompt_template | llm | output_parser
    try:
        response = chain.invoke({"input_text": ''})  # No user input needed
    except Exception as e:
        print(f"Error: {e}")
        response = ""
    return response

# Streamlit Interface
st.title("Cold Email Generator App")

tuneai_api_key: str = st.sidebar.text_input("TuneAI API Key", type="password")

uploaded_file = st.file_uploader("Upload your resume or background document", type=["pdf", "docx"])

if uploaded_file:
    # Extract text from the uploaded document
    document_text = extract_text_from_pdf(uploaded_file)
    
    # Add a text input for the job description
    job_description: str = st.text_area("Enter the job description")
    
    if job_description:
        if st.button("Generate Cold Email"):
            if not tuneai_api_key.strip():
                st.warning("Please enter your TuneAI API Key!", icon="⚠")
            else:
                # Call the generate_response function here
                response: str = generate_response(tuneai_api_key, document_text, job_description)
                st.info(response)
    else:
        st.warning("Please enter the job description!", icon="⚠")
else:
    st.warning("Please upload a valid document!", icon="⚠")
