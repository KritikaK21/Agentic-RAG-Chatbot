# 🤖 Agentic Retrieval-Augmented QA System for Multi-Format Documents (MCP-Inspired Architecture)

This project implements an **Agentic Retrieval-Augmented Generation (RAG) system** that answers natural-language questions from documents in multiple formats including **PDF, DOCX, PPTX, CSV, and TXT**.

The system follows a **modular agent-based architecture inspired by the Model Context Protocol (MCP)** — where ingestion, retrieval, and response-generation agents communicate using structured JSON messages. This improves **traceability, modularity, and robustness** compared to monolithic RAG pipelines.

A **Streamlit UI** is included for document upload and interactive Q&A.

---

## Key Features

- Multi-format document support: PDF, DOCX, PPTX, CSV, TXT  
- Agent-based architecture:
  - Ingestion Agent
  - Retrieval Agent
  - LLM Response Agent
- MCP-style JSON structured message passing
- Semantic search using embeddings + vector database
- Context-aware LLM responses
- Streamlit-based chat UI
- Modular, debuggable design suitable for real-world systems

---

## 📸 Screenshots

### 🔹 Initial Setup
![Initial Setup](screenshots/initial_setup.png)

### 🔹 Creating Vector Store
![Create Vectorstore](screenshots/create_vectorstore.png)

### 🔹 Loading PDF
![Load PDF](screenshots/load_pdf.png)

### 🔹 Q&A Code Block
![Q&A Code](screenshots/qa_code.png)

### 🔹 Q&A Output in Streamlit
![Q&A Output](screenshots/qa_output.png)

---

## System Architecture
```
User → Streamlit UI → Coordinator Agent
├── Ingestion Agent → Extracts & chunks documents
├── Retrieval Agent → Embeds & retrieves top-k chunks
└── LLM Response Agent → Generates final response
```

Agents communicate through MCP-style structured JSON messages.

### Example MCP-Style Message

```
{
  "type": "CONTEXT_RESPONSE",
  "sender": "RetrievalAgent",
  "receiver": "LLMResponseAgent",
  "trace_id": "abc-123",
  "payload": {
    "top_chunks": ["..."],
    "query": "What are the KPIs?"
  }
}
```

## 🧰 Tech Stack
| Component        | Tool / Framework                          |
| ---------------- | ----------------------------------------- |
| UI               | Streamlit                                 |
| LLM              | OpenAI / HuggingFace                      |
| Embeddings       | Sentence Transformers                     |
| Vector Store     | FAISS / Chroma                            |
| File Parsing     | PyMuPDF, python-docx, pandas, python-pptx |
| Agents           | Python modules                            |
| Message Protocol | MCP (custom JSON structure)               |

## Supported File Types
- PDF
- DOCX
- PPTX
- CSV
- TXT

## Installation and Local Setup

**1. Clone the Repository**
```
git clone https://github.com/<your-username>/agentic-rag-qa.git
cd agentic-rag-qa
```

**2. Create a Virtual Environment (Recommended)** 
```
python -m venv venv
source venv/bin/activate   # Mac / Linux
venv\Scripts\activate      # Windows
```

**3. Install Dependencies**
```
pip install -r requirements.txt
```

**4. Configure Environment Variables**
Create a .env file in the project root and add:
```
OPENAI_API_KEY=your_key_here
(or your HuggingFace token, depending on configuration)
```

**5. Run the Application**
```
streamlit run app.py
```
**Upload files and start asking questions.**

## Retrieval Pipeline Overview
- Documents are uploaded and parsed
- Text is chunked
- Chunks are embedded
- Vectors are stored in FAISS/Chroma
- Relevant chunks are retrieved
- The LLM generates a grounded response

**Key configurable parameters include:**
- Chunk size
- Overlap
- Top-k retrieval
- Similarity threshold

## Why Agentic Architecture?
Unlike traditional monolithic RAG systems, this project uses separation of concerns through agents, which enables:
- Easier debugging and observability
- Cleaner modularity
- Replaceable components
- Realistic production-style design

## Example Questions
- Summarize the key findings across all uploaded documents
- What KPIs are mentioned in these files?
- Extract financial metrics from the reports
- What decisions or recommendations are discussed?

## Challenges Addressed
- Parsing and normalizing multiple document formats
- Preserving context relevance during retrieval
- Designing structured agent communication
- Managing chunk size and window selection
- Reducing hallucinations through grounded retrieval

## Future Enhancements
- Deployment on Hugging Face or cloud platforms
- Authentication and persistent chat history
- Redis/Kafka-based message bus
- LangGraph / LangChain integration
- Evaluation dashboard and reporting

## Project Objective

This project demonstrates:
- Practical GenAI system design
- Agent-based orchestration
- Retrieval-grounded answering
- Handling unstructured documents
- UI + backend integration

## Author
**Kritika Aggarwal**
**GitHub:** https://github.com/KritikaK21
**LinkedIn:** linkedin.com/in/kritika-aggarwal-734997249/

## License
This project is available under the license of your choice (MIT recommended).
