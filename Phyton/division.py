import pandas as pd
import numpy as np

route = "C:\Metodo de Division\data.xlsx"
df = pd.read_excel(io=route, header=None)
datos = df.iloc[:,1:11]
datos = datos.values.astype(float)

n = len(datos[0])
m = len(datos)

def costo (matriz,n,m):
    v=26
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.50,0))
    len2 = int(n-len1)

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
    
    #formamos las 2 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    
    #mostramos en pantalla las 2 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    #ordenamos las 2 matrices segun el indice de sensibilidad
    bag1_ordenada = sorted(zip(bag1[2], *bag1), reverse=True) #ordenamos matriz 1
    bag1 = [list(x) for x in zip(*bag1_ordenada)]
    del bag1[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    bag2_ordenada = sorted(zip(bag2[2], *bag2), reverse=True) #ordenamos matriz 2
    bag2 = [list(x) for x in zip(*bag2_ordenada)]
    del bag2[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ 1 ORDENADA\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()

    print()
    print("MATRIZ 2 ORDENADA\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()

    v1 = 0
    v2 = 0
    c1 = 0
    c2 = 0
    cont=0
    #cabe resaltar que el 13 en cada while, es la division del volumen total, entre las dos matrices
    while v1<=13 and cont<len1: #calculamos volumen de la matriz 1
        if (v1+bag1[1][cont])<=13: #calculamos valor de costo y volumen
            c1=c1+bag1[0][cont]
            v1=v1+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v2<=13 and cont<len2: #calculamos volumen de la matriz 2
        if (v2+bag2[1][cont])<=13: #calculamos valor de costo y volumen
            c2=c2+bag2[0][cont]
            v2=v2+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    #sumamos costo y volumen de ambas matrices
    c=c1+c2
    v=v1+v2
    matrizN = np.concatenate((bag1, bag2), axis=1) #unimos las 2 matrices para que vuelva a la original
    matriz_ordenada = sorted(zip(matrizN[3], *matrizN)) #ordeamos al original
    matrizN = [list(x) for x in zip(*matriz_ordenada)]
    del matrizN[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matrizN[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def volumen (matriz,n,m):
    v=26
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.50,0))
    len2 = int(n-len1)

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
    
    #formamos las 2 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    
    #mostramos en pantalla las 2 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    #ordenamos las 2 matrices segun el indice de sensibilidad
    bag1_ordenada = sorted(zip(bag1[2], *bag1), reverse=True) #ordenamos matriz 1
    bag1 = [list(x) for x in zip(*bag1_ordenada)]
    del bag1[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    bag2_ordenada = sorted(zip(bag2[2], *bag2), reverse=True) #ordenamos matriz 2
    bag2 = [list(x) for x in zip(*bag2_ordenada)]
    del bag2[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ 1 ORDENADA\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()

    print()
    print("MATRIZ 2 ORDENADA\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()

    v1 = 0
    v2 = 0
    c1 = 0
    c2 = 0
    cont=0
    #cabe resaltar que el 13 en cada while, es la division del volumen total, entre las dos matrices
    while v1<=13 and cont<len1: #calculamos volumen de la matriz 1
        if (v1+bag1[1][cont])<=13: #calculamos valor de costo y volumen
            c1=c1+bag1[0][cont]
            v1=v1+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v2<=13 and cont<len2: #calculamos volumen de la matriz 2
        if (v2+bag2[1][cont])<=13: #calculamos valor de costo y volumen
            c2=c2+bag2[0][cont]
            v2=v2+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    #sumamos costo y volumen de ambas matrices
    c=c1+c2
    v=v1+v2
    matrizN = np.concatenate((bag1, bag2), axis=1) #unimos las 2 matrices para que vuelva a la original
    matriz_ordenada = sorted(zip(matrizN[3], *matrizN)) #ordeamos al original
    matrizN = [list(x) for x in zip(*matriz_ordenada)]
    del matrizN[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matrizN[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def volumen_costo (matriz,n,m):
    v=26
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.50,0))
    len2 = int(n-len1)

    for i in range(n):
        matriz[2][i] = round(matriz[1][i]/matriz[0][i],1)
        matriz[3][i] = i+1

    print("\nindice de sensibilidad: VOLUMEN/COSTO\n")
    print("MATRIZ ORIGINAL\n") #presentamos matriz actual
    i=0
    while i<m:
        for j in range(n):
            print(matriz[i][j], end="  |  ")
        i+=1
        print()
    
    #formamos las 2 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    
    #mostramos en pantalla las 2 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    #ordenamos las 2 matrices segun el indice de sensibilidad
    bag1_ordenada = sorted(zip(bag1[2], *bag1), reverse=True) #ordenamos matriz 1
    bag1 = [list(x) for x in zip(*bag1_ordenada)]
    del bag1[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    bag2_ordenada = sorted(zip(bag2[2], *bag2), reverse=True) #ordenamos matriz 2
    bag2 = [list(x) for x in zip(*bag2_ordenada)]
    del bag2[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ 1 ORDENADA\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()

    print()
    print("MATRIZ 2 ORDENADA\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()

    v1 = 0
    v2 = 0
    c1 = 0
    c2 = 0
    cont=0
    #cabe resaltar que el 13 en cada while, es la division del volumen total, entre las dos matrices
    while v1<=13 and cont<len1: #calculamos volumen de la matriz 1
        if (v1+bag1[1][cont])<=13: #calculamos valor de costo y volumen
            c1=c1+bag1[0][cont]
            v1=v1+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v2<=13 and cont<len2: #calculamos volumen de la matriz 2
        if (v2+bag2[1][cont])<=13: #calculamos valor de costo y volumen
            c2=c2+bag2[0][cont]
            v2=v2+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    #sumamos costo y volumen de ambas matrices
    c=c1+c2
    v=v1+v2
    matrizN = np.concatenate((bag1, bag2), axis=1) #unimos las 2 matrices para que vuelva a la original
    matriz_ordenada = sorted(zip(matrizN[3], *matrizN)) #ordeamos al original
    matrizN = [list(x) for x in zip(*matriz_ordenada)]
    del matrizN[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matrizN[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

def costo_volumen (matriz,n,m):
    v=26
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.50,0))
    len2 = int(n-len1)

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
    
    #formamos las 2 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    
    #mostramos en pantalla las 2 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    #ordenamos las 2 matrices segun el indice de sensibilidad
    bag1_ordenada = sorted(zip(bag1[2], *bag1), reverse=True) #ordenamos matriz 1
    bag1 = [list(x) for x in zip(*bag1_ordenada)]
    del bag1[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    bag2_ordenada = sorted(zip(bag2[2], *bag2), reverse=True) #ordenamos matriz 2
    bag2 = [list(x) for x in zip(*bag2_ordenada)]
    del bag2[0] #eliminamos la fila 1, para que vuelva a su estado original, pero ordenado

    print()
    print("MATRIZ 1 ORDENADA\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()

    print()
    print("MATRIZ 2 ORDENADA\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()

    v1 = 0
    v2 = 0
    c1 = 0
    c2 = 0
    cont=0
    #cabe resaltar que el 13 en cada while, es la division del volumen total, entre las dos matrices
    while v1<=13 and cont<len1: #calculamos volumen de la matriz 1
        if (v1+bag1[1][cont])<=13: #calculamos valor de costo y volumen
            c1=c1+bag1[0][cont]
            v1=v1+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v2<=13 and cont<len2: #calculamos volumen de la matriz 2
        if (v2+bag2[1][cont])<=13: #calculamos valor de costo y volumen
            c2=c2+bag2[0][cont]
            v2=v2+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    #sumamos costo y volumen de ambas matrices
    c=c1+c2
    v=v1+v2
    matrizN = np.concatenate((bag1, bag2), axis=1) #unimos las 2 matrices para que vuelva a la original
    matriz_ordenada = sorted(zip(matrizN[3], *matrizN)) #ordeamos al original
    matrizN = [list(x) for x in zip(*matriz_ordenada)]
    del matrizN[0] #eliminamos la fila 1, para que vuelva a su estado original

    print()
    print("MATRIZ FINAL\n") #matriz final
    i=0
    while i<m:
        for j in range(n):
            print(matrizN[i][j], end="  |  ")
        i+=1
        print()

    print(f"Costo: {c}\nVolumen: {v}")

matriz = datos
x=n
y=m
costo(matriz,x,y)
volumen(matriz,x,y)
costo_volumen(matriz,x,y)
volumen_costo(matriz,x,y)