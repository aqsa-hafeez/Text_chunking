from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

# ========== LOAD PDF ==========
def load_pdf(file_path):
    print("📄 Loading PDF...")
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

# ========== SEMANTIC CHUNKING ==========
def semantic_chunking(documents):
    print("🧠 Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    print("✂️ Performing semantic chunking...")
    text_splitter = SemanticChunker(embeddings)
    chunks = text_splitter.split_documents(documents)
    return chunks

# ========== SAVE CHUNKS ==========
def save_chunks(chunks, filename="pdf_chunks.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            f.write(f"\n\n--- CHUNK {i+1} ---\n")
            f.write(chunk.page_content)

    print(f"✅ Chunks saved to {filename}")

# ========== MAIN ==========
file_path = input("Enter PDF file path: ")

documents = load_pdf(file_path)
chunks = semantic_chunking(documents)
save_chunks(chunks)
