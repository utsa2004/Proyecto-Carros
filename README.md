# 🚗 Proyecto-Carros : Aplicación Web para Anuncios de Venta de Carros Usados

# Panel de Análisis de Anuncios de Vehículos Usados 🚗📊

Este proyecto es una aplicación interactiva desarrollada con **Streamlit** que permite visualizar y analizar datos de anuncios de vehículos usados. Fue creado como parte del Sprint 7 del programa de formación en análisis de datos de TripleTen.

## 📌 Objetivos

- Explorar la distribución de precios en anuncios de vehículos usados.
- Visualizar la relación entre el año del modelo y el precio del automóvil.
- Analizar diferencias de precios según el tipo de vehículo.

## 📊 Funcionalidades del panel

- **Histograma:** Distribución de precios en anuncios de vehículos usados.
- **Gráfico de dispersión:** Comparación entre año del modelo con el precio del auto
- **Diagrama de caja:** Distribución de precios por tipo de vehículo.

## 🚀 Cómo ejecutar el proyecto

Puedes acceder a la app desplegada en Render aquí:  
🔗 [https://proyecto-oferta-carros-usados.onrender.com](https://proyecto-oferta-carros-usados.onrender.com)

### 🖥️ Para ejecutarlo localmente:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/utsa2004/Proyecto-Carros.git
   cd Proyecto-Carros
   ```

2. Crea un entorno virtual (opcional pero recomendado) y actívalo:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En macOS/Linux
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📁 Estructura del repositorio

```
Proyecto-Carros/
│
├── app.py               # Código principal de la app Streamlit
├── notebooks/           # Carpeta que contiene notebooks con análisis exploratorios
│   └── EDA.ipynb        # Notebook con el análisis exploratorio
├── requirements.txt     # Lista de librerías necesarias para el proyecto
├── vehicles_us.csv      # Conjunto de datos original utilizado en la aplicación
└── README.md            # Archivo de documentación con detalles del proyecto
```

## 📌 Tecnologías utilizadas

- Python 🐍  
- Pandas  
- Plotly-express  
- Streamlit  

## 👤 Autor

**Oscar Aranda**
📧 utsa2004@gmail.com

