import pandas as pd

route = 'data.xlsx'  # ruta de acceso
df = pd.read_excel(io=route, header=None)
datos = df.iloc[:,1:11]
datos = datos.values.astype(float) #definimos en float los valores, por que inicialmente los toma como enteros o string
n = len(datos[0]) #length de la fila
m = len(datos) #length de la columna

def vol_cos (matriz,n,m):
    for i in range(n): #definir indice de sensibilidad
        matriz[2][i] = round(matriz[1][i]/matriz[0][i],1)
        matriz[3][i] = i+1

    print("\nindice de sensibilidad: VOLUMEN/COSTO\n")
    print("MATRIZ ORIGINAL\n") #imprimir matriz actual
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    matriz_ordenada = sorted(zip(matriz[2], *matriz), reverse=True) #ordenamos matriz segun el indice de sensibilidad, forma descendente
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ ORDENADA\n") #presentamos matriz ordenada
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()


    v=0
    c=0
    f=0
    while v<=26 and f<y: #calculamos valor de costo y volumen
        if (v+matriz[1][f])<=26:
            c=c+matriz[0][f]
            v=v+matriz[1][f]
            matriz[4][f]=1
        f+=1

    matriz_ordenada = sorted(zip(matriz[3], *matriz)) #ordeamos al original
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n")  #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def cos_vol (matriz,n,m):
    for i in range(n):
        matriz[2][i] = round(matriz[0][i]/matriz[1][i],1)
        matriz[3][i] = i+1

    print("\nindice de sensibilidad: COSTO/VOLUMEN\n")
    print("MATRIZ ORIGINAL\n") #presentamos matriz actual
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    matriz_ordenada = sorted(zip(matriz[2], *matriz), reverse=True) #ordenamos matriz segun el indice de sensibilidad
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ ORDENADA\n") #presentamos matriz ordenada
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    f=0
    while v<=26 and f<y:
        if (v+matriz[1][f])<=26: #calculamos valor de costo y volumen
            c=c+matriz[0][f]
            v=v+matriz[1][f]
            matriz[4][f]=1
        f+=1

    matriz_ordenada = sorted(zip(matriz[3], *matriz)) #ordeamos al original
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def cos (matriz,n,m):
    for i in range(n):
        matriz[2][i] = round(matriz[0][i],1)
        matriz[3][i] = i+1

    print("\nindice de sensibilidad: COSTO\n")
    print("MATRIZ ORIGINAL\n") #presentamos matriz actual
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    matriz_ordenada = sorted(zip(matriz[2], *matriz), reverse=True) #ordenamos matriz segun el indice de sensibilidad
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ ORDENADA\n") #presentamos matriz ordenada
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    f=0
    while v<=26 and f<y:
        if (v+matriz[1][f])<=26: #calculamos valor de costo y volumen
            c=c+matriz[0][f]
            v=v+matriz[1][f]
            matriz[4][f]=1
        f+=1

    matriz_ordenada = sorted(zip(matriz[3], *matriz)) #ordeamos al original
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def vol (matriz,n,m):
    for i in range(n):
        matriz[2][i] = round(matriz[1][i],1)
        matriz[3][i] = i+1

    print("\nindice de sensibilidad: VOLUMEN\n")
    print("MATRIZ ORIGINAL\n") #presentamos matriz actual
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    matriz_ordenada = sorted(zip(matriz[2], *matriz), reverse=True) #ordenamos matriz segun el indice de sensibilidad
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ ORDENADA\n") #presentamos matriz ordenada
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    f=0
    while v<=26 and f<y:
        if (v+matriz[1][f])<=26: #calculamos valor de costo y volumen
            c=c+matriz[0][f]
            v=v+matriz[1][f]
            matriz[4][f]=1
        f+=1

    matriz_ordenada = sorted(zip(matriz[3], *matriz)) #ordeamos al original
    matriz = [list(x) for x in zip(*matriz_ordenada)]
    del matriz[0] #eliminamos la fila 1, para que vuelva a su estado original

    print() 
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

matriz = datos #definimos el valores de la matriz
x=n #esto seria el valor de la fila
y=m #esto seria el valor de la columna 
cos(matriz,x,y)
vol(matriz,x,y)
cos_vol(matriz,x,y)
vol_cos(matriz,x,y)