# Detecção de Phishing em Páginas Web

Análise exploratória de um dataset com características estruturais de URLs, buscando entender quais atributos mais se relacionam com páginas de phishing.

## Fonte dos dados

Dataset **Web Page Phishing** (Kaggle), com ~100 mil registros. Cada linha representa uma URL, descrita por atributos como comprimento, número de pontos, hífens, barras, símbolos especiais (`@`, `%`, `$`, `#`, etc.) e número de redirecionamentos, além da variável alvo `phishing` (1 = phishing, 0 = legítima).

## O que o script faz

1. Carrega o CSV e mostra visão geral (`shape`, `head`, `dtypes`).
2. Verifica a **distribuição da variável alvo** (`phishing`).
3. Calcula a **correlação de cada atributo com `phishing`**, ordenada tanto pelo valor real (para ver os mais positivos/negativos) quanto pelo valor absoluto (para achar as correlações mais fracas).
4. Compara `url_length` (comprimento da URL) entre as classes phishing/legítima com estatísticas descritivas (`describe`).
5. Compara `n_redirection` (número de redirecionamentos) entre as classes da mesma forma.
6. Gera um **heatmap de correlação** de todas as variáveis do dataset (`seaborn`).

## Como executar

```bash
pip install -r requirements.txt
python analise_phishing.py
```

## Estrutura do repositório

```
├── analise_phishing.py         # script principal da análise
├── web-page-phishing.csv       # dataset original (~100k registros)
├── relatorio_phishing.docx     # relatório formatado com os resultados
├── requirements.txt
└── README.md
```

## Relatório

O arquivo `relatorio_phishing.docx` documenta a análise em português, com a interpretação das correlações encontradas e quais características de URL mais indicam risco de phishing.
