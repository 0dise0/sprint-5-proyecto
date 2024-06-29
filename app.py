# Importar librerias a utilizar
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Graficos realizados a partir de un dataset de anuncios de venta de coches') # Titulo de la aplicacion

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



scatter_boton = st.button('Construir grafico de dispersion') # Crea un boton

if scatter_boton: # al hacer clic en el boton, escribe un mensaje
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # Crea un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")

    # Muestra un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Opcional

st.header('Grafico opcional con casilla de verificacion')

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma con casillas de verificacion')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)
