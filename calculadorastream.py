import streamlit as st 
# Título da aplicação 
st.title("Calculadora de Soma") 
# Campos para entrada dos números 
num1 = st.number_input("Digite o primeiro número", value=0) 
num2 = st.number_input("Digite o segundo número", value=0) 
# Botão para calcular 
if st.button("Calcular Soma"): 
    resultado = num1 + num2
    st.success(f"O resultado da soma é: {resultado}")