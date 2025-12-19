# se crea un generador del tablero tradicional del busca minas
import random

dimensiones = [10,10]
num_minas = 10
tablero = []
minas = []

#Se crean las cordenadas de la minas
for i in range(0,10):
    mina = random.randint(0,(dimensiones[0]*dimensiones[1])-1) # mina random del 1 al 99 pa este caso
    if mina not in minas: # Verificamos que la mina no se repita
        if mina < 10: # si la mina es de un digito el x es 0
            minas.append([0,mina])
        else: # si no pues el primer digito es la X y el segundo es la Y
            minas.append([int(mina/10),mina-int(mina/10)*10])
    else: # Si la mina se repite le restamos uno al contador
        i -= 1
    


