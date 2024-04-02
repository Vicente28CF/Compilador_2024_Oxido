#Team Koil
#Cayetano Flores Vicente
#Santillan Gonzalez Dante Adair
#Villegas Navarro Victor Alfredo
#07/03/2024

ERR = -1
ACP = 999
entrada = ''
idx = 0
bERR = False
ctelog = ['verdadero', 'falso']
palRes = ['fn', 'principal', 'imprimeln!', 'imprimeln', 'entero', 'const',
          'decimal', 'logico', 'alfabetico', 'sea', 'si', 'sino',
          'para', 'en', 'mientras', 'ciclo', 'regresa', 'leer', 'interrumpe',
          'continua','mut']

opa = ['+', '-', '*', '%','^']
dlm = ['[', ']', '{', '}', '(', ')', ',', ';', ':']
Sym = ['#','$','¿','!','?','~','`','@','¡','\\','|','&']



def colCar(c):
    if c.isalpha():     return 0
    if c == '_':        return 1
    if c == '.':        return 2
    if c.isdigit():     return 3
    if c in opa:        return 4
    if c == '&':        return 5
    if c == '!':        return 6
    if c == '=':        return 7
    if c == '"':        return 8
    if c == '/':        return 9
    if c in ['<', '>']: return 10
    if c == '|':        return 11
    if c in dlm:        return 12
    if c in Sym:        return 13
    if c in [' ', '\t', '\n']: return 0

    print(c, 'NO es valido en el alfabeto del Lenguaje')
    return ERR


matran = [
    #  0    1    2    3    4     5   6    7    8    9   10   11   12   13
    [  1,   1,  18,   2,   7,   8,  19,  14,  12,   5,  15,  10,  18,  21],  # 0
    [  1,   1, ACP,   1, ACP, ACP,   1, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 1
    [ACP, ACP,   3,   2, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 2
    [ERR, ERR, ERR,   4, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR],  # 3
    [ACP, ACP, ACP,   4, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 4
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,   6, ACP, ACP, ACP, ACP],  # 5
    [6  , 6  , 6  , 6  , 6  , 6  , 6  ,   6,   6,   6,   6,   6,   6,   6],  # 6
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 7
    [ERR, ERR, ERR, ERR, ERR,   9, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR],  # 8
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 9
    [ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR, ERR,  9,  ERR, ACP],  # 10
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 11
    [12 , 12 , 12 , 12 , 12 , 12 , 12 , 12 , 13 , 12 , 12 , 12 , 12 ,  12],  # 12
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 13
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP,  20, ACP, ACP, ACP, ACP, ACP, ACP],  # 14
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP,  16, ACP, ACP, ACP, ACP, ACP, ACP],  # 15
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 16
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 17
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 18
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP,  17, ACP, ACP, ACP, ACP, ACP, ACP],  # 19
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP],  # 20
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP]   # 21


]



#! Probando esta funcion para contar linea y columna. 
def erra(tipo, desc):
    global idx, entrada
    lineas = entrada.split('\n')
    linea_actual = 1
    columna_actual = 1
    posicion = 0
    tab_contador = 0  #! Contador de tabuladores
    for i, linea in enumerate(lineas):
        #! Reemplaza los tabuladores por espacios y ajusta el número de espacios según la regla especificada
        linea = linea.replace('\t', '    ' if tab_contador == 0 else '   ')
        posicion += len(linea) + 1  #! Suma la longitud de la línea y un carácter de nueva línea
        if posicion >= idx:  #! Si la posición actual es mayor o igual al índice del error
            if '.' in linea:
                columna_actual = linea.index('.') + 2  # Encuentra la posición del punto y suma 2 para contar después del punto
            else:
                columna_actual = idx - (posicion - len(linea))  # Si no hay punto, cuenta la columna normalmente
            break
        linea_actual += 1
        #! Actualiza el contador de tabuladores para la próxima línea
        tab_contador = 1 if '\t' in linea else 0
    print(tipo, desc, 'en la línea:', linea_actual, 'columna:', columna_actual)
    bERR = True


                

def lexico():
    global entrada, ERR, ACP, matran, idx
    estado = 0
    estAnt = 0
    lex = ''
    tok = ''
    while idx < len(entrada) and estado != ERR and estado != ACP:
        while (entrada[idx] in [' ', '\n', '\t', '']
               and estado == 0): idx += 1

        x = entrada[idx]
        idx += 1

        if estado == 6 and x == '\n': break
        if estado == 8 and x == '\n':
            estAnt = 8
            estado = ERR
            break
        if estado == 1 and x in [' ', '\t', '\n']:
            estAnt = estado
            estado = ACP
            break

        col = colCar(x)
        if col >= 0 and col <= 13 and estado != ERR:
            estAnt = estado
            estado = matran[estado][col]
            if estado != ACP and estado != ERR:
                lex += x

        if estado == ACP or estado == ERR:
            if estado == ACP: idx -= 1
            break

    # print(estAnt, estado)
    if estado != ACP and estado != ERR: estAnt = estado

    if estAnt == 3:
        erra('Error Lexico', 'cte Decimal en ' + lex)
    if estAnt == 12:
        erra('Error Lexico', 'cte Alfabetica SIN cerrar en ' + lex)
    if estAnt in [8,10]:
        tok = 'Sym'
        #erra('Error Lexico','OpL incompleto'+lex  )
    elif estAnt == 1:
        tok = 'Ide'
        if lex in palRes:
            tok = 'Res'
        elif lex in ctelog:
            tok = 'CtL'
    elif estAnt == 2:
        tok = 'Ent'
    elif estAnt == 4:
        tok = 'Dec'
    elif estAnt in [5,7]:
        tok = 'OpA'
    elif estAnt in [9, 19]:
        tok = 'OpL'
    elif estado == 6:
        tok = 'Com'
        lex = '//'
    elif estAnt == 13:
        tok = 'CtA'
    elif estAnt == 14:
        tok = 'OpS'
    elif estAnt in [15,16,17,20]:
        tok = 'OpR'
    elif estAnt == 17:
        tok = 'OpR'
    elif estAnt == 18:
        tok = 'Del'
    elif estAnt == 21:
        tok = 'Sym'


    else:
        tok = 'NtK'

    return tok, lex  # Termina lexico


def tokeniza():
    token = 'NtK'
    while (token in ['Com', 'NtK']):
        token, lexema = lexico()

    return token, lexema


if __name__ == '__main__':
    archE = ''
    print(archE[len(archE) - 3:])
    while (archE[len(archE) - 3:] != 'icc'):
        archE = input('Archivo a compilar (*.icc) [.]=Salir: ')
        if archE == '.': exit(0)
        aEnt = None
        try:
            aEnt = open(archE, 'r+',encoding='utf-8')
            break
        except FileNotFoundError:
            print(archE, 'No exite volver a intentar')

    if aEnt != None:
        while (linea := aEnt.readline()):
            entrada += linea
        aEnt.close()

    print('\n\n' + entrada + '\n\n')
    while idx < len(entrada):
        token, lexema = tokeniza()
        print(token, lexema)
