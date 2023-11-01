
Inicio = int(input("Inicio_tablas:"))
Final =int(input("Fina_tablas:"))

n1= Inicio 
n2 = Final 


m1= int(input("Donde Empieza a multiplicar:"))
m2 = int(input("Donde termina de multiplicar:"))



print("inicio de tabla:")


for j in range(n1 , n2 +1):  # Outer for/loop 
    print(f"Tabla: {j}")
    for k in range(m1, m2 +1):  # Inner for/loop (
        
        
        
        resultado = j * k  
     
        
        print(f"{j} x {k} = {resultado}")
        
        
        
print("Final De Tablas")
      
