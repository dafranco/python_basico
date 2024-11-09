# Bienvenida
print("¡Bienvenido al Diagnóstico de Personalidad Virtual!")
print("Voy a hacerte algunas preguntas para conocerte mejor. 😊")
print("¡Responde sinceramente y al final te daré un pequeño diagnóstico!\n")

# Pregunta nombre
nombre = input("¿Cuál es tu nombre? ")

# Pregunta edad
edad = input("¿Cuántos años tienes, " + nombre + "? ")
try:
    edad = int(edad)
except ValueError:
    print("Hmm, parece que eso no es un número. Intentemos con otra cosa.")

# Pregunta color favorito
color = input("¿Cuál es tu color favorito? ")

# Pregunta si le gusta la pizza
le_gusta_pizza = input("¿Te gusta la pizza? (sí/no): ").strip().lower()

# Pregunta animal favorito
animal = input("¿Cuál es tu animal favorito? ")

# Resumen y diagnóstico
print("\n¡Gracias por responder, " + nombre + "! Aquí está tu diagnóstico:")

# Diagnóstico divertido basado en las respuestas
print("\n=== Diagnóstico de Personalidad Virtual ===")

# Análisis basado en el color favorito
if color.lower() == "azul":
    print("Eres una persona tranquila y reflexiva. ¡Como el color del cielo!")
elif color.lower() == "rojo":
    print("Tienes una personalidad apasionada y energética. ¡Cuidado, mundo!")
else:
    print(f"El {color} es un color único, ¡igual que tú!")

# Análisis basado en la preferencia por la pizza
if le_gusta_pizza == "sí":
    print("Veo que eres de buen gusto, ¡la pizza es deliciosa! 🍕")
elif le_gusta_pizza == "no":
    print("No te gusta la pizza... interesante, definitivamente tienes gustos únicos.")

# Análisis basado en el animal favorito
print(f"Ah, y como tu animal favorito es el {animal}, ¡se nota que tienes un espíritu {animal.lower()}!")

# Edad
if isinstance(edad, int):
    if edad < 18:
        print("Eres joven y lleno de energía. ¡El mundo está a tus pies!")
    elif 18 <= edad < 30:
        print("Estás en la flor de la vida. ¡Aprovecha cada momento!")
    elif 30 <= edad < 60:
        print("Con sabiduría y experiencia, tienes mucho que ofrecer al mundo.")
    else:
        print("Con tu experiencia, eres una persona sabia. ¡Todos deberían escuchar tus historias!")

print("\n=== Fin del Diagnóstico ===")
print("¡Gracias por participar, " + nombre + "! Espero que te haya sacado una sonrisa. 😊")
