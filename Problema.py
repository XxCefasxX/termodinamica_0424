#"Un cilindro pesa 5000 N y está apoyado en una superficie rectangular de dimensiones 1.5 m × 2m 
# Luego, se coloca una carga adicional de 2000 N sobre el cilindro. 
#Calcula la nueva presión ejercida sobre la superficie"
from presion import *

f1=int( input("Ingresa la fuerza 1: "))
f2=int( input("Ingresa la fuerza 2: "))
fuerza=f1+f2
area=1.5*2
P=Presion(fuerza,area)
print(f"La presion ejercida es {P}")
