# Inserir Dados do arquivo CSV na tabela do banco 'teste'

import pandas as pd
from sqlalchemy import create_engine
import mariadb
import streamlit as st

# Conecção com o banco de dados usando o sqlalchemy pois o pandas só trabalha com esse tipo de conecção
#connection_string = 'mysql+mariadbconnector://user01:pi@localhost/teste'
#engine = create_engine(connection_string)

#df = pd.read_csv('dados_temperatura.csv')

#Conectar ao banco de dados
try:
    conecao = mariadb.connect(
        user="user01",
        password="pi",
        host="localhost",
        database="teste"
    )

except mariadb.Error as e:
    print(f"ERROR DE CONECÇÃO COM O BANCO")
    sys.exit(1)


#Inserir os dados na tabela do banco de dados
#df.to_sql('temperatura',engine,if_exists='append',index=False)

cursor = conecao.cursor()
cursor.execute("SELECT * FROM temperatura;")

resultado = cursor.fetchall()

temperatura = []
data = []

if resultado:
    for linha in resultado:
        temperatura.append(linha[1])
        data.append(linha[2])
else:
    print("Nenhum resultado encontrado")


#Cria um DataFrame
df = pd.DataFrame({'Temperatura':temperatura, 'Data':data})

# Apaga o index do meu dataframe
df = df.reset_index(drop=True)

#markdown
st.write("""
# Gráfico de temperatura
Monitoramento de temperatura da estufa
""")

# Converte os meus dados da temperatura para numeros.(EU acho que o código não conseguiu converter os valores DECIMAL do banco)
df['Temperatura'] = pd.to_numeric(df['Temperatura'])

# Mostra os tipos de dados do meu dataframe
print('TIPO DE DADOS:')
print(df.dtypes)

st.line_chart(df, x='Data',y='Temperatura')

#markdown
st.write("""
# Fim do App
""")

cursor.close()
conecao.close()