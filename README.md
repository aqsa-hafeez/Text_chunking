# AI Semantic Text Chunking 🧠✂️

A high-precision document processing tool that uses sentence embeddings to break large PDF files into semantically meaningful chunks. This is an essential component for building accurate RAG (Retrieval-Augmented Generation) systems.

## 🌟 Key Features
* **Semantic Splitting**: Instead of fixed character counts, it splits text based on changes in meaning and context.
* **BGE Embedding Integration**: Powered by `BAAI/bge-small-en-v1.5`, a state-of-the-art model for text representation.
* **Context-Aware RAG**: Ensures that related information stays together, reducing hallucinations in LLM responses.
* **PDF Support**: Direct loading and processing of PDF documents using `PyPDFLoader`.

## 🛠️ Tech Stack
* **Language**: Python
* **Framework**: [LangChain](https://www.langchain.com/)
* **Embedding Model**: BGE-Small-v1.5 (via HuggingFace)
* **Libraries**: `langchain-experimental`, `sentence-transformers`, `pypdf`

## 📋 How It Works
The algorithm measures the "distance" between sentence embeddings. If the distance between two consecutive sentences exceeds a dynamic threshold, a new chunk is created.

1. **Extraction**: Reads text from the provided PDF path.
2. **Embedding**: Converts sentences into mathematical vectors.
3. **Threshold Analysis**: Analyzes where topic shifts occur.
4. **Export**: Saves the resulting chunks into a labeled text file (`pdf_chunks.txt`).

## 💻 Installation & Usage

1. **Clone the repo**:
   ```bash
   git clone [https://github.com/aqsa-hafeez/Text_chunking.git](https://github.com/aqsa-hafeez/Text_chunking.git)

```

2. **Install Dependencies**:
```bash
pip install langchain-experimental langchain-community sentence-transformers pypdf

```


3. **Run the Script**:
```bash
python Chunking.py

```


*Enter the path of your PDF when prompted.*

## 📊 Sample Output

Input: A 50-page research paper.
Output: `pdf_chunks.txt` containing segments where each chunk represents a single cohesive idea or topic.

```text
--- CHUNK 1 ---
[Content about Introduction and Problem Statement]

--- CHUNK 2 ---
[Content about Methodology and Proposed System]

```

## 🚀 Use Cases

* **Vector Database Pre-processing**: Indexing documents into FAISS, ChromaDB, or Pinecone.
* **LLM Context Window Optimization**: Feeding only relevant, complete ideas to models like GPT-4 or Gemini.
* **Document Summarization**: Creating summaries for specific sections of a large book.

---
