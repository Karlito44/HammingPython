import itertools
import numpy as np
from random import *
import math

def generate_matrix_h(n):
    matrix_identity = np.identity(n) # sert à générer la matrice I
    combinaisons = [list(i) for i in itertools.product([0, 1], repeat=n)] # créer toutes les combinaisons de 0/1 de taille n
    matrix_combinaisons = np.array(combinaisons) # permet de transformer la liste générée en matrice
    matrix_combinaisons = np.append(matrix_combinaisons, matrix_identity, axis=0)
    # Permet d'obtenir un objet de type matrix pour ensuite poursuivre le traitement
    indexToRemove = []
    for i in range(len(matrix_combinaisons) - len(matrix_identity), len(matrix_combinaisons)):
        indexToRemove.append(i)
    matrix_combinaisons = np.delete(matrix_combinaisons, indexToRemove, axis=0)
    index = [0]
    # Retirer les doublons
    for i in range(0, len(matrix_combinaisons)):
        for y in range(0, len(matrix_identity)):
            if str(matrix_combinaisons[i]) == str(matrix_identity[y]):
                index.append(i)
    matrix_h = np.delete(matrix_combinaisons, index, axis=0)
    matrix_h = np.append(matrix_h, matrix_identity, axis=0) # fusion des deux matrices (concaténation)
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

def encode(mot, matrice): 
    # Part d'un mot de taille 2^l - l − 1 et l'encode pour donner un mot de taille 2^l − 1 
    listTemp = []
    # On récupère les lignes à additionner
    for i in range(0,len(mot)):
        if mot[i] == "1":
            listTemp.append(matrice[i])
    return additionner(listTemp)
    

def additionner(liste):
    # Additionne les lignes voulues de la matrice G 
    liste2 = []
    for j in range(0, len(liste[0])):
        valeur = 0
        for i in range(0, len(liste)):
            valeur+=(liste[i][j])
        liste2.append(int(valeur%2))
    #retourne le mot encodé
    return liste2

def bruitage(mot):
    # Altère un bit choisi au hasard dans un mot de longueur 2^l− 1 
    rand = randint(0, len(mot))
    # On parcours le mot et on s'arrête sur une position random
    for i in range (0, len(mot)):
        # On altère le bit à la position choisie aléatoirement (randint)
        if i == rand and mot[i] == 1:
            mot[i] = 0
        elif i == rand and mot[i] == 0:
            mot[i] = 1
    return mot

def correction(mot, matrice):
    # Corrige un mot de longueur 2^l− 1
    colonne = []
    placeErreur = []
    # On récupère d'abord les colonnes à additionner
    for i in range(0, len(mot)):
        if mot[i] == 1:
            colonne.append(i)
    # On additionnes les colonnes récupérées entres elles
    for k in range(0,len(matrice)):
        valeur = 0
        for j in colonne:
            valeur+=matrice[k][j]
        placeErreur.append(int(valeur%2))

    position = 0
    # On cherche la colonne correspondante dans H afin de connaître la position de l'erreur
    for l in range(0, len(matrice[0])):
        colonneH = []
        for m in range(0, len(matrice)):
            colonneH.append(int(matrice[m][l]%2))
        if colonneH == placeErreur:
            position = l + 1
    
    # On corrige donc l'erreur à la position trouvée précédemment
    for n in range(0, len(mot)):
        rang = n+1
        if rang == position :
            if mot[n] == 1:
                mot[n] = 0
            else:
                mot[n] = 1
    return mot

def hachage(mot, n, matrice):
    # découpe un mot donnée en sous mots de taille 2^l− 1
    taille = math.pow( 2, int(n) ) - 1
    hachage = []
    # On découpe le mot tant que sa taille n'est pas égale à zéro
    while len(mot) != 0:
        hachage.append(list(mot[:int(taille)]))
        mot = mot.replace(mot[:int(taille)], "")
    listeDecode = []
    # On appelle la fonction correction() pour corriger chaque mots
    for i in range(0, len(hachage)):
        for j in range(0, len(hachage[i])):
            hachage[i][j] = int(hachage[i][j])
        print()
        print(hachage[i])
        print("Résultat correction de ce mot: ", correction(hachage[i], matrice))
        print()
    return listeDecode


if __name__ == "__main__":
    # execute only if run as a script
    print("Entrer la taille de la matrice H (n) :")
    n = input()
    print("Matrice H :")
    matriceH = generate_matrix_h(int(n))
    print(matriceH)
    print("Matrice G :")
    matrice = generate_matrix_g(len(generate_matrix_h(int(n))))
    print(matrice)
    print("Choisissez un mot à encoder: ")
    mot = input()
    while True:
        if len(mot) != len(matrice):
            print("Ressaisissez (taille du mot = ",len(matrice),"): ")
            mot = input()
        else:
            break
    print("Mot après encodage: ")
    motEncode = encode(mot, matrice)
    print(motEncode)
    print()
    print("Mot après bruitage: ")
    motBruitage = bruitage(motEncode)
    print(motBruitage)
    print()
    print("Correction du mot: ")
    print(correction(motBruitage, matriceH))
    print()
    print("Hachage et correction du mot 1011101100011000110011111010001110000111011011111: ")
    print(hachage("1011101100011000110011111010001110000111011011111", n, matriceH))
    input('Press ENTER to exit')

