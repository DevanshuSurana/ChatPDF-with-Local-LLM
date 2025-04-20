# 📄 ChatPDF with Local LLM

This is a **Streamlit** application that allows you to upload a PDF document and interact with it using a **local LLM (Large Language Model)** powered by **Ollama**. The app processes the uploaded PDF, chunks the text, and enables users to ask questions about the document content. The model responds with relevant information based on the query.

## 🚀 Features
- Upload a PDF document to the app.
- Extract and chunk text from the PDF.
- Use **Ollama** (powered by models like `mistral`) for querying.
- Retrieve relevant answers from the document.
- Built with **LangChain** for handling embeddings, vector storage, and question answering.

## 🛠️ Technologies Used
- **Streamlit**: For building the web interface.
- **LangChain**: For document processing, embeddings, and question answering.
- **Ollama**: LLM for generating responses based on the document content.
- **FAISS**: For fast similarity search and local vector storage.
- **PyPDF**: For loading and extracting text from PDF files.

## 📝 Installation

### Prerequisites
Before running the application, ensure that you have **Ollama** installed locally. You can download and install it from [https://ollama.com](https://ollama.com). 

### 1. Install Ollama

1. Visit [Ollama’s website](https://ollama.com) to download the appropriate version for your operating system.
2. After downloading, follow the installation instructions to install **Ollama**.

Once installed, you can start the Ollama service by running the following command:

```bash
ollama serve
