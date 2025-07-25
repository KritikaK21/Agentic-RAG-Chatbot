# 🤖 Agentic RAG Chatbot

A powerful Retrieval-Augmented Generation (RAG) based chatbot enhanced with **LangChain**, **OpenAI**, and **FAISS**, allowing document-aware conversational AI with agentic behavior.

---

## 📌 Project Overview

This chatbot is capable of:

- 📄 Reading PDF documents  
- 🔍 Retrieving relevant content  
- 💬 Answering queries based on that content using **LLMs**  
- 🧠 Acting agentically to perform more complex tasks  

It uses **LangChain Agents** and **Tools** to extend the chatbot's capabilities beyond basic Q&A.

---

## 🧰 Tech Stack

- **Python**
- **LangChain**
- **OpenAI API**
- **FAISS**
- **PyPDF2**
- **Streamlit** (for UI)

---

## 📁 Folder Structure

Agentic-RAG-Chatbot/
│
├── app.py # Main Streamlit App
├── helper.py # PDF processing & utilities
├── requirements.txt # Required Python packages
├── .env # API keys (excluded from Git)
├── .gitignore # Git ignore rules
├── README.md # Project documentation
└── data/
└── project.pdf # Sample PDF file for testing

---

## 🚀 Getting Started

### 1. Clone the Repo

```
git clone https://github.com/KritikaK21/Agentic-RAG-Chatbot.git
cd Agentic-RAG-Chatbot
```

### 2. Set up Virtual Environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Add Your API Keys
Create a .env file in the root directory and add:
```
OPENAI_API_KEY=your-openai-api-key
```

✅ Make sure your ```.env``` file is listed in ```.gitignore```


## 🧪 How It Works

1. **Upload a PDF file**

2. **Chunks** are created using LangChain's document loaders

3. **Embeddings** are generated using OpenAI and stored using **FAISS**

4. **LangChain Agent** uses the retriever to answer questions from the PDF

5. Interact with the chatbot via a **Streamlit** interface


## 💻 Run the App
```
streamlit run app.py
```
Open http://localhost:8501 in your browser


## 🧠 Agent Tools & Features
* PDF Question Answering

* LangChain Conversational Retrieval Chain

* Dynamic Prompting

* Agent + Tool architecture for task delegation

## 📸 Demo
Coming soon!

## 🙋‍♀️ Author
Kritika Aggarwal
🚀 LinkedIn | 🌐 Portfolio (add if available)

## 📄 License
This project is licensed under the MIT License.

## ⭐️ Show your support
If you find this project helpful, please give it a ⭐️ on GitHub!
Feel free to fork, clone, and improve!

---
