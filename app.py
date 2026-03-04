import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from docx import Document

load_dotenv()

# Debug: Check if API key loads
api_key = os.getenv("Google_API_KEY")
if not api_key:
    st.error("⚠️ Google_API_KEY not found in .env file! Please add it.")
    st.stop()

# Initialize client
client = genai.Client(api_key=api_key)

# Gemini response with models from your dashboard
def get_gemini_response(input_text):
    models_to_try = [
        "gemini-2.5-flash-lite",        # 10 RPM, 20 RPD available
        "gemini-3-flash",                # 5 RPM, 20 RPD available
        "gemini-2.5-flash",              # 5 RPM, 20 RPD (you have 21/20 used)
        "gemini-3.1-flash-lite",         # 15 RPM, 500 RPD available
        "gemma-3-27b-it",                # 30 RPM, 14.4K RPD available
        "gemini-robotics-er-1.5-preview", # 10 RPM, 20 RPD available
    ]
    
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=input_text
            )
            return response.text
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue
    
    return "Error: Could not get response from any model"

# Function to extract text from PDF
def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()
    return extracted_text

# Function to extract text from .docx files
def extract_docx_text(uploaded_file):
    doc = Document(uploaded_file)
    extracted_text = ""
    for paragraph in doc.paragraphs:
        extracted_text += paragraph.text + "\n"
    return extracted_text

# Function to extract text from .txt files
def extract_txt_text(uploaded_file):
    extracted_text = uploaded_file.read().decode("utf-8")
    return extracted_text

# Streamlit app UI setup
st.set_page_config(page_title="ATS Resume Analyzer")
st.header("✨ RecruitTrack - ATS Analytics Hub 📊🚀")

# User inputs
jd = st.text_area("Paste the Job Description:", help="Provide the job description for evaluation.")
uploaded_file = st.file_uploader("Upload Candidate Resume", type=["pdf", "docx", "txt"], help="Upload the candidate's resume in PDF, Word, or TXT format")

# Determine file type and extract text
def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_pdf_text(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_docx_text(uploaded_file)
    elif uploaded_file.type == "text/plain":
        return extract_txt_text(uploaded_file)
    else:
        st.error("Unsupported file type. Please upload a PDF, Word document, or TXT file.")
        return None


# Prompts templates for different actions
input_prompt1 = """
You are an experienced HR with tech expertise in various job roles, including Data Science, Data Analytics, Full Stack, Web Development, 
Big Data Engineer, DevOps, Data Engineering, and others. Your task is to review the provided resume against the job description.
Please share a professional evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses.
Resume: {resume_text}
Job Description: {job_description}
"""

input_prompt3 = """
You are an expert in ATS optimization. Using the provided resume and job description, identify the missing keywords in the resume 
that are critical for ATS ranking. Provide a list of these keywords and explain their relevance.
Resume: {resume_text}
Job Description: {job_description}
"""

input_prompt4 = """
You are an AI-powered similarity evaluator. Compare the provided resume and job description to analyze their similarity. 
Provide a similarity score (0-100%) and explain how closely the candidate's profile aligns with the job requirements. 
Highlight key matching areas and significant gaps.
Resume: {resume_text}
Job Description: {job_description}
"""

input_prompt_questions = """
You are a recruiter conducting an interview. Based on the provided resume and job description, generate a list of potential interview questions to ask the candidate. 
Include both technical and behavioral questions that assess the candidate's skills, experience, and fit for the role.
Resume: {resume_text}
Job Description: {job_description}
"""

# Buttons and functionality
if st.button("Review Candidate Details"):
    if uploaded_file and jd:
        resume_text = extract_text(uploaded_file)
        if resume_text:
            input_prompt = input_prompt1.format(resume_text=resume_text, job_description=jd)
            with st.spinner("Analyzing..."):
                response = get_gemini_response(input_prompt)
            st.subheader("Candidate Review")
            st.write(response)
    else:
        st.error("Please upload the candidate resume and provide a job description.")

if st.button("Identify Missing Keywords"):
    if uploaded_file and jd:
        resume_text = extract_text(uploaded_file)
        if resume_text:
            input_prompt = input_prompt3.format(resume_text=resume_text, job_description=jd)
            with st.spinner("Analyzing..."):
                response = get_gemini_response(input_prompt)
            st.subheader("Missing Keywords")
            st.write(response)
    else:
        st.error("Please upload the candidate resume and provide a job description.")

if st.button("Similarity Analysis"):
    if uploaded_file and jd:
        resume_text = extract_text(uploaded_file)
        if resume_text:
            input_prompt = input_prompt4.format(resume_text=resume_text, job_description=jd)
            with st.spinner("Analyzing..."):
                response = get_gemini_response(input_prompt)
            st.subheader("Similarity Analysis")
            st.write(response)
    else:
        st.error("Please upload the candidate resume and provide a job description.")

if st.button("Generate Interview Questions for Recruiters"):
    if uploaded_file and jd:
        resume_text = extract_text(uploaded_file)
        if resume_text:
            input_prompt = input_prompt_questions.format(resume_text=resume_text, job_description=jd)
            with st.spinner("Analyzing..."):
                response = get_gemini_response(input_prompt)
            st.subheader("Generated Interview Questions for Recruiters to Ask Candidates")
            st.write(response)
    else:
        st.error("Please upload the candidate resume and provide a job description.")

        
# Custom styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: rgb(76, 36, 189);
        color: white;
        border-radius: 10px;
    }
    .block-container {
        padding-top: 4rem;
    }
    input, select, textarea, .stTextInput, .stSelectbox, .stSlider {
        background-color: #0edde6 !important;
        color:#03116e !important;
    }
    label {
        color: #F60582  !important; 
        margin-top: 10px;  
        display: block; 
        font-size: 20px !important;  
    }
    </style>
""", unsafe_allow_html=True)
