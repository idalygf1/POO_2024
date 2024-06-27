
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho

    
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return 0.5 * self.base * self.altura


