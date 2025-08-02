import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el conjunto de datos
carros = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Panel de Análisis de Anuncios de Vehículos Usados")

# Botón para construir histograma
if st.button("Mostrar Histograma: Distribución de Precios en Anuncios de Vehículos Usados"):
    st.write("Distribución de Precios de Vehículos en los Anuncios")
    fig = px.histogram(carros, x="price", nbins=30,
                       title="Distribución de Precios")
    fig.update_layout(xaxis_title="Precio", yaxis_title="Cantidad")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión: Año del Modelo vs Precio"):
    st.write("Relación Entre el Año del Modelo y el Precio del Vehículo")
    carros_model_year = carros.dropna(subset=["model_year"])
    fig = px.scatter(carros_model_year, x="model_year",
                     y="price",
                     trendline="ols",
                     title="Año del Modelo vs Precio")
    fig.update_layout(xaxis_title="Año del Modelo", yaxis_title="Precio")
    st.plotly_chart(fig, use_container_width=True)

# Diagrama de Caja con casilla
if st.checkbox("Mostrar Diagrama de Caja de Precios por Tipo de Vehículo"):
    st.write(
        "Diagrama de Caja que Muestra la Distribución de Precios Según Tipo de Vehículo")
    carros_precio_filtrado = carros[carros["price"] < 100000]
    fig = px.box(carros_precio_filtrado, x="type", y="price",
                 title="Distribución de Precios por Tipo de Vehículo")
    fig.update_layout(xaxis_title="Tipo de Vehículo", yaxis_title="Precio")
    st.plotly_chart(fig, use_container_width=True)
