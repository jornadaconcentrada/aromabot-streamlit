import os
import fitz  # PyMuPDF
import streamlit as st

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


# Função para extrair texto do PDF
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    doc = fitz.open(caminho_pdf)
    for pagina in doc:
        texto += pagina.get_text()
    # Debug: Mostra uma prévia do texto extraído
    st.write("📄 Prévia do texto extraído do PDF:")
    st.code(texto[:1000])
    return texto


# Função para dividir o texto em pedaços (chunks)
def dividir_em_chunks(texto):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(texto)
    st.write(f"🔍 Total de pedaços (chunks) gerados: {len(chunks)}")
    return chunks


# Função para gerar vetores semânticos (embeddings)
def criar_base_vetorial(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)


# Conectar a IA GPT com o banco de vetores FAISS
def configurar_chatbot(db):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    return RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())


# Função principal que une tudo
def carregar_chatbot(caminho_pdf):
    texto = extrair_texto_pdf(caminho_pdf)
    chunks = dividir_em_chunks(texto)
    db = criar_base_vetorial(chunks)
    chatbot = configurar_chatbot(db)
    return chatbot
