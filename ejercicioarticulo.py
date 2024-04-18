import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo para simular una encuesta
encuesta_data = {
    'Edad': [25, 30, 35, 40, 45],
    'Sexo': ['Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino'],
    'Apoyo_Animales': ['Sí', 'Sí', 'No', 'Sí', 'Sí']
}

# Crear DataFrame a partir de los datos de la encuesta
encuesta_df = pd.DataFrame(encuesta_data)

# Configurar la página
st.set_page_config(page_title="Encuesta sobre Apoyo a los Animales en Perú")

# Crear los elementos de la aplicación
st.title("Encuesta sobre Apoyo a los Animales en Perú")
st.write("Esta aplicación muestra los resultados de una encuesta sobre personas que apoyan a los animales en Perú.")

# Mostrar el dataset
st.subheader("Datos de la Encuesta")
st.write(encuesta_df)

# Gráfico de barras para la distribución del apoyo a los animales por sexo
st.subheader("Distribución del Apoyo a los Animales por Sexo")
fig, ax = plt.subplots()
sns.countplot(x='Sexo', hue='Apoyo_Animales', data=encuesta_df, ax=ax)
plt.xlabel('Sexo')
plt.ylabel('Cantidad')
plt.title('Distribución del Apoyo a los Animales por Sexo')
st.pyplot(fig)

# Resumen estadístico
st.subheader("Resumen Estadístico")
st.write(encuesta_df.describe())
