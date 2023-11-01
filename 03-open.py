from io import open

archivo = "INE.txt"

#Escritura
texto = "HOLA MUNDOOOO!"

archivo = open(archivo,"w")
archivo.write(texto)
archivo.close()

#Lectura
# archivo = open("archivos/hola-mundo.txt","r")
# texto= archivo.read()
# archivo.close
# print(texto)

#lectura como lista
# archivo = open("archivos/hola-mundo.txt","r")
# texto= archivo.readlines()
# archivo.close
# print(texto)

# with y seek
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# #agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("Chao, Mundo:c")
# archivo.close

# #lectura y escritura
# with open("hola-mundo.txt", "r+") as archivo:
#     texto=archivo.readlines()
#     archivo.seek(0)
#     texto[0] ="Chancho Feli"
#     archivo.writelines(texto)