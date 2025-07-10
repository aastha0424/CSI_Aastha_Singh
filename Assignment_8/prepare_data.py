# prepare_data.py

import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# Set file paths
CSV_PATH = "data/training_data.csv"         # Your input CSV
EMBEDDINGS_PATH = "embeddings/vector_index.pkl"  # Where to save embeddings

# Load dataset
df = pd.read_csv(CSV_PATH)

# Fill NaNs for text generation
df.fillna("Unknown", inplace=True)

# Convert each row into a natural language sentence
def row_to_text(row):
    return (
        f"Applicant {row['Loan_ID']} is a {row['Gender']} applicant, "
        f"{'married' if row['Married'] == 'Yes' else 'not married'}, "
        f"with {row['Dependents']} dependents. They are a {row['Education']} "
        f"and {'self-employed' if row['Self_Employed'] == 'Yes' else 'not self-employed'}. "
        f"Their income is {row['ApplicantIncome']} and their co-applicant's income is {row['CoapplicantIncome']}. "
        f"The loan amount requested is {row['LoanAmount']} for a term of {row['Loan_Amount_Term']} months. "
        f"Credit history is {row['Credit_History']} and property area is {row['Property_Area']}. "
        f"Loan was {'approved' if row['Loan_Status'] == 'Y' else 'not approved'}."
    )

# Generate list of textual chunks
print("Converting rows into text...")
texts = [row_to_text(row) for _, row in tqdm(df.iterrows(), total=len(df))]

# Load lightweight embedding model
print("Generating embeddings...")
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(texts, show_progress_bar=True)

# Save texts and embeddings
print("Saving embeddings...")
with open(EMBEDDINGS_PATH, "wb") as f:
    pickle.dump({
        "texts": texts,
        "embeddings": embeddings
    }, f)

print(f"Saved {len(texts)} embedded documents to {EMBEDDINGS_PATH}")
