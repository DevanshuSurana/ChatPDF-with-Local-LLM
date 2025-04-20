import streamlit as st
# New imports from langchain_community
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
import os
import tempfile

st.set_page_config(page_title="📄 Local ChatPDF with Ollama")

st.title("📄 ChatPDF using Local LLM")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    loader = PyPDFLoader(tmp_file_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    st.info("✅ PDF Loaded & Chunked")

    # Use FAISS for local vector store
    embeddings = OllamaEmbeddings(model="mistral")
    vectorstore = FAISS.from_documents(texts, embeddings)

    retriever = vectorstore.as_retriever()
    llm = Ollama(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    query = st.text_input("Ask a question about the PDF:")
    if query:
        with st.spinner("Thinking..."):
            result = qa_chain.invoke(query)
            st.success(result)
