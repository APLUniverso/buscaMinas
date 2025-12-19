# se crea un generador del tablero tradicional del busca minas
import random

def colorear(color,text): # Es la funcion que va a darle color a los numeros y las minas
    colors = dict(BLACK = '\033[30m',RED = '\033[31m',GREEN = '\033[32m',YELLOW = '\033[33m',BLUE = '\033[34m',MAGENTA = '\033[35m',CYAN = '\033[36m',WHITE = '\033[37m',AZUL_RARO = '\033[38;5;24m',RESET = '\033[0m')
    return f"{colors.get(color)}{text}{colors.get('RESET')}"

def numMinasAlrededor(cordenada,minas): # Esta funcion le da el numero a las casillas sin mina
    x = cordenada[0]
    y = cordenada[1]
    # perimetroCordendas = va a contener todas las 8 cordendas del perimetro
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
        if perimetro in minas:# Si hay una mina en el perimetro es contador crece
            num += 1
    return num

def crearTablero(dimensiones, minas): # Esta funcion es la que hace todo el tablero
    tablero = []
    for x in range(dimensiones[0]):
        linea = []
        for y in range(dimensiones[1]):
            if [x,y] in minas: # Si es esa cordenada hay una mina coloca una "X"
                linea.append(colorear("RED","X"))
            else: # Si no ponemos el numero de minas que hay alrededor
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

def imprimirTablero(tablero): # Esta funcion imprime el tablero
    for linea in tablero:
        print(" ".join(linea))

def  crearMinas(dimensiones): # Esta funcion crea las minas
    minas = []
    #Se crean las cordenadas de la minas
    for i in range(0,num_minas):
        mina = [random.randint(0,dimensiones[0]-1),random.randint(0,dimensiones[1]-1)] # mina random del 1 al 99 pa este caso
        if mina not in minas: # Verificamos que la mina no se repita
            minas.append(mina)
        else: # Si la mina se repite le restamos uno al contador
            i -= 1
    return minas

def espasiador(text,caracteres): # Esta funcion centra los textos
    espacios = int((caracteres - len(text))/2)
    return f"{' '*espacios}{text}{' '*espacios}"

dimensiones = [10,10]
num_minas = 10
tablero = []
minas = crearMinas(dimensiones)

print(espasiador("BUSCA MINAS",dimensiones[1]+dimensiones[1]-1))
imprimirTablero(crearTablero(dimensiones,minas))

