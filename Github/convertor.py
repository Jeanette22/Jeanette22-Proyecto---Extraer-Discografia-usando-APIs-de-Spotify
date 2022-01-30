print ("*********covertor peso argentino a dolar*********")
pesos_argentina = input ("Ingrese la cantidad de dinero en pesos (valor): ")
pesos_argentina = float (pesos_argentina) #transformar en valor decimal 
dolar_hoy = 103
dolar_hoy= pesos_argentina /dolar_hoy
dolar_hoy = round (dolar_hoy, 2)
dolar_hoy = str (dolar_hoy)#para que se convierte en texto para mostrar en pantalla
print ("tienes USD" + dolar_hoy + "dolares")
print ("***************************************************")

