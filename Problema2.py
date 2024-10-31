#"Un tanque de gas tiene una presión manométrica de 1.5×10⁶ Pa. 
# La presión atmosférica es 101,325 Pa. 
# Si por un problema técnico el gas pierde presión y 
# la manometría baja a 800,000 Pa8, 
# ¿cuál es la presión absoluta antes y después del incidente?"

from funsiones import *

Pman=int("Ingresa la presion manometrica")
Patm=int("Ingresa la presion atmosferica")
Pabs = PresionAbsoluta(Pman,Patm)
perdida=int ("Ingresa la perdida de presion manometrica")
Pman2=Pman-perdida
Pabs2=PresionAbsoluta(Pman2,Patm)
print(f"La presion antes es {Pabs} y la presion despues es {Pabs2}")