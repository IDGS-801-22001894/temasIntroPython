from io import open
import math

lectura = ""
texto = open("archivo.txt", "r")
lectura = texto.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print(i)
texto.close()
"""
se va almacenar el nombre y la cuenta, lo va a poner en forma de tabla. total de todas las ventas como si fuera un importe


cuando se da terminar el archivo se borra, osea se sobrescribe

menu, nombre de la persoa, num d epersonas, nume de boletos a comprar que te deje comprar mas  
3 x 21, todo dentro una clase
menu principal seguir comprando o terminar...
alli mismo en un archivo nuevo se llama cinepolis

"""