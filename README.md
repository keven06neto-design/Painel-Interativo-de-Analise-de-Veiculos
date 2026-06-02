# 🚗 Painel de Análise de Veículos
## 📌 Descrição do Projeto

Este projeto consiste em uma aplicação web interativa desenvolvida com Streamlit para análise exploratória de dados de veículos. O objetivo é permitir que os usuários visualizem e filtrem informações sobre veículos de forma simples e intuitiva, utilizando gráficos interativos e métricas resumidas.

A aplicação utiliza um conjunto de dados contendo informações sobre anúncios de veículos, incluindo preço, quilometragem, modelo e ano de fabricação.

## 🎯 Objetivos
-Explorar e visualizar dados de veículos.

-Aplicar filtros dinâmicos para análise específica por modelo e ano.

-Criar visualizações interativas utilizando Plotly.

-Desenvolver uma aplicação web com Streamlit.

## 🛠 Tecnologias Utilizadas
-Python

-Pandas

-Streamlit

-Plotly Express

-Git

-GitHub

## Funcionalidades
### Indicadores Principais

A aplicação apresenta métricas resumidas para fornecer uma visão geral dos dados:

-Total de veículos disponíveis.

-Preço médio dos veículos.

-Quilometragem média dos veículos.

### Filtros Interativos

Os usuários podem personalizar a análise utilizando:

-Seleção de modelo do veículo.

-Faixa de ano de fabricação.

## 📊Visualizações
### Histograma

Permite analisar a distribuição da quilometragem dos veículos selecionados.

#### Pergunta respondida pelo gráfico:

Em quais faixas de quilometragem estão concentrados a maioria dos veículos?

### Gráfico de Dispersão

Permite analisar a relação entre quilometragem e preço.

#### Pergunta respondida pelo gráfico:

Como a quilometragem influencia o preço dos veículos?

Cada ponto representa um veículo individual.

## 📁 Estrutura do Projeto
Sprint-5-Project/

│

├── README.md

├── app.py

├── vehicles_us.csv

├── requirements.txt

│

├── notebooks/ 

│     └── EDA.ipynb

│ 

├── .streamlit/

│     └── config.toml 

│ 

└── .gitignore
