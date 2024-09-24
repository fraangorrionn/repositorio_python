prueba = ("hola clase DAW!!")
print(prueba)
edad = 25
if edad>=18:
    print("eres mayor de edad")
elif edad > 30:
    print("viejo chocho")
else:
    print("eres menor de edad")
    
anio = 2020
while anio <= 2024:
    print("informe del año", anio)
    anio+=1
print("fin while")

for i in range(6, 11):
    print(i)
print("fin for")

for i in range(0, 10):
    for j in range(0, 10):
        print("posicion"+str(i)+": "+str(j))
print("fin for doble")

lista = [1,7,8,9]
for x in lista:
    print("elemento de la lista: "+str(x))
print("fin for de lista")

lista = [1,7,8,9]
for x in lista:
    if(x%2 == 0):
        break
    else:
        print("elemento de la lista: "+str(x))
print("fin")