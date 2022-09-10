import math
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
def main():
   
   suma_vect([6,4], [-5,3], [4,-2])
   inverso_vect([-2,3])
   escalar(5, [7,-9])
   
main()
