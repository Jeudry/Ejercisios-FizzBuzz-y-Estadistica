# Funciones
def min_max(numeros):
    if len(numeros) > 0:
        minim = numeros[0]
        max = numeros[0]

        for n in numeros:
            if n < minim:
                minim = n
            if n > max:
                max = n
        return f"Minimo: {minim}", f"Maximo: {max}"
    else:
        return None


def promedio(mat):
    return sum(mat) / len(mat)


def mediana(mat):
    mat.sort()
    tot_elm = len(mat)
    if tot_elm % 2 != 0:
        mediana = mat[tot_elm // 2]
    else:
        m1 = mat[tot_elm // 2]
        m2 = mat[tot_elm // 2 - 1]
        mediana = (m1 + m2) / 2
    return mediana


def moda(mat):
    conrep = 0
    maxim = 0
    tammat = len(mat)
    for val1 in range(tammat):
        conrep = 0
        for val2 in range(tammat):
            if mat[val1] == mat[val2]:
                conrep += 1
        if conrep > maxim:
            mayor = conrep
            moda = mat[val1]
    return moda


# Inicio
mat = [1, 4, 3, 4, 2]


# Salidas
print(f'Matrices: {mat} ')
print(min_max(mat))
print("Promedio: ", round(promedio(mat), 2))
print("Mediana: ", mediana(mat))
print("Moda: ", moda(mat))
print("Rango: ", len(mat))
