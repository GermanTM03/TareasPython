#FBASICOS
def saludo():
    print("Hola Mundo")
    
#saludo()

#F Argumentos
def suma (arg1,arg2):
    suma = arg1 * arg2
    print(suma)
    
#suma(5,2)


def alumno(calificacion):
    
    if(calificacion >= 8):
        print("Aprobado")
    else:
        print("Reprobado")
        
alumno(8)