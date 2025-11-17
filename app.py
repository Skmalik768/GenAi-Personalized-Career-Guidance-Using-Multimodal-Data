# app.py
import streamlit as st
from resume_parser import extract_resume_text, extract_skills_from_resume
from text_analysis import analyze_text_answers
from audio_analysis import analyze_audio
from fusion_model import fuse_modalities
from recommender import recommend_careers
from interview_prep import generate_interview_prep
# app.py (top of file, after imports)
career_recs = []

st.set_page_config(page_title="GenAI Career Guidance", layout="wide")
st.title("🎯 GenAI Career Guidance Assistant")

# ---------------- Resume or Manual Skills ----------------
st.subheader("📄 Resume / Skills Input")

uploaded_resume = st.file_uploader("Upload Resume (PDF) (optional)", type=["pdf"])
resume_skills = []
manual_skills = []

if uploaded_resume:
    try:
        resume_text = extract_resume_text(uploaded_resume)
        resume_skills = extract_skills_from_resume(resume_text)
        st.success("Resume parsed successfully.")
        st.write("✅ Extracted Skills:", resume_skills if resume_skills else "No skills detected")
    except Exception as e:
        st.error(f"Failed to parse resume: {e}")

# Manual skills field (always visible for freshers / to add more skills)
manual_input = st.text_input("Or enter your skills manually (comma separated) — if no resume", "")
if manual_input:
    manual_skills = [s.strip() for s in manual_input.split(",") if s.strip()]
    st.write("✅ Manual Skills:", manual_skills)

# ---------------- Text Q&A ----------------
st.subheader("💬 Behavioral Questions")
st.markdown("Answer briefly about your interests / what you enjoy (e.g., 'I like problems, AI, and building products').")
answers = st.text_area("Write your answers here (optional):", height=120)
text_interests = analyze_text_answers(answers) if answers else []
if text_interests:
    st.write("✅ Detected Interests:", text_interests)

# ---------------- Audio Input ----------------
st.subheader("🎤 Audio Q&A (optional)")
st.markdown("Upload a short audio clip (wav/mp3) answering a simple question like 'Introduce yourself and your interests'.")
audio_file = st.file_uploader("Upload audio response (wav/mp3)", type=["wav", "mp3"])

confidence = None
if audio_file:
    try:
        with st.spinner("Analyzing audio..."):
            confidence = analyze_audio(audio_file)
        st.success("Audio analyzed.")
        st.write(f"✅ Confidence Score: {confidence:.2f}")
    except Exception as e:
        st.error(f"Audio analysis failed: {e}")
        confidence = 0.6  # fallback

# ---------------- Generate Guidance ----------------
st.markdown("---")
if st.button("🚀 Generate Career Guidance"):
    # Fuse modalities: function expects (resume_skills, manual_skills, text_interests, confidence)
    profile_text, conf = fuse_modalities(resume_skills, manual_skills, text_interests, confidence)

    st.subheader("📌 Candidate Profile")
    st.write(profile_text)
    st.write(f"Audio-based confidence used: {conf:.2f}")

    st.subheader("📌 Career Recommendations (Top 3)")
    try:
        career_recs = recommend_careers(profile_text, conf)
        if isinstance(career_recs, (list, tuple)):
            for job in career_recs:
                title = job[0] if len(job) > 0 else "Unknown Role"
                skills = job[1] if len(job) > 1 else "N/A"
                salary = job[2] if len(job) > 2 else "N/A"
                trend = job[3] if len(job) > 3 else "N/A"
                score = job[4] if len(job) > 4 else 0.0
                st.markdown(f"""
**{title}**  
- Skills: {skills}  
- Avg Salary: {salary}  
- Market Trend: {trend}  
- Match Score: {score:.2f}
""")
        else:
            st.markdown(career_recs)
    except Exception as e:
        st.error(f"Recommendation failed: {e}")

    # ---------------- Interview Prep (Auto for Top 3)
st.subheader("📝 Interview Preparation (Auto-Generated)")
if career_recs:
    for job in career_recs:
        job_role = job[0]  # job title
        st.markdown(f"### {job_role}")
        notes = generate_interview_prep(job_role)
        st.markdown(notes)
        st.markdown("---")
else:
    st.info("Generate career recommendations first to see interview prep.")
