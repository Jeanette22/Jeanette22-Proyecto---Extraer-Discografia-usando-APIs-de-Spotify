#Palabra que sea igual del derecho al revés
menu= """

████████   ██████ ███         ██  █    █  ███    ██████     ████     ██      ██     ████
██     ██  █    █  █          ██  ██   █  █   █  █     █  ██     ██  ████  ████   ██     ██
██████     ██████  █          ██  █  █ █  █   █  ║████    ██     ██  ██  ██  ██   ██     ██
██         █    █  ║          ██  █   ██  █   █  █     █  ██     ██  ██      ██   ██     ██
██         █    █  ║███████   ██  █    █  ███    █      █   █████    ██      ██     █████

"""

def palindromo (palabra):
    palabra = palabra.replace (' ', '') #eliminamos espacios y se reemplaza para que tome palabras separadas
    palabra = palabra.lower ()         #se pasa la palabra en minusculas
    palabra_invertida = palabra [::-1] #se lee de atras de adelante
    if palabra == palabra_invertida:
        return True          
    else:
        return False


def run():
    print (menu)
    palabra = input ("escribe una palabra! 😊: ")
    es_palandrimo = palindromo (palabra)
    if es_palandrimo == True:
        print (" FELICIDADES! 😁es palindromo")
    else: 
        print ("Esta palabra no es palindromo 😫, sigue intentando!")


#es el punto de entrada de un programa de python, corre todo lo que esta debajo
if __name__ == '__main__':
    run () #invocamos a la funcion 


