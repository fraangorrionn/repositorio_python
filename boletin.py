#1Imprime "Hola, mundo!" en la pantalla.
print("hola mundo")

#2Calcula la suma de dos números ingresados por el usuario. 
n1 = input("Introduce un número: ")
n2 = input("Introduce otro número: ")
suma = n1+n2
print("La suma de "+n1+" y "+n2+" es: "+suma)

#3Calcula el área de un triángulo con la fórmula: Área = (base * altura) / 2.
base = int(input("Introduce la base: "))
altura = int(input("Introduce la altura: "))
area = base*altura/2
print("El área es: " + str(area))

#4Convierte grados Celsius a Fahrenheit
celsius = int(input("Introduce los grados celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("celsius: "+str(celsius)+" fahrenheit: "+str(fahrenheit))

#5Calcula el factorial de un número.
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

#6Verifica si un número es par o impar.
numero = int(input("Introduce un número: "))
if numero%2==0:
    print("el número es par")
else:
    print("el número es impar")
    
#7Calcula el máximo común divisor (MCD) de dos números.
num1 = 48
num2 = 18

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("El máximo común divisor de "+str(num1)+" y "+str(num2)+" es "+str(num1))

#8Imprime los números del 1 al 10 usando un bucle for.
for i in range(0,11):
    print(i)
    
#9Calcula la suma de los números del 1 al 100. 
suma = 0
for i in range(0,101):
    suma+=i
print("suma: "+str(suma))

#10Crea una lista de números y calcula su promedio.
lista = [1,7,8,9]
contador = 0
suma = 0
for i in lista:
    contador+=1
    suma +=i
promedio = suma/contador
print("el promedio es: "+str(promedio))

#11Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.
class persona():
    def __init__(self,nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
        
persona1 = persona("Fran", 20)
persona2 = persona("Ale", 23)

print("nombre: " + persona1.nombre + " edad: " + str(persona1.edad))
print("nombre: " + persona2.nombre + " edad: " + str(persona2.edad))

#12Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del 
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