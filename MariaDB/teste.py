#Importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

#Criar as funções de carregamento de dados
    #Cotações do Itau - ITAUB4 
@st.cache_data                                                                                                                                                                             
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacao_acao = dados_acao.history(period="1d",start="2010-01-01",end="2024-12-16")
    cotacao_acao = cotacao_acao[["Close"]]
    return cotacao_acao

dados = carregar_dados("ITUB4.SA")

print('Dados:')
print(dados)

print('STREAMLIT:')
#markdown
st.write("""
# App Preço de Ações
Gráfico do preço das ações do Itaú (ITUB4) ao longo dos anos
""")

#Criar o gráfico
st.line_chart(dados)

#markdown
st.write("""
# Fim do App
""")
