
x=0
tem=""
while x<10:
    print(x)
    tem+=str(x)+"+"
    x=x+2

print(tem)

a=int(input("Captura el primer número: "))
b=int(input("Captura el segundo número: "))
salida=0 
contador=0  
suma = ""  
while contador <b:
    salida += a
    suma += f"{a} + " if contador < b - 1 else f"{a}"  
    contador += 1
print(f"La suma de {suma} es {salida}")


