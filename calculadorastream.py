import streamlit as st 
# Título da aplicação 
st.title("Calculadora de Soma") 
# Campos para entrada dos números 
num1 = st.number_input("Digite o primeiro número", value=0) 
num2 = st.number_input("Digite o segundo número", value=0) 

# Criando e organizando os botões em linha
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Soma"): 
        st.success(f"O resultado da soma é: {num1 + num2}")
with col2:
    if st.button("Subtração"): 
        st.success(f"O resultado da subtração é: {num1 - num2}")
with col3:
    if st.button("Multiplicação"): 
        st.success(f"O resultado da multiplicação é: {num1 * num2}")
with col4:
    if st.button("Divisão", icon="➗"):     
        st.success(f"O resultado da divisão é: {num1 / num2}")