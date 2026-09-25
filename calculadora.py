import streamlit as st

# Configuração da página (Aba do navegador)
st.set_page_config(
    page_title="Calculadora Dev",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone
st.title("🧮 Calculadora Interativa")
st.markdown("Uma aplicação simples e elegante para realizar operações matemáticas básicas.")

st.divider()

# Layout em colunas para os campos de entrada
col1, col2 = st.columns(2)

# 2. Campos de entrada numérica
with col1:
    num1 = st.number_input("Primeiro número:", value=0.0, step=1.0, format="%.2f")

with col2:
    num2 = st.number_input("Segundo número:", value=0.0, step=1.0, format="%.2f")

# 3. Componente de seleção da operação
operacao = st.radio(
    "Escolha a operação desejada:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

st.divider()

# 4. Botão de ação e 5. Lógica de cálculo
if st.button("Calcular", type="primary", use_container_width=True):
    if operacao == "Soma (+)":
        resultado = num1 + num2
        st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")
        st.balloons()

    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")
        st.balloons()

    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")
        st.balloons()

    elif operacao == "Divisão (/)":
        if num2 == 0.0:
            st.error("⚠️ Ops! Não é possível realizar divisão por zero.")
        else:
            resultado = num1 / num2
            st.metric(label="Resultado da Divisão", value=f"{resultado:.2f}")
            st.balloons()
    #Feito
    
