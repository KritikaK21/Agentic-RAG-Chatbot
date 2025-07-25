from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# 1. Load Documents from the 'data' folder
def load_documents(directory="data"):
    loader = DirectoryLoader(directory, glob="**/*.txt")  # Loads all .txt files in 'data'
    docs = loader.load()
    return docs

# 2. Split Documents into Chunks
def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# 3. Create HuggingFace Embeddings
def create_embeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)

# 4. Create or Load Vector Store (Chroma)
def get_vector_store(docs, embeddings, persist_directory="chroma_db"):
    if os.path.exists(persist_directory):
        print("🔁 Loading existing Chroma vector store...")
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    else:
        print("💾 Creating new Chroma vector store...")
        vectordb = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_directory)
        vectordb.persist()
    return vectordb

# 5. Build Retriever for Querying
def build_retriever():
    raw_docs = load_documents()
    split_docs = split_documents(raw_docs)
    embeddings = create_embeddings()
    vector_store = get_vector_store(split_docs, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever

# 6. Optional Test: Query the Retriever
if __name__ == "__main__":
    retriever = build_retriever()
    results = retriever.get_relevant_documents("What is this project about?")
    for i, doc in enumerate(results):
        print(f"\n--- Document {i+1} ---\n{doc.page_content}")
