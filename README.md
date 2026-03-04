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

📊 Sample Output

Candidate Review Example
text
**Candidate Evaluation Report**

**Overall Assessment:** The candidate demonstrates strong alignment with the Senior Python Full Stack Developer role, with particular strength in backend development and AI/LLM integration.

**Strengths:**
- ✅ Extensive Python expertise with 5+ years of experience
- ✅ Strong proficiency in FastAPI, LangChain, and LangFlow
- ✅ Demonstrated experience with RAG implementations and LLM applications
- ✅ Solid understanding of microservice architecture
- ✅ Good grasp of REST APIs and database management

**Weaknesses/Areas for Improvement:**
- ⚠️ Limited experience with SOAP APIs (mentioned but not demonstrated in projects)
- ⚠️ No mention of regression testing or evaluation frameworks
- ⚠️ Cursor/JetBrains AI tools not listed in technical stack
- ⚠️ 5 years experience vs. required 8+ years

**Verdict:** Strong technical candidate for mid-level position, but may need additional senior-level experience for this specific role. Recommended for interview with focus on architecture decisions and scaling experience.
Missing Keywords Example
text
**Critical Keywords Missing from Resume for ATS Optimization**

| Keyword | Relevance | Found in Resume? |
|---------|-----------|------------------|
| SOAP | Required for enterprise API integration | ❌ Missing |
| Regression Testing | Essential for ML model validation | ❌ Missing |
| Cursor | AI-assisted development tool mentioned in JD | ❌ Missing |
| JetBrains AI | Specific tool preference in job requirements | ❌ Missing |
| Microservices | Required architecture pattern | ✅ Present |
| LangChain | Core framework for LLM applications | ✅ Present |

**Impact on ATS Score:** Current match rate is 78%. Adding missing keywords could improve ranking to 94%.
Similarity Analysis Example
text
**Resume-Job Description Similarity Analysis**

┌─────────────────────────────────────┐
│     MATCH SCORE: 83%                │
│     ████████████████████░░░░░░      │
└─────────────────────────────────────┘

**Matching Areas (High Alignment):**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Python Programming (Core requirement)
✓ FastAPI Framework (Explicitly mentioned)
✓ LangChain/LangFlow (Key differentiator)
✓ REST API Development (Essential skill)
✓ Microservice Architecture (Required)
✓ Database Management (PostgreSQL/MySQL)

**Partial Matches:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
○ LLM Applications (Some experience, needs depth)
○ RAG Implementations (Basic understanding)
○ Docker/Containerization (Mentioned but limited)

**Significant Gaps:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✗ SOAP APIs (Not demonstrated)
✗ Regression Testing (Missing entirely)
✗ AI-assisted Tools (Cursor/JetBrains AI)

**Recommendation:** Strong technical foundation with 83% skill match. Experience gap (5 years vs. 8 years required) is the primary differentiator. Consider for roles with 5-7 year requirements.
Generated Interview Questions Example
text
**Tailored Interview Questions for Senior Python Full Stack Developer**

**Technical Questions:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. **LLM Integration:** "You've worked with LangChain and RAG implementations. Can you walk me through a specific project where you integrated an LLM into a production application? What challenges did you face with prompt engineering and tool calling?"

2. **Microservice Architecture:** "The role requires deep understanding of microservice architecture. Describe a system you built using microservices. How did you handle service discovery, inter-service communication, and data consistency?"

3. **API Development:** "You have experience with both REST and some exposure to SOAP. In a distributed system, when would you choose SOAP over REST, and what are the trade-offs?"

4. **Performance Optimization:** "FastAPI is one of your key skills. How would you optimize a FastAPI application handling 10,000+ concurrent requests? Walk me through your approach to caching, database connection pooling, and async patterns."

5. **Database Design:** "You've worked with PostgreSQL and MySQL. Design a schema for a job matching platform that needs to handle millions of resumes and perform semantic search. What indexing strategies would you use?"

**Behavioral Questions:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6. **Team Collaboration:** "Tell me about a time you had to collaborate with data scientists to deploy an ML model to production. How did you handle the handoff and ensure the model performed well in the production environment?"

7. **Conflict Resolution:** "Describe a situation where you disagreed with a team member about a technical architecture decision. How did you resolve it, and what was the outcome?"

8. **Mentorship:** "As a senior developer, you'll be expected to mentor junior team members. Tell me about your experience mentoring others and your approach to code reviews."

9. **Project Management:** "Walk me through a complex project from requirements gathering to deployment. How did you break down the work, estimate timelines, and handle unexpected challenges?"

10. **Continuous Learning:** "The tech stack mentions several AI-assisted development tools. How do you stay current with emerging technologies, and how have you incorporated new tools into your workflow recently?"

**Role-Specific Scenarios:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

11. **System Design:** "Design a real-time resume scoring system that matches candidates to jobs using LLMs. Consider scalability, cost optimization, and response time requirements."

12. **Debugging Challenge:** "A production service suddenly starts returning 50x errors after a new model deployment. How would you diagnose and fix the issue? What monitoring and logging would you put in place to prevent this?"

13. **Technical Decision:** "You need to choose between LangChain and building custom LLM orchestration. What factors would influence your decision, and which would you choose for a high-throughput application?"

**Assessment Criteria:**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Depth of technical knowledge (1-10): Target 7+
- Problem-solving approach (1-10): Target 8+
- Communication clarity (1-10): Target 7+
- Cultural fit indicators: Collaboration, learning agility
- Seniority level: Expected 5+ years experience demonstration
  

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
