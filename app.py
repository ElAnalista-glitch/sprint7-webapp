import streamlit as st
import pandas as pd
import plotly.express as px



# Encabezado de la aplicación
st.header("Exploración de Vehículos Usados")


# Leer archivo CSV
car_data = pd.read_csv('C:/Users/irvin/Desktop/Escritorio/Mochilero/certificadoDataAnalyst/sprint7-webapp/vehicles_us.csv')


# Mostrar una vista previa de los datos
st.write("Vista previa de los datos:")
st.write(car_data.head())

# Botón para crear histograma
if st.button("Mostrar histograma del odómetro"):
    st.write("Histograma de kilometraje (odómetro):")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)
    
 
# Botón para mostrar gráfico de dispersión
if st.button("Mostrar gráfico de dispersión (precio vs odómetro)"):
    st.write("Gráfico de dispersión entre precio y kilometraje:")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig_scatter)
    
    
# Casilla para mostrar histograma
if st.checkbox("Mostrar histograma del odómetro"):
    st.write("Histograma de kilometraje (odómetro):")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist)

# Casilla para mostrar gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión (precio vs odómetro)"):
    st.write("Gráfico de dispersión entre precio y kilometraje:")
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig_scatter)   