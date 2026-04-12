import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Define Paths
KNOWLEDGE_DIR = "./knowledge"
CHROMA_DB_DIR = "./chroma_db"
EMBED_MODEL   = "nomic-embed-text"

# Safety Check
if not os.path.exists(KNOWLEDGE_DIR) or not os.listdir(KNOWLEDGE_DIR):
    print("❌ No files found in /knowledge folder.")
    print("   Add .txt files there first, then re-run this script.")
    exit(1)

# Load Documents
print("📂 Loading knowledge files from /knowledge...")

loader = DirectoryLoader(
    KNOWLEDGE_DIR,
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},  # critical for Sinhala Unicode
    show_progress=True
)

documents = loader.load()
print(f"✅ Loaded {len(documents)} file(s) from knowledge folder.")

# Split Into Chunks
print("\n✂️  Splitting into chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,       # smaller = better for Sinhala sentences
    chunk_overlap=30,
    length_function=len,
)

chunks = splitter.split_documents(documents)
print(f"✅ Created {len(chunks)} chunks.")

# Generate Embeddings + Store in ChromaDB
print("\n🧠 Generating embeddings and storing in ChromaDB...")
print("   (This may take a few minutes)")

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

# Clear old ChromaDB first
import shutil
if os.path.exists(CHROMA_DB_DIR):
    shutil.rmtree(CHROMA_DB_DIR)
    print("🗑️  Cleared old ChromaDB.")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DB_DIR
)

print(f"\n✅ Stored {len(chunks)} chunks in ChromaDB.")
print(f"   Location: {CHROMA_DB_DIR}")
print("\n🚀 Knowledge base ready! Run: streamlit run chatbot.py")