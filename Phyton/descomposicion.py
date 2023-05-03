import pandas as pd
import numpy as np

route = 'data.xlsx'  # ruta de acceso
df = pd.read_excel(io=route, header=None)
datos = df.iloc[:,1:11]
datos = datos.values.astype(float)


n = len(datos[0])
m = len(datos)

def costo (matriz,n,m):
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.33,0))
    len2 = int(round(n*0.33,0))
    len3 = n-(len1+len2)

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

    #formamos las 3 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    bag3 = [fila[len2+len1:] for fila in matriz]

    #mostramos en pantalla las 3 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 3\n") #presentamos matriz 3 ordenada
    i=0
    while i<m:
        for j in range(len3):
            print(bag3[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    cont=0
    while v<=26 and cont<len1:
        if (v+bag1[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag1[0][cont]
            v=v+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len2:
        if (v+bag2[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag2[0][cont]
            v=v+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len3:
        if (v+bag3[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag3[0][cont]
            v=v+bag3[1][cont]
            bag3[4][cont]=1
        cont+=1
    
    matrizN = np.concatenate((bag1, bag2, bag3), axis=1) #unimos las 3 matrices para que vuelva a la original

    matriz_ordenada = sorted(zip(matriz[3], *matrizN)) #ordeamos al original
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
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.33,0))
    len2 = int(round(n*0.33,0))
    len3 = n-(len1+len2)

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

    #formamos las 3 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    bag3 = [fila[len2+len1:] for fila in matriz]

    #mostramos en pantalla las 3 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 3\n") #presentamos matriz 3 ordenada
    i=0
    while i<m:
        for j in range(len3):
            print(bag3[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    cont=0
    while v<=26 and cont<len1:
        if (v+bag1[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag1[0][cont]
            v=v+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len2:
        if (v+bag2[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag2[0][cont]
            v=v+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len3:
        if (v+bag3[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag3[0][cont]
            v=v+bag3[1][cont]
            bag3[4][cont]=1
        cont+=1
    
    matrizN = np.concatenate((bag1, bag2, bag3), axis=1) #unimos las 3 matrices para que vuelva a la original

    matriz_ordenada = sorted(zip(matriz[3], *matrizN)) #ordeamos al original
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
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.33,0))
    len2 = int(round(n*0.33,0))
    len3 = n-(len1+len2)

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

    #formamos las 3 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    bag3 = [fila[len2+len1:] for fila in matriz]

    #mostramos en pantalla las 3 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 3\n") #presentamos matriz 3 ordenada
    i=0
    while i<m:
        for j in range(len3):
            print(bag3[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    cont=0
    while v<=26 and cont<len1:
        if (v+bag1[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag1[0][cont]
            v=v+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len2:
        if (v+bag2[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag2[0][cont]
            v=v+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len3:
        if (v+bag3[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag3[0][cont]
            v=v+bag3[1][cont]
            bag3[4][cont]=1
        cont+=1
    
    matrizN = np.concatenate((bag1, bag2, bag3), axis=1) #unimos las 3 matrices para que vuelva a la original

    matriz_ordenada = sorted(zip(matriz[3], *matrizN)) #ordeamos al original
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
    #definimos cada tamaño de la matriz
    len1 = int(round(n*0.33,0))
    len2 = int(round(n*0.33,0))
    len3 = n-(len1+len2)

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

    #formamos las 3 matrices
    bag1 = [fila[:len1] for fila in matriz]
    bag2 = [fila[len2:] for fila in matriz]
    bag3 = [fila[len2+len1:] for fila in matriz]

    #mostramos en pantalla las 3 matrices
    print()
    print("MATRIZ 1\n") #presentamos matriz 1 ordenada
    i=0
    while i<m:
        for j in range(len1):
            print(bag1[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 2\n") #presentamos matriz 2 ordenada
    i=0
    while i<m:
        for j in range(len2):
            print(bag2[i][j], end="  |  ")
        i+=1
        print()
    
    print()
    print("MATRIZ 3\n") #presentamos matriz 3 ordenada
    i=0
    while i<m:
        for j in range(len3):
            print(bag3[i][j], end="  |  ")
        i+=1
        print()

    v=0
    c=0
    cont=0
    while v<=26 and cont<len1:
        if (v+bag1[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag1[0][cont]
            v=v+bag1[1][cont]
            bag1[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len2:
        if (v+bag2[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag2[0][cont]
            v=v+bag2[1][cont]
            bag2[4][cont]=1
        cont+=1
    
    cont=0
    while v<=26 and cont<len3:
        if (v+bag3[1][cont])<=26: #calculamos valor de costo y volumen
            c=c+bag3[0][cont]
            v=v+bag3[1][cont]
            bag3[4][cont]=1
        cont+=1
    
    matrizN = np.concatenate((bag1, bag2, bag3), axis=1) #unimos las 3 matrices para que vuelva a la original

    matriz_ordenada = sorted(zip(matriz[3], *matrizN)) #ordeamos al original
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