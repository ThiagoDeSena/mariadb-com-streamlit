import pandas as pd
import random
import datetime

# Gerar dados aleatórios
def gerar_dados():
    return random.uniform(10,35)  #Gera números aleatórios entre 10 e 35

# Gerar um DataFrame com 1000 linhas
data = {
    'temperatura': [gerar_dados() for _ in range(1000)],
    'data': pd.date_range(start='2024-01-01', end='2024-12-15',freq='h')[0:1000]
}

df = pd.DataFrame(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('dados_temperatura.csv', index=False)