import pandas as pd
import plotly.express as px
import streamlit as st
        
# Leer los datos
car_data = pd.read_csv(r'C:/Users/marc-/OneDrive/Escritorio/SPRINT6/vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir histograma') 
        
# Comprobar si el botón fue presionado
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # Mostrar un gráfico Plotly interactivo en Streamlit
    st.plotly_chart(fig, use_container_width=True)
