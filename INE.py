#Crear un programa que solicite todos los datos de la INE
#y que los almacene en un diccionario. Posteriormente y se guardarán en un archivo txt

from io import open



archivo = "INE.txt"


INE = {
    "Nombre": input("Ingresa tu nombre(s):"),
    "Apellidos": input("Ingresa tu Apellidos:"),
    "Curp": input("Ingresa tu Curp:"),
    "Edad": input("Ingresa tu Edad:"),
    "Domicilio": input("Ingresa tu Localidad:"),
    "Mes_Nacimiento": input("Mes De Nacimeinto:"),
    "Dia_N": input("Dia De Nacimiento:"),
    "Año_N": input("Año De Nacimiento:"),
    "Vigencia": input("Vigencia:"),
    "ClaveElectoral": input("Clave Electrola:"),
    "Año_Registro": input("Año De Registro:"),
    "Genero": input("Genero (H/M):")
}

with open(archivo, "w") as archivo_txt:
    for clave, valor in INE.items():
        archivo_txt.write(f"{clave}: {valor}\n")



