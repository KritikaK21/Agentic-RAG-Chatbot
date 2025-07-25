from rag_agent import build_retriever
from transformers import pipeline

# 1. Load the retriever
retriever = build_retriever()

# 2. Load a lightweight HuggingFace model (flan-t5-base)
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    tokenizer="google/flan-t5-base",
    max_new_tokens=300
)

# 3. Function to format a better prompt and generate an answer
def generate_answer(query):
    # Get top documents from vector store
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs])

    # 🧠 Improved prompt for better LLM behavior
    prompt = f"""You are an intelligent assistant. Answer the question below based **only** on the provided context.

Context:
{context}

Question: {query}

If the answer is not in the context, say "I don't know."

Answer:"""

    # Generate response using the model
    result = generator(prompt)
    return result[0]["generated_text"]

# 4. CLI-style interface
if __name__ == "__main__":
    user_question = input("Ask a question: ")
    response = generate_answer(user_question)
    print("\n🤖 Answer:\n", response)
