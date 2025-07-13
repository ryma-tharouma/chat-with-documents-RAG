"""This module provides functions for a RAG (Retrieval-Augmented Generation) workflow."""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Initialize the LLM globally
LLM = OllamaLLM(model="mistral")

def split_text(docs, chunk_size=600, chunk_overlap=200):
    """Split text into chunks using RecursiveCharacterTextSplitter."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(docs)

def create_vectore_store(docs):
    """Create an in-memory vector store using Ollama embeddings."""
    embeddings = OllamaEmbeddings(model="mistral")
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(docs)
    return vector_store

def get_retriever(vector_store):
    """Get a retriever from the vector store."""
    return vector_store.as_retriever(search_type='similarity', search_kwargs={"k": 1})

def create_prompt():
    """Create a chat prompt template."""
    return ChatPromptTemplate.from_messages([
        ("system",
         "You are a strict question-answering assistant. Use only the provided context to answer. "
         "If the answer is not in the context, respond: 'It is not mentioned.'"),
        ("user", "Context:\n{context}\n\nQuestion: {question}")
    ])

def run_query(retriever, prompt, question):
    """Run a query using the retriever and prompt."""
    docs = retriever.invoke(question)
    context = "\n\n".join(doc.page_content for doc in docs)
    formatted_prompt = prompt.format_messages(question=question, context=context)
    return LLM.invoke(formatted_prompt)

def init_rag(docs):
    """Initialize the RAG pipeline from raw documents."""
    split_docs = split_text(docs)
    vector_store = create_vectore_store(split_docs)
    retriever = get_retriever(vector_store)
    prompt = create_prompt()
    return retriever, prompt

def get_answer(question, retriever, prompt):
    """Answer a question using the retriever and prompt."""
    return run_query(retriever, prompt, question)
