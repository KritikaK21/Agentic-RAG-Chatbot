import os
from rag_agent import build_retriever
from agentsingestion_agent import IngestionAgent
from retrieval_agent import RetrievalAgent
from llm_agent import LLMResponseAgent

class CoordinatorAgent:
    def __init__(self):
        self.name = "CoordinatorAgent"
        print("🚀 Initializing agents...")
        
        self.ingestion_agent = IngestionAgent()
        
        retriever = build_retriever()
        self.retrieval_agent = RetrievalAgent(retriever)
        
        self.llm_agent = LLMResponseAgent()
        
        print("✅ All agents ready.")

    def handle_query(self, query, file_path=None):
        # Step 1 — If file uploaded, ingest it first
        if file_path:
            print(f"📄 Ingesting file: {file_path}")
            self.ingestion_agent.ingest(file_path)

        # Step 2 — Retrieve relevant docs
        print(f"🔍 Retrieving docs for: {query}")
        retrieval_message = self.retrieval_agent.retrieve(query)

        # Step 3 — Generate answer
        print("🤖 Generating answer...")
        response_message = self.llm_agent.generate(retrieval_message)

        return response_message["payload"]["answer"]


if __name__ == "__main__":
    coordinator = CoordinatorAgent()
    
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = coordinator.handle_query(query)
        print(f"\n🤖 Answer: {answer}")