"""Streamlit app for RAG (Retrieval-Augmented Generation) with document upload and question answering."""

import os
import hashlib
import shutil
import streamlit as st
from RAG import get_answer, init_rag
from load_files import get_docs

# App setup
st.set_page_config(page_title="📄 Chat with Documents", layout="centered")
st.title("📚 Ask Questions About Your Files")

TEMP_DIR = "temp_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

# Upload
uploaded_files = st.file_uploader("Upload PDF, Word, or PowerPoint", type=["pdf", "pptx", "docx"], accept_multiple_files=True)

file_paths = []
if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(TEMP_DIR, file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        file_paths.append(file_path)

    with st.spinner("📂 Loading and parsing documents..."):
        docs = get_docs(file_paths)
        st.success(f"{len(docs)} document chunks loaded.")

        # Create hash of document content for caching
        def hash_docs(docs):
            content = "".join(doc.page_content for doc in docs)
            return hashlib.md5(content.encode()).hexdigest()

        docs_hash = hash_docs(docs)

        @st.cache_resource
        def cached_init_rag(_docs, key):
            return init_rag(_docs)

        retriever, prompt = cached_init_rag(_docs=docs, key=docs_hash) # Cache the RAG initialization
        st.session_state.retriever = retriever
        st.session_state.prompt = prompt
        st.success("✅ RAG system initialized.")

# Question input
if "retriever" in st.session_state and "prompt" in st.session_state:
    question = st.text_input("❓ Ask a question based on the documents")

    if question:
        with st.spinner("🧠 Thinking..."):
            answer = get_answer(question, st.session_state.retriever, st.session_state.prompt)
            st.subheader("💬 Answer:")
            st.write(answer)

# Optional cleanup button
if st.button("🧹 Clear session & uploaded files"):
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    st.cache_resource.clear()
    st.session_state.clear()
    st.success("Temporary files and memory cleared.")
