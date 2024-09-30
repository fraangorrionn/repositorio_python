#Hacer un pequeño tutorial en un Google Dosc de cada una de las funciones de debug con VsCode.
#Hacer el ejemplo con una un programa que tenga 4 funciones : sumar, restar, multiplicar y dividir.
#Explicar el panel dónde se ven las variable locales y globales.
n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "No se puede dividir entre cero."

print(str(n1) + " + " + str(n2) + " = " + str(sumar(n1, n2)))
print(str(n1) + " - " + str(n2) + " = " + str(restar(n1, n2)))
print(str(n1) + " * " + str(n2) + " = " + str(multiplicacion(n1, n2)))
print(str(n1) + " / " + str(n2) + " = " + str(division(n1, n2)))