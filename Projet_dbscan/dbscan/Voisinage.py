from distance import distance_euclidienne as distance
def Voisinage(X, point, epsilon):# X est l'ensemble des donnée, point est l'element dont on cherche la boule ouvret centrée en ce point, epsilon est e rayon de la boule
    boule = [] #initiation de la boule ouverte
    for y in X:
        if (distance(point,y)) < epsilon:
            boule.append(y) # ajoute a boule les element proche de points à un distance inferieur de epsilon
    return boule   #renvoie la boule ouverte centrée en pint
