import plotly.express as px
import streamlit as st
import pandas as pd
import plotly_express as px

# Carga de dataset .csv
car_data = pd.read_csv(
    '/Users/irmalupita/proyecto_7/repo_vehicles/vehicles_us.csv')

print(car_data.head())

st.header('CarTrack comparative')

# Mostrar un encabezado
st.header("Filtrar marcas con menos de 50 días listados")

# Casilla de verificación para filtrar los datos
filtrar = st.checkbox("Mostrar marcas con menos de 50 días listados")

# Filtrar los datos si la casilla está marcada
if filtrar:
    filtered_data = car_data[car_data['days_listed'] < 50]
else:
    filtered_data = car_data

# Mostrar el dataframe en Streamlit
st.dataframe(filtered_data)


# BOTÓN HISTOGRAMA

# Cargar los datos
car_data = pd.read_csv(
    '/Users/irmalupita/proyecto_7/repo_vehicles/vehicles_us.csv')

# Filtrar solo pickups
car_data_pickup = car_data[car_data['type'] == 'pickup']

# Obtener lista de modelos únicos
modelos_disponibles = sorted(car_data_pickup['model'].unique())

# Crear selectbox para elegir modelos
modelo_1 = st.selectbox("Selecciona el primer modelo:",
                        modelos_disponibles, index=0)
modelo_2 = st.selectbox("Selecciona el segundo modelo:",
                        modelos_disponibles, index=1)

# Botón para construir el histograma

# Filtrar solo pickups
car_data_pickup = car_data[car_data['type'] == 'pickup']

# Obtener lista de modelos únicos
modelos_disponibles = sorted(car_data_pickup['model'].unique())

# Permitir seleccionar varios modelos
modelos_seleccionados = st.multiselect(
    "Selecciona los modelos a comparar:", modelos_disponibles, default=modelos_disponibles[:2])

# Botón para construir el histograma
if st.button('Mostrar histograma de precios'):
    if len(modelos_seleccionados) < 1:
        st.warning("Selecciona al menos un modelo.")
    else:
        # Filtrar los datos según los modelos seleccionados
        filtered_data = car_data_pickup[car_data_pickup['model'].isin(
            modelos_seleccionados)]

        # Crear el histograma con Plotly Express
        fig = px.histogram(
            filtered_data,
            x="price",
            color="model",
            barmode="overlay",
            title="Comparación de precios por modelo",
            labels={"price": "Precio", "model": "Modelo"}
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)

# Opcional: mostrar los primeros datos filtrados
st.write(car_data_pickup.head())
