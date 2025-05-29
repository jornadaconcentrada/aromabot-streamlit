import fitz  # PyMuPDF
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# Função que lê o PDF
def extrair_texto_pdf(caminho_pdf):
    texto = ""
    doc = fitz.open(caminho_pdf)
    for pagina in doc:
        texto += pagina.get_text()
    return texto

# Divide o texto em pedaços menores
def dividir_em_chunks(texto):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(texto)

# Gera vetores semânticos a partir dos chunks
def criar_base_vetorial(chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)

# Conecta a IA GPT para responder com base na base vetorial
def configurar_chatbot(db):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    return RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Função principal que junta tudo
def carregar_chatbot(caminho_pdf):
    texto = extrair_texto_pdf(caminho_pdf)
    chunks = dividir_em_chunks(texto)
    db = criar_base_vetorial(chunks)
    chatbot = configurar_chatbot(db)
    return chatbot
