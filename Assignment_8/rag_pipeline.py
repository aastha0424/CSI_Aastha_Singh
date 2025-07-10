# rag_pipeline.py
from dotenv import load_dotenv
load_dotenv()
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
import os

# =======================
# CONFIGURATION
# =======================

GROQ_MODEL = "llama3-8b-8192"  # Other options: llama3-8b-8192, gemma-7b-it

# =======================
# LOAD EMBEDDINGS
# =======================
with open("embeddings/vector_index.pkl", "rb") as f:
    data = pickle.load(f)

texts = data["texts"]
embeddings = np.array(data["embeddings"])

# =======================
# INIT EMBEDDING MODEL
# =======================
model = SentenceTransformer('all-MiniLM-L6-v2')

# =======================
# INIT GROQ CLIENT
# =======================
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# client = Groq(api_key=GROQ_API_KEY)


# =======================
# RETRIEVER
# =======================
def retrieve_top_k_chunks(query, k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = similarities.argsort()[-k:][::-1]
    return [texts[i] for i in top_indices]


# =======================
# GENERATOR (GROQ)
# =======================
def generate_response(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""You are an intelligent assistant with access to loan application data.

Context:
{context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": "You are an expert on loan approvals."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=512,
        top_p=1
    )

    return response.choices[0].message.content.strip()


# =======================
# MAIN FUNCTION
# =======================
def answer_question(question):
    top_chunks = retrieve_top_k_chunks(question, k=5)
    return generate_response(question, top_chunks)


# =======================
# CLI DEMO
# =======================
if __name__ == "__main__":
    print("Loan RAG Chatbot (Groq)\n")
    while True:
        user_question = input("Ask a question (or type 'exit'): ")
        if user_question.lower() == 'exit':
            break
        answer = answer_question(user_question)
        print("\nAnswer:\n", answer, "\n")
