import itertools
import numpy as np

def generate_matrix_h(n):
    matrix_identity = np.identity(n) # sert à générer la matrice I
    combinaisons = [list(i) for i in itertools.product([0, 1], repeat=n)] # créer toutes les combinaisons de 0/1 de taille n
    matrix_combinaisons = np.array(combinaisons) # permet de transformer la liste générée en matrice
    i = 0
    index = []
    # Retirer les doublons pour l = 3
    for value in matrix_combinaisons:
        if str(value) == "[0 0 0]" or str(value) == "[1 0 0]" or str(value) == "[0 1 0]" or str(value) == "[0 0 1]":
            index.append(i)
        i += 1
    matrix_h = np.delete(matrix_combinaisons, index, axis=0)
    matrix_h = np.append(matrix_h, matrix_identity, axis=0) # fusion des deux matrices (conacténation)
    matrix_h = matrix_h.T
    return matrix_h


def generate_matrix_g(size):
    matrix_h = generate_matrix_h(int(size))
    nb_col = matrix_h.size/size
    index = []
    # Stocker les index des colonnes à supprimer afin de retirer la matrice d'identité
    while True:
        index.append(int(nb_col-size))
        size -= 1
        if size == 0:
            break
    matrix_temp = np.delete(matrix_h.T, index, axis=0) # supprime la matrice I
    matrix_temp = matrix_temp.T # transposé de la matrice
    size_matrix_i = matrix_temp.size/len(matrix_temp)
    matrix_identity = np.identity(int(size_matrix_i))
    matrix_g = matrix_identity
    matrix_g = np.append(matrix_g, matrix_temp, axis=0) # construit la matrice G avec la transposé de matrix A
    matrix_g = matrix_g.T
    return matrix_g


if __name__ == "__main__":
    # execute only if run as a script
    print("Entrer la taille de la matrice H (n) :")
    n = input()
    print("Matrice H :")
    print(generate_matrix_h(int(n)))
    print("Matrice G :")
    print(generate_matrix_g(len(generate_matrix_h(int(n)))))

