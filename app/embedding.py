import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

def get_embedding(text):
    response = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return response['embedding']


# to check code is working or not


if __name__ == "__main__":
    sample_text = "This is a sample Jira story about a login issue."
    embedding = get_embedding(sample_text)
    print("Embedding vector (first 100 values):", embedding[:100])

