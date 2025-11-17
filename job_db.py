import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# Load dataset
def load_jobs_dataset():
    df = pd.read_csv("data/jobs_dataset.csv")
    return df

# Build ChromaDB collection
def build_job_db():
    chroma_client = chromadb.Client()
    model = SentenceTransformer('all-MiniLM-L6-v2')

    jobs_df = load_jobs_dataset()
    collection = chroma_client.get_or_create_collection(name="jobs")


    for idx, row in jobs_df.iterrows():
        text = f"{row['JobRole']} - {row['RequiredSkills']} - {row['Description']}"
        embedding = model.encode(text).tolist()
        collection.add(
            ids=[str(idx)],
            documents=[text],
            embeddings=[embedding],
            metadatas=[{
                "JobRole": row["JobRole"],
                "RequiredSkills": row["RequiredSkills"],
                "AvgSalary": row["AvgSalary"],
                "GrowthTrend": row["GrowthTrend"]
            }]
        )
    return collection, model
