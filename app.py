import streamlit as st
import os
from chatbot import carregar_chatbot

# 🔑 Coloque sua chave da OpenAI aqui (ex: sk-...)
import os
import streamlit as st

# Acessa a chave de forma segura via Streamlit Cloud Secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# 📄 Nome exato do seu PDF (esse arquivo deve estar no repositório)
PDF_PATH = "essentiallife02 (1).pdf"

# 🚀 Carrega o chatbot baseado no PDF
chatbot = carregar_chatbot(PDF_PATH)

# 🌿 Interface do app
st.set_page_config(page_title="Aromabot", page_icon="🌿")
st.title("🌿 Aromabot - Seu consultor de bem-estar com IA")
st.write("Digite sua dúvida ou sintoma e veja o que os óleos essenciais podem fazer por você!")

# ⌨️ Campo de pergunta
pergunta = st.text_input("Digite sua pergunta:")

# 🤖 Obter resposta da IA
if pergunta:
    with st.spinner("🔍 Procurando resposta com IA..."):
        resposta = chatbot.run(pergunta)
        st.success(resposta)
