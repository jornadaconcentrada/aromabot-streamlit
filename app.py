import streamlit as st
import os
from chatbot import carregar_chatbot

# Defina sua chave da OpenAI (não exponha essa chave em produção!)
os.environ["OPENAI_API_KEY"] = "sua-chave-aqui"

# Carrega o chatbot com base no PDF
chatbot = carregar_chatbot("essential-life_Guia-óleos-individuais.pdf")

# Interface do usuário
st.set_page_config(page_title="Aromabot", page_icon="🌿")
st.title("🌿 Aromabot - Seu consultor de bem-estar com IA")
st.write("Digite sua dúvida ou sintoma e veja o que os óleos essenciais podem fazer por você!")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    st.write("🔍 Procurando resposta...")
    resposta = chatbot.run(pergunta)
    st.success(resposta)
