import google.generativeai as genai
from vector_store import search_similar
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found in .env or environment.")

# Configure Gemini
genai.configure(api_key="AIzaSyCeN-AeJUwhohm2nbwmeCdsfdOhayVjydA")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_rag_answer(index, stories, query, top_k=5):
    # Step 1: Retrieve relevant stories using the index
    try:
        relevant_stories = search_similar(index, stories, query, top_k=top_k)
    except Exception as e:
        print("⚠️ FAISS index failed or not found. Falling back to top stories.")
        relevant_stories = stories[:top_k]

    # Step 2: Construct context from stories
    context = "\n\n".join(
        f"{s['summary']}:\n{s['description'] or 'No description'}" for s in relevant_stories
    )

    # Step 3: Construct prompt
    prompt = (
        f"Given the following Jira stories:\n\n{context}\n\n"
        f"Answer the following query: {query}"
    )

    # Step 4: Generate answer using Gemini
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Gemini generation failed:", e)
        return "Error: Gemini generation failed."

# Test block (optional)"
'''if __name__ == "__main__":
    # Dummy values for test
    index = None  # Replace with actual FAISS index if available
    stories = [
        {"summary": "Add login functionality", "description": "Implement login via OAuth", "status": "To Do"},
        {"summary": "Fix bug in payment module", "description": "Resolve overflow error", "status": "In Progress"},
        {"summary": "Improve dashboard UI", "description": "Add chart and table", "status": "Done"},
    ]
    query = "JIRA1_AI_PRO"

    result = generate_rag_answer(index, stories, query)
    print("\n📘 RAG Answer:\n", result)
'''