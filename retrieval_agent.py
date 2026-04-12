class RetrievalAgent:
    def __init__(self, retriever):
        self.name = "RetrievalAgent"
        self.retriever = retriever

    def retrieve(self, query):
        docs = self.retriever.get_relevant_documents(query)
        
        message = {
            "sender": self.name,
            "receiver": "LLMResponseAgent",
            "type": "DOCS_RETRIEVED",
            "payload": {
                "query": query,
                "docs": [doc.page_content for doc in docs]
            }
        }
        return message
