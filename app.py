import streamlit as st
import pandas as pd
import joblib

# 1. Carregar o Modelo Inteligente
try:
    modelo = joblib.load('modelo_churn.pkl')
except FileNotFoundError:
    st.error("Erro: O arquivo 'modelo_churn.pkl' não foi encontrado. Rode a célula de salvamento no Jupyter!")

# 2. Título e Design
st.title('🔮 Sistema de Previsão de Rotatividade')
st.write('Use Inteligência Artificial para prever se o cliente vai cancelar.')

st.sidebar.header('📝 Dados do Cliente')

# 3. Coletando os dados (EXATAMENTE iguais aos do treino)
idade = st.sidebar.slider('Idade', 18, 80, 30)
fatura = st.sidebar.number_input('Fatura Mensal ($)', min_value=0.0, max_value=200.0, value=70.0)
contrato = st.sidebar.slider('Tempo de Contrato (meses)', 1, 72, 12)

# 4. Botão de Previsão
if st.button('Analisar Risco'):
    
    # Criar uma tabela com os dados do cliente (igual ao X_test)
    dados_cliente = pd.DataFrame({
        'idade': [idade],
        'fatura_mensal': [fatura],
        'tempo_contrato': [contrato]
    })
    
    # A MÁGICA: O modelo faz a previsão
    predicao = modelo.predict(dados_cliente)
    # Também podemos pegar a probabilidade (certeza)
    probabilidade = modelo.predict_proba(dados_cliente)
    
    # Mostrando o resultado
    if predicao[0] == 1:
        certeza = probabilidade[0][1] * 100
        st.error(f'🚨 ALERTA DE CHURN! O modelo prevê que este cliente VAI SAIR.')
        st.write(f'Probabilidade de saída: **{certeza:.2f}%**')
    else:
        certeza = probabilidade[0][0] * 100
        st.success(f'✅ Cliente Seguro. O modelo prevê que ele VAI FICAR.')
        st.write(f'Probabilidade de ficar: **{certeza:.2f}%**')