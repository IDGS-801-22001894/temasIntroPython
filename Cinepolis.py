class CompraBoletos:
    def __init__(self, precioBoleto):
        self.precioBoleto = precioBoleto

    def ingresarDatos(self):
        self.nombreComprador = input("Escribe el nombre del comprador: ")
        numeroPersonas = int(input("¿Cuántas personas asistirán?: "))
        self.totalBoletos = int(input("¿Cuántos boletos vas a comprar?: "))

        while self.totalBoletos > 7 * numeroPersonas:
            print("\nNo es posible adquirir más de 7 boletos por persona.")
            print("1. Cambiar número de personas")
            print("2. Cambiar número de boletos")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                numeroPersonas = int(input("Introduce el nuevo número de personas: "))
            elif opcion == "2":
                self.totalBoletos = int(input("Introduce la nueva cantidad de boletos: "))
            else:
                print("Opción inválida. Inténtalo de nuevo.")

        print("\nSelecciona el método de pago:")
        print("1. Tarjeta CINECO")
        print("2. Efectivo")
        
        while True:
            opcionPago = input("Elige una opción (1 o 2): ")
            if opcionPago == "1":
                descuentoCineco = True
                break
            elif opcionPago == "2":
                descuentoCineco = False
                break
            else:
                print("Opción inválida. Inténtalo nuevamente.")
        
        self.totalPagar = self.calcularTotal(self.totalBoletos, self.precioBoleto, descuentoCineco)
        self.guardarCompra()

    def obtenerDescuento(self, cantidadBoletos):
        if cantidadBoletos >= 6:
            return 0.15
        elif 5 >= cantidadBoletos >= 3:
            return 0.10
        else:
            return 0.0

    def calcularTotal(self, cantidadBoletos, precioBoleto, descuentoCineco=False):
        subtotal = cantidadBoletos * precioBoleto
        descuento = self.obtenerDescuento(cantidadBoletos)
        total = subtotal * (1 - descuento)

        if descuentoCineco:
            total *= 0.90

        return total

    def guardarCompra(self):
        with open("compras.txt", "a") as archivo:
            archivo.write(f"{self.nombreComprador},{self.totalPagar}\n")

def mostrarCompras():
    with open("compras.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    total_ventas = 0
    print("\nCompras")
    print("{:<15} {:<10}".format("Nombre", "Total"))
    for linea in lineas:
        nombre, total = linea.strip().split(",")
        print("{:<15} {:<10}".format(nombre, format(float(total), "12,.0f").replace(",", ".")))
        total_ventas += float(total)
    
    print(f"\nTotal de ventas: {format(total_ventas, '12,.0f').replace(',', '.')}")

def main():
    precio_boleta = 12000
    
    with open("compras.txt", "w") as archivo:
        archivo.write("")
    
    while True:
        print("\nMenú Principal")
        print("1. Comprar boletos")
        print("2. Terminar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            compra = CompraBoletos(precioBoleto=precio_boleta)
            compra.ingresarDatos()
            print(f"Total a pagar: {format(compra.totalPagar, '12,.0f').replace(',', '.')}")
        elif opcion == "2":
            mostrarCompras()
            print("\nGracias!")
            break  
        else:
            print("Intente de nuevo.")

if __name__ == "__main__":
    main()