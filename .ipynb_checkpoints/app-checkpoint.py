import streamlit as st
import pandas as pd
import numpy as np

# Título do App
st.title('🔮 Churn Prediction System')

# Texto explicativo
st.write('Este sistema prevê a probabilidade de um cliente cancelar o contrato.')

# Criando botões para o usuário digitar
st.sidebar.header('Dados do Cliente')

idade = st.sidebar.slider('Idade', 18, 80, 30)
fatura = st.sidebar.number_input('Fatura Mensal ($)', min_value=0.0, value=50.0)
contrato = st.sidebar.slider('Tempo de Contrato (meses)', 1, 72, 12)

# Botão para prever
if st.button('Calcular Risco'):
    # Lógica simples apenas para teste (depois colocaremos a IA real)
    risco = (fatura / 200) - (contrato / 100)
    
    if risco > 0.5:
        st.error(f'Risco Alto! Score: {risco:.2f}')
    else:
        st.success(f'Cliente Seguro. Score: {risco:.2f}')