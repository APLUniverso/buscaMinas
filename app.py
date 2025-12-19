# se crea un generador del tablero tradicional del busca minas
import random

def numMinasAlrededor(cordenada,minas):
    x = cordenada[0]
    y = cordenada[1]
    perimetroCordendas = [
        [x-1,y],# Cordenada de arriba
        [x+1,y],# Cordenada de abajo
        [x,y-1],# Cordenada de derecha
        [x,y+1],# Cordenada de izquierda
        # DIAGONALES
        [x-1,y+1],# Cordenada de arriba derecha
        [x-1,y-1],# Cordenada de arriba izquierda
        [x+1,y+1],# Cordenada de abajo derecha
        [x+1,y-1]# Cordenada de abajo izquierda
    ]
    num = 0
    for perimetro in perimetroCordendas:
        if perimetro in minas:
            num += 1
    return num

def crearTablero(dimensiones, minas):
    tablero = []
    for x in range(dimensiones[0]):
        linea = []
        for y in range(dimensiones[1]):
            if [x,y] in minas:
                linea.append("X")
            else:
                num = numMinasAlrededor([x,y],minas)
                linea.append(num)
        tablero.append(linea)
    return tablero

def imprimirTablero(tablero):
    for linea in tablero:
        print("".join(linea)+"\n")


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


imprimirTablero(crearTablero(dimensiones,minas))

