#if
edad = 20

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")


#For con lista
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(f"El número es: {numero}")

#For con rango
for i in range(5):  # Genera valores de 0 a 4
    print(f"Iteración: {i}")

#While
contador = 0

while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1  # Incremento para evitar un bucle infinito