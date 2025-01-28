import math

class Punto:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_punto):
        return math.sqrt(math.pow(otro_punto.x - self.x, 2) + math.pow(otro_punto.y - self.y, 2))

class CalculadoraDeDistancia:
    
    @staticmethod
    def calcular_distancia(punto1, punto2):
        return punto1.distancia(punto2)

    @staticmethod
    def obtener_coordenadas():
        x = float(input("Ingrese la coordenada x: "))
        y = float(input("Ingrese la coordenada y: "))
        return Punto(x, y)

if __name__ == "__main__":
    print("Ingrese las coordenadas del primer punto:")
    punto_a = CalculadoraDeDistancia.obtener_coordenadas()

    print("Ingrese las coordenadas del segundo punto:")
    punto_b = CalculadoraDeDistancia.obtener_coordenadas()
    
    distancia = CalculadoraDeDistancia.calcular_distancia(punto_a, punto_b)
    print(f"La distancia entre los puntos es: {distancia}")
