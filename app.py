import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Nilda Echevarria")

modulos = st.sidebar.selectbox("Seleccione el modulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de listas")
  
elif modulos == "Arreglos":
  st.write("Bienvenidos al modulo de arreglos")

elif modulos == "Funciones":
  st.write("Bienvenidos al modulo de funciones")

else:
  st.write("Bienvenidos al modulo de POO")
