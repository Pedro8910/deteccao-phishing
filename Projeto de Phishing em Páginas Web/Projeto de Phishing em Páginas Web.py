#Análise de Phishing em Páginas Web#
import pandas as pd
import matplotlib.pyplot as plt   
import seaborn as sns
# Carrega o arquivo CSV para um DataFrame do pandas
df = pd.read_csv('web-page-phishing.csv')

# --- Visão geral dos dados ---
print(df.shape)          # (linhas, colunas) — dimensões do dataset
print(df.head())         # primeiras 5 linhas, para inspecionar os dados
print(df.dtypes)         # tipo de cada coluna (int, float, etc.)
# Conta quantas URLs são phishing (1) e quantas são legítimas (0)
print(df['phishing'].value_counts())
corr = df.corr()['phishing']       
corr = corr.drop('phishing')       
corr = corr.sort_values(ascending=False)  
print(corr)
print(corr.abs().sort_values())
print(df.groupby('phishing')['url_length'].describe())
print(df.groupby('phishing')['n_redirection'].describe)

# Define o tamanho da figura (largura=10, altura=8 polegadas)
# Um tamanho maior ajuda a caber todos os rótulos das ~19 colunas sem sobrepor
plt.figure(figsize=(10, 8))

# Cria o heatmap (mapa de calor) da matriz de correlação
sns.heatmap(
    df.corr(),        # calcula a correlação de Pearson entre todas as colunas numéricas do DataFrame
    annot=True,        # escreve o valor numérico da correlação dentro de cada célula
    fmt='.2f',         # formata esses números com 2 casas decimais (ex: 0.61 em vez de 0.611472...)
    cmap='coolwarm',   # paleta de cores: azul para valores negativos, vermelho para positivos
    center=0           # centraliza a escala de cores no zero, então correlações fracas ficam claras/neutras
                        # e correlações fortes (positivas ou negativas) ficam bem destacadas
)

# Ajusta automaticamente os espaçamentos para que rótulos longos não fiquem cortados
plt.tight_layout()

# Exibe a figura na tela
plt.show()