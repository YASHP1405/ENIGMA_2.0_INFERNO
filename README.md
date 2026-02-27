# Inferno-Edtech-E2-PS3


Problem Statement :- 
=======
Team Members :- 
1. Yash Pawar
2. Yash Selokar
3. Jai Jadhav
4. Prajwal Satarkar
5. Charudata Lende

Problem Statement :-
3. Intelligent Interview Simulation System 
The Problem: 
There is a significant gap between coding practice platforms and real-world interview 
experiences. While students can solve problems and validate their code against test cases, they 
do not receive structured feedback on their thinking process, communication clarity, or logical 
reasoning. Additionally, current AI-based interview tools do not fully integrate coding 
evaluation, voice-based explanation analysis, and resume-personalized questioning into a 
single interactive platform. 

_________________________________________________
The Challenge: 
Build an AI-powered intelligent interview simulation system that evaluates not just code 
correctness but also a candidate’s problem-solving approach, communication skills, reasoning 
ability, and overall interview readiness. The system should simulate real interview conditions 
by analyzing voice explanations, coding performance, resume context, and HR responses in a 
unified workflow.
____________________________________________________________
Deliverables: 
• Voice AI Agent–based DSA interview simulation with real-time conversational interaction      
and reasoning evaluation 
• AI analysis of candidate’s logical approach and reasoning 
• Automated follow-up question generation 
• Suggestions for optimized or alternative solutions 
• Resume upload and AI-based skill extraction 
• Resume-personalized technical interview questions 
• Structured feedback report including technical and communication scores 
• Interview session history and performance analytics dashboard 
• Browser locking mechanism during interviews to prevent tab switching and cheating 


# 🔥 ENIGMA 2.0 – Inferno EdTech AI Interview Platform

An AI-powered interview and assessment platform designed to evaluate candidates through coding tests, cognitive tests, resume-based interviews, and deep performance reports.

---

## 🚀 Features

- 🧠 AI Mock Interview (Groq LLM powered)
- 💻 Coding Test Evaluation
- 📊 Cognitive Assessment
- 📄 Resume-based Interview
- 📈 Deep Performance Report
- 📱 PWA Support (Manifest + Service Worker)
- 🔥 Firebase Integration

---

## 🏗️ Project Structure

Inferno-Edtech-E2-PS3/
│
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ ├── interview.html
│ ├── resume_interview.html
│ ├── coding_test.html
│ ├── cognitive_test.html
│ ├── report.html
│ └── deep_report.html
│
├── firebase-config.js
├── manifest.json
├── sw.js
├── package-lock.json
└── README.md


---

## ⚙️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Flask (Python)
- AI Model: Groq (LLaMA3)
- Database/Auth: Firebase
- Deployment: GitHub

---

## 🔐 Security Notice

⚠️ API keys must NEVER be stored in frontend files.

Use environment variables in backend:

And access in Flask using:

```python
--import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


git clone https://github.com/YASHP1405/ENIGMA_2.0_INFERNO.git

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
