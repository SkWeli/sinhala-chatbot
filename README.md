# සිංහල AI චැට්බොට් - Sinhala AI Chatbot

A fully offline, RAG-powered, Constitutional AI chatbot built with Ollama, LangChain, and Streamlit. Designed to accept and respond in **Sinhala (Unicode)** with no internet connection required.

---

## Architecture
```
User Input (Sinhala)
↓
Streamlit UI
↓
Constitutional AI Layer ←── Rules enforced on every prompt
↓
RAG Retriever ←── ChromaDB + nomic-embed-text
↓
Qwen2.5:7b via Ollama ←── Fully local LLM inference
↓
Sinhala Response (streamed)
```

---

## Tech Stack

| Component | Tool |
|---|---|
| LLM Runtime | [Ollama](https://ollama.com) |
| Language Model | Qwen2.5 7B (local) |
| Embedding Model | nomic-embed-text (local) |
| Vector Store | ChromaDB |
| Orchestration | LangChain |
| UI | Streamlit |
| Language | Sinhala (Unicode) |

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Windows 10/11 (64-bit)
- Python 3.11+
- [Ollama](https://ollama.com/download/windows) installed

### 2. Pull Required Models
```powershell
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

### 3. Clone the Repository
```powershell
git clone https://github.com/SkWeli/sinhala-chatbot.git
cd sinhala-chatbot
```

### 4. Create Virtual Environment
```powershell
python -m venv chatbot-env
chatbot-env\Scripts\activate
```

### 5. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 6. (Optional) Load Knowledge Base for RAG
Place PDF or text files inside the `documents/` folder, then run:
```powershell
python ingest.py
```

### 7. Run the Chatbot
```powershell
streamlit run chatbot.py
```
Open your browser at `http://localhost:8501`

---

## Project Structure
```
sinhala-chatbot/
├── documents/ ← PDF knowledge base (add files here)
├── chroma_db/ ← Auto-generated vector store (git-ignored)
├── chatbot-env/ ← Virtual environment (git-ignored)
├── chatbot.py ← Main Streamlit chatbot application
├── ingest.py ← Document ingestion script for RAG
├── requirements.txt ← Python dependencies
├── .gitignore
└── README.md
```

---

## Features

- 🇱🇰 Sinhala Unicode input and output
- Fully offline - no API keys, no internet required
- Constitutional AI - built-in safety rules on every prompt
- RAG — answers grounded in your own documents
- Session-based chat history
- Clear chat button
- Streaming responses with live token display

---

## Testing

The `documents/` folder can contain any Sinhala or English PDF.  
At least 20 Sinhala test prompts with outputs are documented in the project report.

---

## Requirements

See [`requirements.txt`](requirements.txt)

---

## License

MIT License — free to use and modify.

