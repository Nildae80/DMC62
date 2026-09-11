import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Nilda Echevarria")

st.image("Python_logo.png",width = 200)
st.sidebar.image("DMC.png")


modulos = st.sidebar.selectbox("Seleccione el modulo",["Listas", "Arreglos", "Funciones", "POO"])

if modulos == "Listas":
  st.write("Te encuentras en el modulo de listas")
  
  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango", value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango", value=10))
  
  lista = list(range(valor_inicial, valor_final))
  st.write(lista)
  
elif modulos == "Arreglos":
  st.write("Bienvenidos al modulo de arreglos")
  
  cantidad = st.slider("Seleccione un valor del rango",min_value=1, max_value=100,value=20)
  arreglo = np.arange(cantidad)
  
  st.write(arreglo)

elif modulos == "Funciones":
  st.write("Bienvenidos al modulo de funciones")
  
  capital_i = st.number_input("Ingrese capital inicial", min_value = 0, max_value = 100000, value = 1000)
  aporte_m = st.number_input("Ingrese el aporte mensual", min_value = 0, max_value = 10000, value = 100)
  tasa_a = st.slider("Ingrese tasa anual", min_value = 0.01, max_value = 1.0, value = 0.05)
  anios = st.slider("Ingrese tiempo", min_value = 1, max_value = 20, value = 2)
  resultado_valor_futuro = lf.valor_futuro_inversion(capital_i,aporte_m,tasa_a,anios)
  st.write("El resultado de tu valor futuro de inversion es: ",resultado_valor_futuro)
  
else:
  st.write("Bienvenidos al modulo de POO")
