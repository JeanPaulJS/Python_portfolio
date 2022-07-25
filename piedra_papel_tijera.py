import random


def playgame():
    vidas = 3
    winers = 0
    while vidas != 0 and winers != 3:
        user = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, y 'ti' para tijera:\n").lower()
        computer = random.choice(['pi','pa','ti'])
        
        eleccion = tipo_de_eleccion(user, computer)

        if user == computer:
            print(f" !Empate¡ Ambos elegimos {eleccion[0]}. Aún tienes {vidas} vidas") 
        elif user_win(user, computer):
            winers = winers + 1
            print(f" !Ganaste¡ Yo perdí, elegí {eleccion[0]} y tu {eleccion[1]}. ¡Tienes {vidas} vidas con {winers} victorias!\n")
        else:
            vidas = vidas - 1
            print(f" !Perdiste¡ Yo elegí {eleccion[0]} y tu {eleccion[1]}. Te quedan {vidas} vidas :(")
    if vidas > 0 and winers == 3:
        print("============================================")
        frase = "Ganaste, ¡Felicidades y gracias por jugar!"
        return frase 
    print("============================================")
    frase = "Perdiste, pero animos, ¡intentalo de nuevo!"
    return frase   
    

def tipo_de_eleccion(user, computer):

    if computer == 'pa':
            eleccion = 'papel'
    elif computer == 'pi':
        eleccion = 'piedra'
    else: 
        eleccion = 'tijeras'
        
    if user == 'pi':
        elijio = 'piedra'
    elif user == 'pa':
        elijio = 'papel'
    else:
        elijio = 'tijeras'
    choose = [eleccion, elijio]
    return choose


def user_win(player, oponent):
    if ((player == 'pi' and oponent == 'ti' ) or (player == 'ti' and oponent == 'pa') or (player == 'pa ' and oponent == 'pi')):
        return True
    else:
        return False


print("=====================================")
print(" ¿Listo para jugar? Tienes tres vidas")
print("=====================================")
print(playgame())
print("============================================")

