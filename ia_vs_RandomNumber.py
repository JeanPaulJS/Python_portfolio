import random 


def choose_computer(y):
    lim_min = 1
    lim_max = y

    answer = ""
    while answer != "c":
        if lim_min != lim_max:
            prediction = random.randint(lim_min, lim_max)
        else: 
            prediction = lim_max
        print(f"Creo que el numero es {prediction}.")    
        answer = input("Si mi numero es muy alto, escribe (A). Si es muy bajo, escribe (B). Si el numero es el correcto, escribe (C): ").lower()

        if answer == "a":
            lim_max = prediction - 1
        elif answer == "b": 
            lim_min = prediction + 1
    print("============================================================")
    print(f"He hallado tu numero, era el {prediction}. !Gracias por jugar¡")


print("======================================================")
print(" ¡Bienvenido(a) al juego! Tu numero vs nuestro codigo¡")
print("======================================================")
number = int(input("Selecciona un numero mayor a 1 para que el codigo intente averiguarlo: "))
choose_computer(number)
