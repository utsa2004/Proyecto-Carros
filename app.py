import pandas as pd
import plotly.express as px
import streamlit as st

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom, #a8d5ba, #f5f0e6);
        min-height: 100vh;
        padding: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Configuración inicial de la app
st.set_page_config(
    page_title="Análisis de Vehículos Usados",
    layout="wide",
    page_icon="🚗"
)

# Título principal
st.title("🚗 Panel de Análisis de Anuncios de Vehículos Usados")

# Intentar cargar el archivo CSV
try:
    carros = pd.read_csv("vehicles_us.csv")
except FileNotFoundError:
    st.error("❌ Error: El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en el directorio correcto.")
    st.stop()

# Verificar que las columnas necesarias existan
columnas_requeridas = ["odometer", "price", "model"]
columnas_faltantes = [
    col for col in columnas_requeridas if col not in carros.columns]

if columnas_faltantes:
    st.error(
        f"❌ Error: Faltan columnas necesarias en el archivo CSV: {', '.join(columnas_faltantes)}.")
    st.stop()

# Verificar si hay valores faltantes en las columnas clave
if carros[columnas_requeridas].isnull().any().any():
    st.warning(
        "⚠️ Advertencia: Se encontraron valores faltantes en las columnas clave (odometer, price, model).")

# Cargar los datos
carros = pd.read_csv("vehicles_us.csv")

# Limpieza y transformación de datos
carros["is_4wd"] = carros["is_4wd"].fillna(0).astype(int)
carros.rename(columns={"is_4wd": "traccion"}, inplace=True)

carros["model_year"] = carros["model_year"].astype("Int64")
carros["cylinders"] = carros["cylinders"].astype("Int64")
carros["odometer"] = carros["odometer"].astype("Int64")
carros["date_posted"] = pd.to_datetime(carros["date_posted"], dayfirst=True)

# 🧭 Barra lateral con filtros
st.sidebar.header("🔧 Filtros de Visualización")

precio_min, precio_max = int(carros["price"].min()), int(carros["price"].max())
precio = st.sidebar.slider("Precio (USD)", precio_min,
                           min(precio_max, 100000), (500, 40000))

año_opciones = carros["model_year"].dropna().sort_values().unique()
año = st.sidebar.select_slider("Año del modelo", options=año_opciones, value=(
    año_opciones.min(), año_opciones.max()))

tipos_vehiculo = carros["type"].dropna().unique()
tipo_seleccionado = st.sidebar.multiselect(
    "Tipo de vehículo", tipos_vehiculo, default=list(tipos_vehiculo))

traccion_opcion = st.sidebar.selectbox(
    "¿Tracción 4WD?", ["Todos", "Con tracción", "Sin tracción"])

# 🧼 Aplicar filtros
df_filtrado = carros[
    (carros["price"] >= precio[0]) & (carros["price"] <= precio[1]) &
    (carros["model_year"] >= año[0]) & (carros["model_year"] <= año[1]) &
    (carros["type"].isin(tipo_seleccionado))
]

if traccion_opcion != "Todos":
    valor = 1 if traccion_opcion == "Con tracción" else 0
    df_filtrado = df_filtrado[df_filtrado["traccion"] == valor]

# ✅ Histograma de precios
if st.checkbox("📊 Mostrar Histograma de Precios"):
    st.subheader("Distribución de Precios de Vehículos")
    fig = px.histogram(df_filtrado, x="price", nbins=30,
                       color_discrete_sequence=["#1f77b4"])
    fig.update_layout(xaxis_title="Precio (USD)",
                      yaxis_title="Cantidad de Anuncios")
    st.plotly_chart(fig, use_container_width=True)

# ✅ Gráfico de dispersión: Año vs Precio (altura aumentada)
if st.checkbox("📈 Mostrar Dispersión Año vs Precio"):
    st.subheader("Relación entre Año del Modelo y Precio")
    fig = px.scatter(df_filtrado.dropna(subset=["model_year"]),
                     x="model_year", y="price",
                     color_discrete_sequence=["#e377c2"]
                     )
    fig.update_layout(xaxis_title="Año del Modelo", yaxis_title="Precio (USD)")
    st.plotly_chart(fig, use_container_width=True)

# ✅ Gráfico de caja por tipo de vehículo
if st.checkbox("📦 Mostrar Boxplot de Precios por Tipo de Vehículo"):
    st.subheader("Distribución de Precios por Tipo de Vehículo")
    df_box = df_filtrado[df_filtrado["price"] < 100000]
    fig = px.box(df_box, x="type", y="price", color="type",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(xaxis_title="Tipo de Vehículo",
                      yaxis_title="Precio (USD)", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
