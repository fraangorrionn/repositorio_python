## 20 Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el 
# salario anual del empleado. Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y 
# métodos específicos de cada tipo de empleado.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_anual(self):
        return self.salario * 12

class Gerente(Empleado):
    def __init__(self, nombre, salario, bonificacion):
        super().__init__(nombre, salario)
        self.bonificacion = bonificacion

    def calcular_salario_anual(self):
        return (self.salario + self.bonificacion) * 12

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

gerente = Gerente("Fran", 3000, 500)
programador = Programador("Ale", 2000, "Python")

print(f"Salario anual de {gerente.nombre}: {gerente.calcular_salario_anual()}")
print(f"Salario anual de {programador.nombre}: {programador.calcular_salario_anual()}")
