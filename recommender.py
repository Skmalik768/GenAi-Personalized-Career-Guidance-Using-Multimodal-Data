import os
from job_db import build_job_db
from tavily import TavilyClient
from utils import query_llm  # Ollama
from dotenv import load_dotenv

# Load .env
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Initialize Tavily if API key is present
tavily = TavilyClient(api_key=TAVILY_API_KEY) if TAVILY_API_KEY else None

# Convert GrowthTrend to numeric weights
def trend_score(trend):
    if trend == "High":
        return 1.0
    elif trend == "Medium":
        return 0.6
    elif trend == "Low":
        return 0.3
    return 0.5

# Tavily fallback for live jobs
def fetch_new_jobs(query):
    if not tavily:
        return []  # skip if no API key
    results = tavily.search(query, max_results=3)
    return [r["title"] for r in results["results"]]

# Recommend jobs
def recommend_careers(user_profile, confidence=0.7):
    collection, model = build_job_db()

    # Encode user profile
    user_embedding = model.encode(user_profile).tolist()

    # Query ChromaDB
    results = collection.query(
        query_embeddings=[user_embedding],
        n_results=10
    )

    scored_jobs = []
    seen = set()  # avoid duplicates
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        job_role = meta['JobRole']
        if job_role in seen:
            continue
        seen.add(job_role)

        base_score = trend_score(meta['GrowthTrend'])
        final_score = base_score * confidence
        scored_jobs.append(
            (job_role, meta['RequiredSkills'], meta['AvgSalary'], meta['GrowthTrend'], final_score)
        )

    # Sort and pick top 3
    scored_jobs.sort(key=lambda x: x[4], reverse=True)
    top_jobs = scored_jobs[:3]

    # Fallback to Tavily if not enough jobs
    if len(top_jobs) < 3:
        live_jobs = fetch_new_jobs(user_profile)
        for job in live_jobs:
            if len(top_jobs) >= 3:
                break
            top_jobs.append((job, "N/A", "N/A", "N/A", 0.5))

    # -------------------
    # Optional: Ollama refinement
    # -------------------
    try:
        prompt = f"Refine the following career recommendations for the user profile: {user_profile}\n\n" \
                 f"Jobs: {', '.join([job[0] for job in top_jobs])}\n" \
                 f"Provide only updated list of top 3 jobs with title and skills."
        llm_response = query_llm(prompt, max_new_tokens=200)
        # Optional: parse llm_response if you want structured output
    except Exception:
        pass  # keep top_jobs intact if LLM fails

    return top_jobs
