import math
def sum(complex_1, complex_2):
    add = (complex_1[0] + complex_2[0], complex_1[1] + complex_2[1])
    answer(add)
def product (complex_1, complex_2):
    prod = (complex_1[0]* complex_2[0] - complex_1[1]*complex_2[1], complex_1[1]*complex_2[0] + complex_1[0]* complex_2[1] )
    answer(prod)
def answer (result):
    if result[1] > 0:
        print (str(result[0]) + "+" + str(result[1])+ "i")
    else:
        print (str(result[0]) + str(result[1])+ "i")
def suma_vect(vector_1,vector_2,vector_3):
    suma = (vector_1[0] + vector_2[0] + vector_3[0], vector_1[1] + vector_2[1] + vector_3[1])
    answer(suma)
def inverso_vect(vector):
    for i in range (len(vector)):
        vector[i] = vector[i] * -1 
    answer(vector)
def escalar(multi,vector_1):
    multiplicar = multi * vector_1[0],  multi * vector_1[1]
    answer(multiplicar)
def suma_mat(matriz_1, matriz_2):
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1)):
            for m in range(len(matriz_2)):
                for n  in range(len(matriz_2)):
                    sumatoria = matriz_1[i] + matriz_2[m], matriz_1[j] + matriz_2[n]
    return sumatoria
def producto_matriz(m,n):
    if len(m) != len(n[0]):
        return "operación invalida"
    cadena = []
    contador = 0
    while contador < len(m[0]):
        cadena.append([])
        contador_2 = 0
        while contador_2 < len(n):
            contador_3 = 0
            suma = (0,0)
            while contador_3 < len(m):
                suma = sum(suma, product(m[contador_3,contador]), (n[contador_2,contador]))
                contador_3 += 1
            cadena[contador].append(suma)
            contador_2 += 1
        contador += 1
    return cadena
def llenar(vector):
    llenando = vector.split(" ")
    for i in range (len(llenando)):
        llenando[i] = tuple(llenando[i])
    return llenando
def generar_matriz(m):
    cadena = []
    for i in range(m):
        vector = "Ingrese un vector dejando espacio entre cada dato: "
        cadena.append(llenar(vector))
    return cadena
def clicks (matriz, vector, click):
    vector = [vector]
    contador = 0
    while contador < click:
        vector = producto_matriz(matriz,vector)
        contador += 1
    return vector[0]


