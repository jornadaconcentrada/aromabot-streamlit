import streamlit as st
from chatbot import carregar_chatbot

# ✅ Esta linha DEVE ser a primeira chamada do Streamlit
st.set_page_config(page_title="Aromabot", page_icon="🌿")

PDF_PATH = "essentiallife02 (1).pdf"
chatbot = carregar_chatbot(PDF_PATH)

st.title("🌿 Aromabot - Seu consultor de bem-estar com IA")
st.write("Digite sua dúvida ou sintoma e veja o que os óleos essenciais podem fazer por você!")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    st.write("🔍 Procurando resposta...")
    resposta = chatbot.run(pergunta)
    st.success(resposta)
