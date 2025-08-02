import streamlit as st
import os
from dotenv import load_dotenv
from jira_extraction import extract_jira_stories
from embedding import get_embedding
from rag import generate_rag_answer
import faiss
import numpy as np

# Load .env variables
load_dotenv()

st.set_page_config(page_title="Jira AI Assistant", layout="centered")
st.title("📊 Jira AI Story Assistant")

# Load config
jira_url = os.getenv("JIRA_URL")
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_API_TOKEN")
project_key = os.getenv("PROJECT_KEY")

# Session state to avoid reloading stories every time
if "stories" not in st.session_state:
    st.session_state.stories = []
if "index" not in st.session_state:
    st.session_state.index = None

# === Load or Refresh Stories ===
def load_stories():
    stories = extract_jira_stories(jira_url, email, api_token, project_key)
    vectors = []

    for story in stories:
        text = f"{story['summary']} {story.get('description') or ''}"
        emb = get_embedding(text)
        vectors.append(emb)

    vectors_np = np.array(vectors, dtype='float32')
    index = faiss.IndexFlatL2(len(vectors_np[0]))
    index.add(vectors_np)

    st.session_state.stories = stories
    st.session_state.index = index
    return stories

# === Sidebar ===
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🔄 Refresh Stories"):
        with st.spinner("Fetching stories from Jira..."):
            stories = load_stories()
            st.success(f"Loaded {len(stories)} stories")

# === Main Query Interface ===
query = st.text_input("🔍 Enter your Jira query")

if query and st.session_state.index:
    with st.spinner("🤖 Generating answer using Gemini..."):
        result = generate_rag_answer(
            st.session_state.index,
            st.session_state.stories,
            query
        )
    st.markdown("### ✅ Gemini RAG Answer")
    st.write(result)

elif query and not st.session_state.index:
    st.warning("⚠️ No stories indexed yet. Click 'Refresh Stories' in the sidebar.")