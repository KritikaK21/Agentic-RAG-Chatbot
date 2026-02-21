from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma  # updated import
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Load documents from a folder
def load_documents(directory="data"):
    loader = DirectoryLoader(directory, glob="**/*.txt")
    docs = loader.load()
    return docs

# Split into smaller chunks
def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# HuggingFace embeddings
def create_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)

# Create or load Chroma vector store
def get_vector_store(docs, embeddings, persist_directory="chroma_db"):
    if os.path.exists(persist_directory):
        print("🔁 Loading existing Chroma vector store...")
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    else:
        print("💾 Creating new Chroma vector store...")
        vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_directory)
        vectordb.persist()
    return vectordb

# Build retriever
def build_retriever():
    raw_docs = load_documents()
    split_docs = split_documents(raw_docs)
    embeddings = create_embeddings()
    vector_store = get_vector_store(split_docs, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever

# Allow file-based ingestion
def rebuild_retriever_from_uploaded_files(file_paths):
    documents = []
    for path in file_paths:
        loader = TextLoader(path)
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)

    embeddings = create_embeddings()
    vector_store = Chroma.from_documents(documents=split_docs, embedding=embeddings, persist_directory="chroma_db")
    vector_store.persist()

    return vector_store.as_retriever(search_kwargs={"k": 3})

# Test run
if __name__ == "__main__":
    retriever = build_retriever()
    results = retriever.invoke("What is LangChain?")
    for i, doc in enumerate(results):
        print(f"\n--- Document {i+1} ---\n{doc.page_content}")

