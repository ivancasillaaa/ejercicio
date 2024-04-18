import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv('data_animal_supporters_peru.csv')

# Configurar la página
st.set_page_config(page_title="Análisis de Apoyo a Animales en Perú")

# Crear los elementos de la aplicación
st.title("Análisis de Apoyo a Animales en Perú")
st.write("Esta aplicación muestra información sobre el apoyo a los animales en Perú.")

# Mostrar el dataset
st.subheader("Datos de Apoyo a Animales")
st.write(df)

# Gráfico de barras por tipo de animal
st.subheader("Apoyo por Tipo de Animal")
animal_counts = df['animal_type'].value_counts()
fig, ax = plt.subplots()
ax.bar(animal_counts.index, animal_counts.values)
ax.set_xlabel('Tipo de Animal')
ax.set_ylabel('Número de Apoyos')
st.pyplot(fig)

# Gráfico de dispersión por ubicación y donaciones
st.subheader("Donaciones por Ubicación")
fig, ax = plt.subplots()
ax.scatter(df['location'], df['donations'])
ax.set_xlabel('Ubicación')
ax.set_ylabel('Donaciones')
st.pyplot(fig)

# Resumen estadístico
st.subheader("Resumen Estadístico")
st.write(df.describe())