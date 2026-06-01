#Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

#Lendo os dados do arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Criando a interface do aplicativo

#Criando o cabeçalho da aplicação
st.header('Painel de análise de veículos')

#Adicionando três métricas importantes
col1, col2, col3 = st.columns(3)
col1.metric('Total de veículos', car_data.shape[0])
col2.metric('Preço Médio', f"${car_data['price'].mean():,.0f}")
col3.metric('Quilometragem Média', f"{car_data['odometer'].mean():,.0f}")

#Criando filtros
st.sidebar.header('Filtros')
modelo = st.sidebar.selectbox('Selecione o modelo', options=car_data['model'].unique())
ano = st.sidebar.slider('Selecione o ano', min_value=int(car_data['model_year'].min()), max_value=int(car_data['model_year'].max()), value=(int(car_data['model_year'].min()), int(car_data['model_year'].max())))

filtered_data = car_data[
    (car_data['model'] == modelo) &
    (car_data['model_year'] >= ano[0]) &
    (car_data['model_year'] <= ano[1])
]

#Criando duas checkbox para o usuário escolher se deseja criar um histograma ou num gráfico de dispersão
build_histogram = st.checkbox('Criar um histograma')

#Histograma será criado caso o usuário marque a checkbox
if build_histogram: 
    st.write('Criando um histograma para a faixa de quilometragem dos veículos:')
    fig = px.histogram(filtered_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

#Gráfico de dispesão será criado caso o usuário marque a checkbox
if build_scatter:
    st.write('Criando um gráfico de dispersão para a relação entre preço e quilometragem dos veículos:')
    fig = px.scatter(filtered_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

