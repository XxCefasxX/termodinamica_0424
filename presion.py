#formula
#P=Ftotal/A
#P
#Ftotal
#A

#Pedir datos
Ft=int (input("Ingresa la fuerza total "))
A= int( input("Ingresa el area de la base "))

#APlicar formula
P=Ft/A
#formatear a 2 decimales
result =round(P,2)

#Validar si es mas de 1000 Pa
if(result>1000):
    #Convierte a Kilo Pascales
    print(f"La presion es: {result/1000}KPa")
else:
    #Muestra el resultado en pascales
    print(f"La presion es: {result}Pa")