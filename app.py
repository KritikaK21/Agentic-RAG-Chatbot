import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline

import torch
from transformers import pipeline

# Set page
st.set_page_config(page_title="RAG Chatbot (Local)", layout="wide")
st.title("📄 Local RAG-based Chatbot (No API Required)")

# File uploader
pdf = st.file_uploader("Upload your PDF file", type="pdf")

if pdf is not None:
    # Extract text
    pdf_reader = PdfReader(pdf)
    raw_text = ""
    for page in pdf_reader.pages:
        raw_text += page.extract_text()

    # Split into chunks
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(raw_text)

    # Load local embeddings model
    st.info("Generating embeddings (local)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    # Load local LLM pipeline
    st.info("Loading local LLM (this may take a few seconds)...")
    pipe = pipeline("text2text-generation", model="google/flan-t5-small", device=0 if torch.cuda.is_available() else -1)
    llm = HuggingFacePipeline(pipeline=pipe)

    # Input prompt
    st.success("PDF successfully loaded and indexed.")
    query = st.text_input("Ask a question about the PDF:")

    if query:
        docs = vectorstore.similarity_search(query)
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)

        st.subheader("Answer:")
        st.write(response)
