# 🧠 GenAI Personalized Career Guidance Using Multimodal Data

The **GenAI Personalized Career Guidance Using Multimodal Data** project presents an advanced, AI-driven framework designed to redefine how students and professionals explore and select their career paths. Developed at the **Apex Institute of Technology, Chandigarh University**, this system addresses the shortcomings of traditional career counseling approaches, which often rely on static aptitude tests, generalized assessments, and outdated labor market assumptions. Such methods typically overlook vital personal dimensions such as communication confidence, behavioral inclinations, and the rapid evolution of industry skills, leading to misaligned or suboptimal career recommendations.

To overcome these limitations, this system leverages the capabilities of **Generative Artificial Intelligence (GenAI)** and a **multimodal learning architecture**, incorporating three distinct and complementary input sources:

1. **Resume and Skill Extraction (Text Processing):**  
   Through a hybrid pipeline that combines Natural Language Processing (NLP), semantic embeddings, and Optical Character Recognition (OCR), the system analyzes user resumes to extract technical skills, soft competencies, and academic or professional experience. This enables standardized profile construction regardless of resume formatting or wording differences.

2. **Behavioral and Interest Analysis (NLP Embedding Models):**  
   Users provide short written responses about their interests, motivations, and preferred work styles. These are transformed into vector representations using sentence-transformer embeddings, enabling the system to infer suitable career domains based on personality traits, learning preferences, and cognitive alignment with specific fields.

3. **Audio-Based Communication Confidence Assessment:**  
   Recognizing the importance of communication and confidence in many professional roles, the system evaluates short user-recorded audio responses. Whisper-based speech-to-text conversion and acoustic analysis techniques measure pitch stability, hesitation patterns, and speech rate, yielding a confidence score that influences recommendations particularly for client-facing or leadership careers.

These multimodal signals are integrated through a **Multimodal Fusion Layer**, producing a comprehensive and contextualized profile. The **Hybrid Career Recommendation Engine** then performs semantic vector matching using **ChromaDB** and augments insights with real-time labor market intelligence from **Tavily Search**. The final output includes:

- Top recommended career roles with match scores  
- Salary and market demand indicators  
- Required technical and soft skills  
- Personalized skill-gap analysis and learning roadmap  
- AI-generated interview preparation guidance

By combining multimodal analytics, labor-market relevance, and LLM-powered reasoning, this project delivers a next-generation, highly personalized career guidance experience—moving beyond one-size-fits-all assessments and empowering users to make informed, confident, and future-ready career decisions.

---

## 🎯 Research Motivation & Problem Statement

Career decisions significantly impact an individual’s professional journey, yet most guidance systems rely on **static, generalized assessments**. As a result:

❌ Skills and interests are often mismatched  
❌ Communication traits are ignored  
❌ Market trends are not incorporated  
❌ Suggestions lack explainability

To address these limitations, this work introduces a **multimodal, AI-driven framework** that analyzes **skills, behavioral interests, and communication attributes** to generate **context-aware** and **market-relevant** career paths.

---

## 🚀 Core Features

| Capability | Description |
|------------|-------------|
| 📄 Resume Parsing | Extracts technical and soft skills using NLP + OCR hybrid processing |
| ✍ Behavioral Text Understanding | Maps interests to career domains using sentence embeddings |
| 🎤 Audio Confidence Analysis | Whisper-based transcription + pitch, speech-rate, hesitation scoring |
| 🔗 Multimodal Fusion Layer | Weighted semantic fusion of skills + interests + communication |
| 🧩 Career Recommendation Engine | Vector search (ChromaDB) + live job trend enrichment (Tavily Search) |
| 🗣 AI Interview Preparation | LLM-generated interview Q&A and learning roadmap for each role |
| 📚 Skill-Gap Detection | Identifies missing competencies and suggests upskilling path |

---

## 🏗 System Architecture
<img width="322" height="497" alt="image" src="https://github.com/user-attachments/assets/1a59e9e7-c04b-400e-a9c9-fc02b41273ca" />

## 📊 Key Results (Experimental Findings)

- **Recommendation Accuracy:** 89.6%
- **Cosine Similarity (Profile vs Career Vectors):** 0.82 – 0.93
- **Improved matching through audio-confidence weighting**

Example Output:

| Rank | Career Path        | Match Score |
|------|-------------------|-------------|
| 1    | Data Scientist     | 0.91        |
| 2    | Business Analyst   | 0.68        |
| 3    | ML Engineer        | 0.64        |

---

## 📁 Repository Structure


```plaintext
📁 Repository Structure
├── app.py                # Streamlit application interface
├── resume_parser.py      # Hybrid text/OCR resume processing
├── text_analysis.py      # Behavioral semantic analysis
├── audio_analysis.py     # Whisper + acoustic confidence scoring
├── fusion_model.py       # Multimodal vector fusion
├── recommender.py        # Hybrid vector + market-aware retrieval
├── interview_prep.py     # LLM interview/learning plan generation
├── job_db.py             # Local structured job role database
├── data/                 # Sample datasets
├── requirements.txt
└── .env                  # Environment variables (ignored)
```

## 🧪 Technology Stack

| Area | Tools / Technologies |
|------|---------------------|
| Core Language | Python 3.10+ |
| Large Language Models | Ollama: Mistral / LLaMA models |
| NLP Embeddings | Sentence Transformers (MiniLM-L6-v2) |
| OCR Pipeline | PyMuPDF (fitz), Tesseract |
| Audio Processing | Whisper, librosa/pydub |
| Vector Database | ChromaDB |
| Job Market Retrieval | Tavily Search API (optional) |
| UI Framework | Streamlit |

---

## ⚙ Installation & Setup

### 1️⃣ Install Ollama
Download: https://ollama.com/download
Run test model: ollama run mistral
### 2️⃣ Clone the Repository
https://github.com/Skmalik768/GenAi-Personalized-Career-Guidance-Using-Multimodal-Data.git
### 3️⃣ Create Virtual Environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
pip install -r requirements.txt
### 4️⃣ Launch Application
streamlit run app.py
### 🔮 Future Improvements
Psychometric and visual multimodal integration

Explainable AI (XAI) transparency layer

Real-time global labor market analytics

Scalable deployment for universities & workforce platforms

Mobile application version with on-device inference

📜 Academic Citation (APA Format)
powershell
Copy code
Hussain Hazari, E., Ali, S. M. Y., & Khera, P. (2025).
GenAI Personalized Career Guidance Using Multimodal Data.
Apex Institute of Technology, Chandigarh University, Mohali, India.
👥 Authors & Contributions
Contributor	Role
Ejaz Hussain Hazari	Research, System Development
Sk Malik Yasar Ali	System Architecture, Backend Engineering
Preeti Khera	Project Supervisor / Research Advisor
