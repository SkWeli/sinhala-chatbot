import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Define Paths 
DOCUMENTS_DIR = "./documents"
CHROMA_DB_DIR = "./chroma_db"
EMBED_MODEL   = "nomic-embed-text"  # local embedding model via Ollama

# Safety Check 
if not os.path.exists(DOCUMENTS_DIR) or not os.listdir(DOCUMENTS_DIR):
    print("❌ No documents found in /documents folder.")
    print("   Add PDF or text files there first, then re-run this script.")
    exit(1)

# Load Documents 
print("📂 Loading documents from /documents...")

loader = DirectoryLoader(
    DOCUMENTS_DIR,
    glob="**/*.pdf",           # target all PDF files recursively
    loader_cls=PyPDFLoader,    # use PyPDF to read each PDF's text
    show_progress=True         # show loading progress bar
)

documents = loader.load()
print(f"✅ Loaded {len(documents)} page(s) from your documents.")

# Split Into Chunks
print("\n✂️  Splitting documents into chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # max characters per chunk
    chunk_overlap=50,     # overlap between consecutive chunks
    length_function=len,  # measure size by character count
)

chunks = splitter.split_documents(documents)
print(f"✅ Created {len(chunks)} chunks from your documents.")

# Generate Embeddings + Store in ChromaDB 
print("\n🧠 Generating embeddings and storing in ChromaDB...")
print("   (This may take a few minutes depending on document size)")

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DB_DIR   # saves to ./chroma_db folder
)

print(f"\n✅ Successfully stored {len(chunks)} chunks in ChromaDB.")
print(f"   Location: {CHROMA_DB_DIR}")
print("\n🚀 RAG knowledge base is ready! Run: streamlit run chatbot.py")