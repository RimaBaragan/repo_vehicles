import plotly.express as px
import streamlit as st
import pandas as pd
import plotly_express as px

# Carga de dataset .csv
car_data = pd.read_csv(
    'vehicles_us.csv')


st.header('Compara-precios $$')

st.header('Utiliza el comparador de precios')

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


# Checkbox para mostrar dispersión
if st.checkbox("Construir gráfico de dispersión"):
    st.write(
        "Creación de un gráfico de dispersión para comparar precios de camionetas seleccionadas")

    car_data_filtrado = car_data[car_data["model"].isin(modelos_seleccionados)]

    fig_disp = px.scatter(car_data_filtrado, x="model_year", y="price", color="model",
                          title="Comparación de precios por año", opacity=0.7)

    st.plotly_chart(fig_disp)
