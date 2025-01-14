
texto1="Hola"
texto2="Mundo"

texto3Final=texto1+" "+texto2
print(texto3Final)
print("El saludo es: %s %s %(texto1,texto2)")

saludoFinal2="Saludo:{x} {y}".format(x=texto1,y=texto2)
print(saludoFinal2)

texto="desarrollo web profesional utl"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("all"))
print(texto.count("e"))

print(texto.replace("e","a"))

cadenaSeparada=texto.split(" ")
print(cadenaSeparada)



