# RecruitTrack---ATS-Anlytics-System

📋 Overview

RecruitTrack is a powerful AI-powered Applicant Tracking System (ATS) analytics tool that helps recruiters and HR professionals evaluate candidates efficiently. Built with Streamlit and Google's Gemini AI, this application provides comprehensive resume analysis against job descriptions.

✨ Key Features

- 📄 Multi-format Resume Support: Upload resumes in PDF, DOCX, or TXT formats
- 🤖 AI-Powered Analysis: Leverages Google's Gemini AI models for intelligent evaluation
- 🔍 Four Analysis Modes:
  - Candidate Review: Professional evaluation of candidate alignment with job role
  - Missing Keywords: Identifies critical ATS keywords missing from resumes
  - Similarity Analysis: Provides similarity score with detailed matching analysis
  - Interview Questions: Generates tailored technical and behavioral interview questions
- 🎨 Modern UI: Clean, professional interface with custom styling
- ⚡ Fast Processing: Local text extraction for quick analysis
- 🔄 Model Fallback: Automatically tries multiple Gemini models for reliability

🛠️ Technology Stack

- Frontend	- Streamlit
- AI Models -	Google Gemini AI (gemini-3.1-flash-lite, gemini-2.5-flash-lite, gemma-3-27b-it)
- Document Processing	- PyPDF2, python-docx
- Environment	- Python-dotenv
- Styling	- Custom CSS
  
🚀 Installation & Setup

Prerequisites
  - Python 3.8+
  - Google AI Studio API key

Step 1: Clone the Repository

Step 2: Create Virtual Environment and activate it
- python -m venv venv
- venv\Scripts\activate

Step 3: Install Dependencies
- pip install -r requirements.txt

Step 4: Set Up Environment Variables
- Create a .env file in the root directory:
- Google_API_KEY=your_actual_api_key_here
- Get your API key from Google AI Studio

Step 5: Run the Application
- streamlit run app.py
- The app will open in your browser at http://localhost:8501

📦 Dependencies

- Create a requirements.txt file:
    streamlit>=1.28.0
    google-genai>=1.0.0
    python-dotenv>=1.0.0
    PyPDF2>=3.0.0
    python-docx>=1.0.0
  
Install all at once via pip install streamlit google-genai python-dotenv PyPDF2 python-docx

🎯 How to Use

- Paste Job Description: Enter the job description in the text area

- Upload Resume: Upload candidate resume (PDF, DOCX, or TXT)

- Choose Analysis Type:

  - Click "Review Candidate Details" for professional evaluation
  - Click "Identify Missing Keywords" for ATS optimization
  - Click "Similarity Analysis" for match score
  - Click "Generate Interview Questions" for tailored questions

- View Results: Analysis appears instantly below each button

🤖 AI Models Used
The application automatically tries multiple models in sequence:

Priority	Model	RPM	RPD	Description

- 🥇 1st	gemini-3.1-flash-lite	15	500	Fast, efficient, high quota
- 🥈 2nd	gemini-2.5-flash-lite	10	20	Reliable, good performance
- 🥉 3rd	gemini-3-flash	5	20	Alternative option
- 4th	gemini-2.5-flash	5	20	When available
- 5th	gemma-3-27b-it	30	14,400	Massive quota, text-only
- 6th	gemini-robotics-er-1.5-preview	10	20	Experimental

💡 Features in Detail

1. Candidate Review
  - Provides comprehensive evaluation including:
  
  - Overall alignment with job role
  
  - Key strengths from resume
  
  - Potential weaknesses or gaps
  
  - Professional recommendations

2. Missing Keywords Analysis
  - Identifies critical keywords missing from resume:
  
  - Technical skills required
  
  - Soft skills mentioned in JD
  
  - Industry-specific terminology
  
  - Certification requirements

3. Similarity Analysis
  - Generates match score with:
  
  - Percentage match (0-100%)
  
  - Key matching areas
  
  - Significant gaps
  
  - Detailed explanation

4. Interview Questions Generator
  - Creates tailored questions:
  
  - Technical questions based on required skills
  
  - Behavioral questions from job requirements
  
  - Experience-based questions
  
  - Role-specific scenarios

🎨 UI Customization
  - The application features custom styling:
  
  - Purple buttons with rounded corners
  
  - Teal input fields with dark blue text
  
  - Pink labels for better visibility
  
  - Clean, professional layout


📝 License
This project is for educational and professional development purposes.

📧 Contact
- Anuji Thrimanna
- Email: thrimanna2000@gmail.com
- LinkedIn: https://www.linkedin.com/in/anuji-thrimanna-6389392a9/

## Deployed Live Demo (Streamlit)

https://recruittrack---ats-anlytics-system-bvpljqtybm8bj2pkn2w8te.streamlit.app/

## Video Demo

https://github.com/user-attachments/assets/b18bb06f-2312-487c-bf6b-0bba18b6b344


⭐ If you find this project useful, please consider giving it a star on GitHub!
