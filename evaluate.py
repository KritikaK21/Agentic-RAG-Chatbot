from rag_pipeline import generate_answer

# Test questions with expected keywords
test_cases = [
    {
        "question": "What is LangChain?",
        "expected_keywords": ["framework", "language models", "applications"]
    },
    {
        "question": "What is RAG?",
        "expected_keywords": ["retrieval", "augmented", "generation"]
    },
    {
        "question": "What vector stores does LangChain support?",
        "expected_keywords": ["FAISS", "Chroma", "Pinecone"]
    },
    {
        "question": "What embedding models does LangChain integrate with?",
        "expected_keywords": ["OpenAI", "Hugging Face", "Cohere"]
    },
    {
        "question": "What can LangChain be used to build?",
        "expected_keywords": ["chatbots", "Q&A", "document search"]
    },
    {
        "question": "What does LangChain allow developers to combine with LLMs?",
        "expected_keywords": ["memory", "tools", "APIs"]
    },
    {
        "question": "What are LangChain agents?",
        "expected_keywords": ["reasoning", "tools", "dynamically"]
    },
]

def evaluate():
    print("🧪 Running Evaluation...\n")
    passed = 0

    for i, test in enumerate(test_cases):
        question = test["question"]
        expected = test["expected_keywords"]

        answer = generate_answer(question).lower()
        matched = [kw for kw in expected if kw.lower() in answer]
        success = len(matched) >= 1  # Pass if at least 1 keyword found

        status = "✅ PASS" if success else "❌ FAIL"
        if success:
            passed += 1

        print(f"Q{i+1}: {question}")
        print(f"Answer: {answer[:150]}...")
        print(f"Matched keywords: {matched}")
        print(f"Status: {status}\n")

    accuracy = (passed / len(test_cases)) * 100
    print(f"{'='*40}")
    print(f"✅ Passed: {passed}/{len(test_cases)}")
    print(f"📊 Accuracy: {accuracy:.1f}%")
    print(f"{'='*40}")

if __name__ == "__main__":
    evaluate()
