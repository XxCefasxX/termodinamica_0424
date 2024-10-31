#"Un tanque de gas tiene una presión manométrica de 2×10⁵ Pa. La presión atmosférica es 101,325Pa. 
# El tanque está en contacto con una superficie cuya área es 0.5 m². 
# ¿Cuál es la presión absoluta dentro del tanque? 
# ¿Cuál es la fuerza total ejercida sobre la superficie? "

from presion import *

#Pedir datos
Pman= float( input("Ingresa la presion manometrica en Pascales"))
Patm= float( input("Ingresa la presion atmosferica en Pascales"))
Area= float(input("Ingresa el area "))

#llamr funciones
Pabs = PresionAbsoluta(Pman,Patm)
Ftotal=FuerzaTotal(Pabs,Area)

#Formatear decimales
F = round(Ftotal,2)
P = round(Pabs,2)

#Mostrar resultado
print(f"La presión absoluta es {P}Pa y la fuerza sobre la superficie es {F}N ")
