print("HOLA MUNDO")
opcion= input("Ingrese la operacion aritmetica: ")
var1= float (input("Escribe el primer valor: "))
var2= float (input("Escribe el segundo valor: "))
0
if opcion== "suma":
    resultado_suma = var1 + var2
    print(resultado_suma)
if opcion== "resta":
    resultado_resta= var1 - var2
    print(resultado_resta)
if opcion == "multiplicacion":
    resultado_multiplicacion= var1 * var2
    print(resultado_multiplicacion)
if opcion == "division":
    if var1 % var2 == 0:
        resultado_division= var1 / var2
        print("igual: ", resultado_division)
print("añadiendo contenido para verificar una actualizacion en el repositorio")
print("mi tercer commit")
print(":D")