#Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

#Lendo os dados do arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Criando a interface do aplicativo

#Criando o cabeçalho da aplicação
st.header('Análise de dados de veículos')

#Criando duas checkbox para o usuário escolher se deseja criar um histograma ou num gráfico de dispersão
build_histogram = st.checkbox('Criar um histograma')

#Histograma será criado caso o usuário marque a checkbox
if build_histogram: 
  st.write('Criando um histograma para a coluna odometer')
  fig = px.histogram(car_data, x='odometer')
  st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

#Gráfico de dispesão será criado caso o usuário marque a checkbox
if build_scatter:
  st.write('Criando um gráfico de dispersão para as colunas odometer e price')
  fig = px.scatter(car_data, x="odometer", y="price")
  st.plotly_chart(fig, use_container_width=True)