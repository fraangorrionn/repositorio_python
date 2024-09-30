#1 Imprime "Hola, mundo!" en la pantalla.
print("hola mundo")

#2 Calcula la suma de dos números ingresados por el usuario. 
n1 = input("Introduce un número: ")
n2 = input("Introduce otro número: ")
suma = n1+n2
print("La suma de "+n1+" y "+n2+" es: "+suma)

#3 Calcula el área de un triángulo con la fórmula: Área = (base * altura) / 2.
base = int(input("Introduce la base: "))
altura = int(input("Introduce la altura: "))
area = base*altura/2
print("El área es: " + str(area))

#4 Convierte grados Celsius a Fahrenheit
celsius = int(input("Introduce los grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("celsius: "+str(celsius)+" fahrenheit: "+str(fahrenheit))

#5 Calcula el factorial de un número.
numero = int(input("Introduce un número para comprobar su factorial: "))

if numero < 0:
    print("no se pueden numeros negativos")
elif numero == 0 or numero == 1:
    resultado = 1
else:
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i

print("El factorial de "+str(numero)+" es: "+str(resultado))

#6 Verifica si un número es par o impar.
numero = int(input("Introduce un número: "))
if numero%2==0:
    print("el número es par")
else:
    print("el número es impar")
    
#7 Calcula el máximo común divisor (MCD) de dos números.
num1 = 48
num2 = 18

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("El máximo común divisor de "+str(num1)+" y "+str(num2)+" es "+str(num1))

#8 Imprime los números del 1 al 10 usando un bucle for.
for i in range(0,11):
    print(i)
    
#9 Calcula la suma de los números del 1 al 100. 
suma = 0
for i in range(0,101):
    suma+=i
print("suma: "+str(suma))

#10 Crea una lista de números y calcula su promedio.
lista = [1,7,8,9]
contador = 0
suma = 0
for i in lista:
    contador+=1
    suma +=i
promedio = suma/contador
print("el promedio es: "+str(promedio))

#11 Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.
class persona():
    def __init__(self,nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
        
persona1 = persona("Fran", 20)
persona2 = persona("Ale", 23)

print("nombre: " + persona1.nombre + " edad: " + str(persona1.edad))
print("nombre: " + persona2.nombre + " edad: " + str(persona2.edad))

#12 Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del 
#rectángulo y otro para calcular su perímetro.
class rectangulo():
    def __init__(self, ancho=0, altura=0):
        self.ancho = ancho
        self.altura = altura

    def calcularArea(self):
        area = self.ancho * self.altura
        return area

rectangulo1 = rectangulo(20, 30)
print("ancho: " + str(rectangulo1.ancho) + " altura: " + str(rectangulo1.altura) + " area: " + str(rectangulo1.calcularArea()))

##13 Crea una clase llamada Estudiante con atributos nombre, edad y curso. Crea varios objetos de tipo Estudiante y 
##almacénalos en una lista. Luego, itera sobre la lista e imprime la información de cada estudiante.  

class Estudiante:
    def __init__(self, nombre="", edad=0, curso=""):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

estudiante1 = Estudiante("Fran", 20, "2DAW")
estudiante2 = Estudiante("Ale", 22, "1DAW")
estudiante3 = Estudiante("Manolo", 30, "3ASIR")

lista_estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in lista_estudiantes:
    print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Curso: {estudiante.curso}")
    
##14 Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para depositar y retirar dinero de la cuenta.  

class CuentaBancaria:
    def __init__(self, titular="", saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        print(f"Deposito de {deposito} realizado. Nuevo saldo: {self.saldo}")
    
    def retirar(self, retiro):
        if retiro > self.saldo:
            print("Error: No hay suficiente saldo para realizar el retiro.")
        else:
            self.saldo -= retiro
            print(f"Retiro de {retiro} realizado. Nuevo saldo: {self.saldo}")

titular1 = CuentaBancaria("Fran", 200)
titular2 = CuentaBancaria("Ale", 220)

titular1.depositar(20)
titular1.retirar(100)
titular2.depositar(500)
titular2.retirar(40)

listaTitulares = [titular1, titular2]

for titulares in listaTitulares:
    print(f"Titular: {titulares.titular}, Saldo: {titulares.saldo}")
    
##15 Crea una clase llamada Coche con atributos marca y modelo. Crea un método que imprima la información del coche en un formato legible. 
class Coche:
    def __init__(self, marca = "", modelo = ""):
        self.marca = marca
        self.modelo = modelo
        
    def imprimir(self):
        print(f"Coche de marca: {self.marca}, modelo: {self.modelo}")
        
coche1 = Coche("Seat", "Toledo")
coche2 = Coche("Porsche", "Cayenne")

coche1.imprimir()
coche2.imprimir()

##16 Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. Luego, crea dos clases derivadas,
##Perro y Gato, que hereden de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 

class Animal:
    def hablar(self):
        print("mensaje generico.")

class Perro(Animal):
    def hablar(self):
        print("El perro hace: guau")

class Gato(Animal):
    def hablar(self):
        print("El gato hace: vamos no me jodas")

mi_perro = Perro()
mi_gato = Gato()

mi_perro.hablar()
mi_gato.hablar()

##17 Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura.
# Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método area para calcular
# el área específica de cada figura.

class FiguraGeometrica:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        print("el metodo area no se implementado en la clase base.")

class Rectangulo(FiguraGeometrica):
    def area(self):
        return self.ancho * self.altura

class Triangulo(FiguraGeometrica):
    def area(self):
        return (self.ancho * self.altura) / 2

rectangulo = Rectangulo(10, 20)
triangulo = Triangulo(10, 20)

print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Área del triángulo: {triangulo.area()}")

# 18 Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo.
# Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print(f"Vehículo de Marca: {self.marca}, Modelo: {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def informacion(self):
        super().informacion()
        print(f"Puertas: {self.puertas}")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def informacion(self):
        super().informacion()
        print(f"Tipo: {self.tipo}")

coche = Coche("Seat", "Ibiza", 4)
bicicleta = Bicicleta("Monty", "Escape 3", "Híbrida")

coche.informacion()
bicicleta.informacion()

##19 Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. Luego, 
##crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.
class InstrumentoMusical:
    
    def tocar(self):
        print("Este instrumento musical produce un sonido.")

class Piano(InstrumentoMusical):
    def tocar(self):
        print("(sonido de piano).")

class Guitarra(InstrumentoMusical):
    def tocar(self):
        print("(sonido de guitarra).")

piano = Piano()
guitarra = Guitarra()

piano.tocar()
guitarra.tocar() 

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