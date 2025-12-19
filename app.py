# se crea un generador del tablero tradicional del busca minas
import random

def colorear(color,text):
    colors = dict(BLACK = '\033[30m',RED = '\033[31m',GREEN = '\033[32m',YELLOW = '\033[33m',BLUE = '\033[34m',MAGENTA = '\033[35m',CYAN = '\033[36m',WHITE = '\033[37m',AZUL_RARO = '\033[38;5;24m',RESET = '\033[0m')
    return f"{colors.get(color)}{text}{colors.get('RESET')}"

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
                linea.append(colorear("RED","X"))
            else:
                num = str(numMinasAlrededor([x,y],minas))
                match num :
                    case "1":
                        num = colorear("BLUE",num)
                    case "2":
                        num = colorear("GREEN",num)
                    case "3":
                        num = colorear("RED",num)
                    case "4":
                        num = colorear("MAGENTA",num)
                    case "5":
                        num = colorear("YELLOW",num)
                    case _:
                        num = colorear("WHITE",num)
                linea.append(num)
        tablero.append(linea)
    return tablero

def imprimirTablero(tablero):
    for linea in tablero:
        print(" ".join(linea))

def  crearMinas(dimensiones):
    minas = []
    #Se crean las cordenadas de la minas
    for i in range(0,num_minas):
        mina = [random.randint(0,dimensiones[0]-1),random.randint(0,dimensiones[1]-1)] # mina random del 1 al 99 pa este caso
        if mina not in minas: # Verificamos que la mina no se repita
            minas.append(mina)
        else: # Si la mina se repite le restamos uno al contador
            i -= 1
    return minas

dimensiones = [20,10]
num_minas = 30
tablero = []
minas = crearMinas(dimensiones)

imprimirTablero(crearTablero(dimensiones,minas))

