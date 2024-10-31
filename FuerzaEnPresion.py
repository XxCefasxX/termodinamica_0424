#Formulas
#1----- Pabs ​= Pman ​+ Patm​
#2----- Ftotal=P*A
#Requisitos
#Ftotal
#P
#A

#1 Pedir datos
Pman= float( input("Ingresa la presion manometrica en Pascales"))
Patm= float( input("Ingresa la presion atmosferica en Pascales"))
A= float(input("Ingresa el area "))
#2 APlicar formula
Pabs = Pman + Patm#calcula la Presion absoluta
Ftotal=Pabs*A #Calcula la furza total
#3 Formatear decimales
Fuerza = round(Ftotal,2)
Presion = round(Pabs,2)
#4 Mostrar resultado
print(f"La presión absoluta es {Presion}Pa y la fuerza sobre la superficie es {Fuerza}N ")
