<img width="1920" height="1080" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/4c507235-efe6-4f76-8630-19c05620c211" /><img width="1920" height="1080" alt="Screenshot (88)" src="https://github.com/user-attachments/assets/56696734-ea1a-4793-8372-d349e7b2095a" />
<img width="1920" height="1080" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/e11562f6-d805-48b1-8b86-4648f05a7222" />
<img width="1920" height="1080" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/8a4f7027-164b-4d38-866f-265cbbc3beca" />
<img width="1920" height="1080" alt="Screenshot (85)" src="https://github.com/user-attachments/assets/766b99ab-5d30-46e8-ae39-47a2a0d79d8a" />
<img width="1920" height="1080" alt="Screenshot (84)" src="https://github.com/user-attachments/assets/3b2de2f9-13df-4ba3-9ac2-b2577510722d" />

# AGENTIC-AI-HACKATHON
HireGenie AI is a multi-agent recruitment assistant that uses LangGraph, RAG, and Google Gemini to analyze resumes, match candidates with job descriptions, generate interview questions, recommend salaries, and provide human-approved hiring decisions through specialized AI agents.
# 🤖 HireGenie AI
### AI-Powered Multi-Agent Recruitment Assistant

## 📌 Problem Statement

Recruitment teams spend significant time manually screening resumes, comparing candidates with job descriptions, estimating salary ranges, and preparing interview questions. This process is repetitive, time-consuming, and prone to inconsistencies.

**HireGenie AI** automates the recruitment workflow using multiple AI agents that collaborate to analyze resumes, compare them with job descriptions, predict salary, support HR decision-making, and generate interview questions.

---

## 🚀 Features

- 📄 Resume PDF Analysis
- 📋 Job Description Analysis
- 🤖 AI-based Resume–JD Matching
- 📊 Match Score & Skill Gap Analysis
- 💰 Salary Prediction
- 👨‍💼 HR Decision Support
- ❓ AI-Generated Technical & HR Interview Questions
- 🧠 Multi-Agent Workflow using LangGraph
- ⚡ Gemini 2.5 Flash Integration
- 🌐 Streamlit Web Interface

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Frameworks
- LangGraph
- Google Gemini 2.5 Flash

### Libraries
- Pydantic
- PyPDF2
- python-dotenv
- Google GenAI SDK

### Utilities
- JSON Parsing
- File Caching
- PDF Text Extraction

### Version Control
- Git
- GitHub

---

## 🏗 Project Architecture

```
                    Resume PDF
                         │
                         ▼
                 Resume Agent
                         │
                         ▼
                  Resume Analysis
                         │
                         │
Job Description PDF ───► JD Agent
                         │
                         ▼
                  JD Analysis
                         │
                         ▼
                 Matcher Agent
                         │
                         ▼
              Match Report + Score
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   Salary Agent                 Decision Agent
          │                             │
          └──────────────┬──────────────┘
                         ▼
               HR Approval (UI)
                         │
                  If Approved
                         ▼
             Interview Agent
                         │
                         ▼
         Technical + HR Questions
```

---

## 📷 Screenshots

Add screenshots here after running the application.

### Home Page

```
screenshots/home.png
```

### Resume & JD Upload

```
screenshots/upload.png
```

### Match Report

```
screenshots/match_report.png
```

### Salary Prediction

```
screenshots/salary.png
```

### Interview Questions

```
screenshots/interview.png
```

---

## ⚙️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/SRIVARDHANBHUSARAPU/AGENTIC-AI-HACKATHON.git
```

### 2. Move into Project

```bash
cd AGENTIC-AI-HACKATHON
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```text
GEMINI_KEY=YOUR_API_KEY
```

### 5. Run Streamlit UI

```bash
streamlit run ui.py
```

Or run from terminal

```bash
python app.py
```

---

## 📂 Project Structure

```
AGENTIC-AI-HACKATHON
│
├── agents/
│   ├── resume_agent.py
│   ├── jd_agent.py
│   ├── matcher_agent.py
│   ├── salary_agent.py
│   ├── decision_agent.py
│   ├── interview_agent.py
│   └── supervisor.py
│
├── tools/
├── utils/
├── database/
├── cache/
│
├── app.py
├── ui.py
├── graph.py
├── config.py
├── prompts.py
├── schemas.py
└── README.md
```

---

## 👥 Team Members

| Roll Number | Name |
|-------------|---------------------------|
| 25881A05Q7 | **SRIVARDHAN BHUSARAPU** |
| 25881A05K6 | **PEDDIREDDY ABHILASH REDDY** |
| 25881A05P9 | **V. SHASHANK REDDY** |
| 25881A05Q6 | **M. SRISHANTH** |

---

## 🎯 Future Enhancements

- ATS Resume Ranking
- Recruiter Dashboard
- Candidate Database
- Email Notifications
- Multi-language Resume Parsing
- Resume Recommendation Engine
- Job Recommendation System
- Cloud Deployment (AWS/Azure)

---

## 📜 License

This project was developed for the Agentic AI Hackathon to demonstrate how AI-powered multi-agent systems can streamline and enhance the recruitment process.
