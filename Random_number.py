from __future__ import print_function
import random


def adivina_cual(x):
    print("=====================")
    print(" ¿Listo para elegir? ")
    print("=====================")
    print("Tu meta es adivinar un numero aleatorio")
    random_number = random.randint(1,x)
    prediction = 0
    while prediction != random_number:
        prediction = int(input(f"Adivina un numero entre el 1 al {x}: "))

        if prediction < random_number:
            print("Intenta otra vez¡ Este numero es muy pequeño")
        elif prediction > random_number:
            print("Intenta otra vez¡ Este numero es muy grande")
    print("=============================================")        
    print(f"¡Felicidades, adivinaste! El número era el {random_number}.")
    print("=============================================") 


random_number_IA = random.randint(2,20)
adivina_cual(random_number_IA)
    

