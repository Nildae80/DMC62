import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Nilda Echevarria")

modulos = st.sidebar.selectbox("Seleccione el modulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de listas")
  
  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango", value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango", value=10))
  
  lista = list(range(valor_inicial, valor_final))
  st.write(lista)
  
elif modulos == "Arreglos":
  st.write("Bienvenidos al modulo de arreglos")

elif modulos == "Funciones":
  st.write("Bienvenidos al modulo de funciones")

else:
  st.write("Bienvenidos al modulo de POO")
