
#Este codigo tiene como finalidad mostrar el uso del f-string de python concatenando palabras a un texto de forma aleatorio dandole sentido de acuerdo a las palabras ingresadas por el usuario

adj1 = input("Ingrese un adjetivo: ")
adj2 = input("Ingrese un adjetivo: ")
sust1 = input("Ingrese un sustantivo (singular): ")
sust2 = input("Ingrese un sustantivo (plural): ")
verb1 = input("Ingrese un verbo: ")
verb2 = input("Ingrese un verbo: ")


madlib = f"Un lenguaje es un medio para expresar y registrar pensamientos. Hay muchos lenguajes a nuestro alrededor. Algunos de ellos no requieren {verb1} ni escribir, como el lenguaje corporal. Es posible {verb2} tus sentimientos más profundos de manera muy precisa sin decir una {sust1}. Otras {sust2} que empleas cada día es tu lengua materna, que utilizas para manifestar tu voluntad y para pensar en la realidad. Las computadoras son muy {adj1} y también tienen su propio lenguaje, llamado lenguaje máquina, el cual es muy {adj2}."

print("=====================")
print(madlib)
print("=====================")
