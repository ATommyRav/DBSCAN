from .Voisinage import Voisinage
def etendre_cluster(X, groupes, P_indice, PtsVoisins, k, eps, m):
# X : c'est l'ensemble des points [X1,X2,...,Xn] avec X1 appartenant a R^d
#  groupes (list[int]) : pour identifier chaque point (si =0 : non visité, si =-1: bruit, si  >0 : cluster), cette marquage se fait dans main_dbscan.
# P_indice	:Indice du point P de départ du cluster
# PtsVoisins(list[int]):	Liste des indices des voisins proches de P 
# k : Numéro du cluster actuel
# eps : Rayon du voisinage
# m :	Nombre minimum de points pour être un point cœur 
    groupes[P_indice] = k # On marque le point de départ P comme appartenant au cluster numéro C (avec P un point coeur qui sera verifier dans main_dbscan)
    i = 0
    while i < len(PtsVoisins): #On traite les voisins de P
      Pv_indice = PtsVoisins[i]
      if groupes[Pv_indice] == 0: # Si le voisins de P est marqué non visité auparavant alors on le met dans le meme cluster que P 
         groupes[Pv_indice] = k
         PtsVoisinsP = Voisinage(X, X[Pv_indice], eps) #on cherche les voisins de voisin de P
         if len(PtsVoisinsP) >= m : #Si le  voisin de P  est un point coeur alors ses voisins s'ajoutent aussi au cluster 
            for v in PtsVoisinsP:
               if v not in PtsVoisins:
                  PtsVoisins.append(v) # len(Ptsvoisins) augmente 
      elif groupes[Pv_indice] == -1: #Si un point a ete considéré comme bruit dans main_dbscan mais qu’il est maintenant voisin d’un point cœur P  alors on le reintègre dans le même cluster que P
           groupes[Pv_indice] = k
      i+= 1 #on passe au voisin suivant 

 
