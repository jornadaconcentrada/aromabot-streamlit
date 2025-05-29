import streamlit as st

st.set_page_config(page_title="Aromabot", page_icon="🌿")
st.title("🌿 Aromabot - Seu consultor de bem-estar com IA")
st.write("Digite sua dúvida ou sintoma e veja o que os óleos essenciais podem fazer por você!")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    st.write("🔍 Procurando resposta...")
    # Aqui futuramente entra a resposta da IA
    st.success("Resposta simulada: use lavanda e vetiver para insônia.")
