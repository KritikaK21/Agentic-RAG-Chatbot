from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

class LLMResponseAgent:
    def __init__(self):
        self.name = "LLMResponseAgent"
        print("⏳ Loading local LLM...")
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=200
        )
        print("✅ Local LLM ready.")

    def generate(self, message):
        query = message["payload"]["query"]
        docs = message["payload"]["docs"]
        
        context = "\n\n".join(docs)
        
        prompt = f"""Answer the question based on the context below.

Context:
{context}

Question: {query}

Answer:"""

        result = self.generator(prompt)
        
        return {
            "sender": self.name,
            "receiver": "User",
            "type": "RESPONSE_GENERATED",
            "payload": {
                "query": query,
                "answer": result[0]["generated_text"]
            }
        }