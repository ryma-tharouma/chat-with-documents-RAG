# 📄 Chat with Your Documents – RAG App

**Retrieval-Augmented Generation (RAG)** powered app to chat with your own PDF, Word, or PowerPoint files using `Ollama`, `LangChain`, and `Streamlit`.

Ask questions about your uploaded documents, the system retrieves relevant chunks and responds using a locally running LLM (e.g., Mistral via Ollama).

---

## 🚀 Features

- 📁 Upload `.pdf`, `.docx`, and `.pptx` files
- ✂️ Smart chunking with `RecursiveCharacterTextSplitter`
- 🧠 Embedding via `OllamaEmbeddings` (Mistral)
- 🗂️ Fast in-memory vector store (no disk I/O delay)
- 🔍 Similarity search-based retrieval
- 🤖 LLM response constrained to document content
- ⚡ Streamlit UI with live Q&A

---

## 🧱 Tech Stack

- **[Streamlit](https://streamlit.io/)** – Frontend interface
- **[LangChain](https://www.langchain.com/)** – RAG pipeline components
- **[Ollama](https://ollama.com/)** – Local language model inference
- **Mistral** – LLM used for generation
- **Python 3.10+**

---

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed on your system

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Install and Setup Ollama

1. **Download and install Ollama** from [https://ollama.com/](https://ollama.com/)

2. **Pull the Mistral model**:

   ```bash
   ollama pull mistral
   ```

3. **Start Ollama service** (keep this running in a separate terminal):
   ```bash
   ollama serve
   ```

### Step 3: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎯 Usage

1. **Upload Documents**: Drop your PDF, Word, or PowerPoint files
2. **Wait for Processing**: The app will chunk and embed your documents
3. **Ask Questions**: Type questions about your uploaded content
4. **Get Answers**: The AI will respond based only on your document content

---

## 📝 Requirements

The project uses these key packages:

- `streamlit>=1.28.0` - Web interface
- `langchain-community>=0.0.1` - Document loaders
- `langchain-text-splitters>=0.0.1` - Text chunking
- `langchain-ollama>=0.1.0` - Ollama integration
- `langchain-core>=0.1.0` - Core LangChain components
