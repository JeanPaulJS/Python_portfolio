

def concatenar(frase):
    frase = frase.lower()
    contador = 1
    while contador != 0 :
        contador = frase.find(" ")
        if contador != -1 :
            frase_agregada = frase[0 : contador]
            frase = frase[ contador +1 : len(frase)]
            frase_agregada = frase_agregada + frase
        else:
            print("!Gracias por jugar¡, mira las letras que solo usaste en tu frase: ")
            print(set(frase_agregada))
            contador = 0


print("========================================") 
print("¿Listo para jugar? ¡Piensa en una frase!")
print("========================================") 
frase = input("Ingresa una frase que tenga al menos dos palabras:\n")
concatenar(frase)







