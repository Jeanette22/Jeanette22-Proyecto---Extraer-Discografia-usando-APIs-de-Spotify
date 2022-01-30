#proyeo concto contrasena
import random 




def generar_contrasena():
    mayusculas = ['A', 'E', 'I', 'O', 'U']
    minusculas = ['G', 'J', 'R', 'R']
    simbolos = ['!', '#', '$', '*']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    caracteres  = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range (15):
        caracteres_random = random.choice (caracteres)
        contrasena.append (caracteres_random)

        contrasena = " ".join (contrasena) #USO DEL JOIN: PARA QUE DEVUELVA UNA CADENA DE TEXTO, STRING DE MI LISTA ORIGINAL 
        return contrasena      #TODOS LOS CARACTERES MEZCLADOS. Y GUARDAR EN ESA MISMA VARIABLE 

def run ():
    contrasena = generar_contrasena ()
    print ("tu nueva contrasena es:  "  + contrasena)


if __name__ == '__main__': 
    run ()


