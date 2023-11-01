from matematicas import divicion,multiplicacion,potencia,raiz,resta,suma

def Calculadora_Total():
    print("Bienvenido a la calculadora")
    print("Selecciona Una Opccion")
    respuesta = input("1.Suma,2.resta,3.multiplicacion,4.Divicion,5.Raiz,6.Potencia,7.salir")
    
    if respuesta.lower() == "1":
        suma.sum()
    elif respuesta.lower()=="2":
        resta.res()
    elif respuesta.lower()=="3":
        multiplicacion.multi
    elif respuesta.lower()=="4":
        divicion.divi()
    elif respuesta.lower()=="5":
        raiz.ra2()
    elif respuesta.lower()=="6":
        potencia.pot()
    elif respuesta.lower()=="7":
        return
  
    
Calculadora_Total()