# 🎓 Career Guidance using Ollama (Local GenAI)

This project provides an AI-powered **career guidance system** that runs fully on **local Large Language Models (LLMs)** using **Ollama**. It analyzes user resumes, skills, interests, and career goals to recommend suitable job roles, learning paths, and interview prep guidance—all with **privacy and offline capability**.

---

## 🚀 Features

- 🧠 Local LLM inference using **Ollama** (No API keys required)
- 📄 Resume Parsing (Skills, Experience, Education extraction)
- 🎯 Job Role Recommendation using embeddings
- 🤝 Interview Preparation (Questions, sample answers)
- 🔊 Audio-based sentiment & communication analysis
- 🔗 Fusion model combining skills, goals & job market context
- 📚 Text analysis for user career answers
- 🗄️ Simple local job database lookup

---

## 🗂️ Project Structure

career guidance using ollama/
│
├── .venv/ # Virtual environment
├── newenv/ # Optional env folder
├── data/ # Datasets, job data, sample resumes
├── app.py # Main application entry
├── audio_analysis.py # Voice / audio evaluation
├── fusion_model.py # Combines model outputs for career scoring
├── interview_prep.py # Interview questions & evaluation
├── job_db.py # Local job database and queries
├── recommender.py # Job recommendation engine
├── requirements.txt # Python dependencies
├── resume_parser.py # Resume text parsing
├── text_analysis.py # Skill & interest extraction
├── utils.py # Helper functions
└── .env # Environment variables (Do NOT commit)

yaml
Copy code

---

## 🛠️ Installation & Setup

### 1️⃣ Install Ollama
Download and install from:  
https://ollama.com/download

Verify installation:
```bash
ollama run llama2
2️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/career-guidance-ollama.git
cd career-guidance-ollama
3️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
4️⃣ Install Requirements
bash
Copy code
pip install -r requirements.txt
5️⃣ Run the Application
bash
Copy code
python app.py
📌 Requirements
Key dependencies (full list in requirements.txt):

Python 3.10+

Ollama

sentence-transformers

pydub / librosa (optional for audio analysis)

numpy, pandas, scikit-learn

FastAPI / Flask (if building API)

🔮 Future Enhancements
Web UI Dashboard (Streamlit or FastAPI-React)

PDF resume upload & automatic parsing

Real job market integration (optional online mode)

Learning path recommendation (Courses, Roadmaps)

🤝 Contributing
Pull requests are welcome! For major changes, open an issue to discuss what you would like to improve.

