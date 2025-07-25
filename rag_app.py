from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
import gradio as gr

# Load and split the data
loader = TextLoader("data.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create embeddings and vector store
embedding = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)

# Use HuggingFaceHub LLM (you can also use OpenAI if you have API key)
llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature": 0.5, "max_length": 100})

# Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Gradio UI
def rag_app(query):
    return qa_chain.run(query)

demo = gr.Interface(fn=rag_app, inputs="text", outputs="text", title="Simple RAG App")
