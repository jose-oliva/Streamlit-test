import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.header('Demostración de st.write en Streamlit')
st.write('¡Bienvenido a mi app de ejemplo! :wave:')
st.write(2025)

info_dict = {
    'Nombre': 'Jose Oliva',
    'Edad': 22,
    'Ciudad': 'Monterrey'
}
st.write('Ejemplo de diccionario:', info_dict)

ventas = pd.DataFrame({
    'Producto': ['Café', 'Té', 'Galletas', 'Pastel'],
    'Ventas': [120, 80, 150, 60],
    'Precio Unitario': [35, 30, 20, 50]
})
st.write('Tabla de ventas:', ventas)

st.write('A continuación se muestra el DataFrame de ventas:', ventas, '¡Arriba está la tabla!')
chart = alt.Chart(ventas).mark_bar().encode(
    x='Producto',
    y='Ventas',
    color='Producto',
    tooltip=['Producto', 'Ventas', 'Precio Unitario']
).properties(title='Ventas por producto')
st.write(chart)

random_df = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['col1', 'col2']
)
st.write('DataFrame de datos aleatorios:', random_df)