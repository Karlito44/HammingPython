import itertools
import numpy as np

def generate_matrix_h(n):
    matrix_identity = np.identity(n) # sert à générer la matrice I
    combinaisons = [list(i) for i in itertools.product([0, 1], repeat=n)] # créer toutes les combinaisons de 0/1 de taille n
    matrix_combinaisons = np.array(combinaisons) # permet de transformer la liste générée en matrice
    matrix_combinaisons = np.delete(([1,0,0],[0,1,0],[0,0,1])
    matrix_h = np.append(matrix_combinaisons, matrix_identity, axis=0) # fusion des deux matrices (conacténation)
    matrix_h = matrix_h.T
    matrix_h = np.delete(matrix_h, 0, axis=1)
    return matrix_h


def generate_matrix_g():
    matrix_h = generate_matrix_h()
    matrix_h = np.delete(matrix_h, [matrix_h])
    return "a"


if __name__ == "__main__":
    # execute only if run as a script
    print("Entrer la taille de la matrice H (n) :")
    n = input()
    print("Matrice H :")
    print(generate_matrix_h(int(n)))

