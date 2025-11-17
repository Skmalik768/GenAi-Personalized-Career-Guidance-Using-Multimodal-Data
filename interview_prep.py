# interview_prep.py
from utils import query_llm

def generate_interview_prep(job_role):
    """Generate interview preparation notes for a given job role using LLM."""
    prompt = f"""
    You are an expert interviewer preparing candidates.

    Job Role: {job_role}

    Generate:
    - Concise revision notes for the role
    - Key subtopics they should prepare
    - 4 sample interview questions
    Use markdown formatting.
    """
    return query_llm(prompt, max_new_tokens=500)
