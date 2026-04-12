import gradio as gr
from main import CoordinatorAgent
import os

# Initialize coordinator once
coordinator = CoordinatorAgent()

def chat(query, file, history):
    if not query:
        return history, ""
    
    file_path = None
    if file is not None:
        file_path = file.name
    
    answer = coordinator.handle_query(query, file_path)
    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": answer})
    return history, ""

# Build UI
with gr.Blocks(title="Agentic RAG Chatbot") as demo:
    gr.Markdown("# 🤖 Agentic RAG Chatbot")
    gr.Markdown("Multi-agent architecture · ChromaDB · LangChain · flan-t5")
    
    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(
                label="📄 Upload Document",
                file_types=[".pdf", ".docx", ".csv", ".pptx", ".txt"]
            )
            gr.Markdown("Supported: PDF, DOCX, CSV, PPTX, TXT")
        
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Chat", height=400, type="messages")
            question_input = gr.Textbox(
                placeholder="Ask a question about your document...",
                label="Your Question"
            )
            with gr.Row():
                submit_btn = gr.Button("Send", variant="primary")
                clear_btn = gr.Button("Clear")
    
    submit_btn.click(
        fn=chat,
        inputs=[question_input, file_input, chatbot],
        outputs=[chatbot, question_input]
    )
    
    clear_btn.click(
        fn=lambda: ([], ""),
        outputs=[chatbot, question_input]
    )

if __name__ == "__main__":
    demo.launch()