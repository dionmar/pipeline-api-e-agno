import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Streamlit Component Showcase", layout="wide")

# Título e Introdução
st.title("🔗 Streamlit Component Showcase")
st.markdown("Explore os principais componentes do Streamlit com exemplos interativos.")

# 1. Text Components
st.header("📝 Text Components")
st.subheader("1. st.write")
st.write("Streamlit é uma ferramenta incrível para criar aplicações web com Python!")
st.text("Texto simples sem formatação.")
st.markdown("**Markdown** é muito útil para formatação.")
st.code("st.write('Hello, Streamlit!')", language="python")

# 2. Media Components
st.header("🖼️ Media Components")
st.subheader("2. st.image")
st.image("https://via.placeholder.com/400", caption="Placeholder Image", use_column_width=True)

st.subheader("3. st.video")
st.video("https://www.youtube.com/watch?v=0rpDD5aaJ_Q")

st.subheader("4. st.audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 3. Data Display Components
st.header("📊 Data Display Components")
st.subheader("5. st.dataframe")
data = pd.DataFrame(np.random.randn(10, 5), columns=[f'Col {i}' for i in range(1, 6)])
st.dataframe(data)

st.subheader("6. st.table")
st.table(data.head())

st.subheader("7. st.metric")
st.metric(label="Temperature", value="72 °F", delta="-2 °F")

# 4. Input Components
st.header("📝 Input Components")
st.subheader("8. st.text_input")
name = st.text_input("Digite seu nome:")
st.write(f"Olá, {name}!")

st.subheader("9. st.text_area")
feedback = st.text_area("Deixe seu feedback:")
st.write(f"Feedback recebido: {feedback}")

st.subheader("10. st.number_input")
number = st.number_input("Escolha um número", min_value=0, max_value=100, step=1)
st.write(f"Você escolheu: {number}")

st.subheader("11. st.slider")
slide_value = st.slider("Ajuste o valor", 0, 100, 50)
st.write(f"Valor do slider: {slide_value}")

st.subheader("12. st.selectbox")
option = st.selectbox("Escolha uma linguagem de programação", ["Python", "JavaScript", "C++", "Rust"])
st.write(f"Você escolheu: {option}")

st.subheader("13. st.checkbox")
checkbox = st.checkbox("Marque para confirmar")
st.write(f"Checkbox marcado: {checkbox}")

st.subheader("14. st.radio")
radio = st.radio("Escolha uma cor", ["Vermelho", "Verde", "Azul"])
st.write(f"Cor escolhida: {radio}")

st.subheader("15. st.button")
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")

# 5. Visualization Components
st.header("📊 Visualization Components")
st.subheader("16. st.line_chart")
st.line_chart(data)

st.subheader("17. st.bar_chart")
st.bar_chart(data)

st.subheader("18. st.pyplot")
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Gráfico com Matplotlib")
st.pyplot(fig)

# 6. Status Components
st.header("🕒 Status Components")
st.subheader("19. st.progress")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)

st.subheader("20. st.spinner")
with st.spinner("Carregando..."):
    time.sleep(2)
st.success("Carregamento concluído!")

# Footer
st.markdown("---")
st.markdown("Feito com 💙 por Luciano Vasconcelos")
