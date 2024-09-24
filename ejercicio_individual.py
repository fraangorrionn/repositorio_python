class rectangulo():
    def __init__(self, ancho=0, altura=0):
        self.ancho = ancho
        self.altura = altura

    def calcularArea(self):
        area = self.ancho * self.altura
        return area

rectangulo1 = rectangulo(20, 30)
print("ancho: " + str(rectangulo1.ancho) + " altura: " + str(rectangulo1.altura) + " area: " + str(rectangulo1.calcularArea()))