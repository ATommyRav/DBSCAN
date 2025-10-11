from .Etendre_cluster import etendre_cluster
from .Distance import distance_euclidienne as distance
from .Voisinage import Voisinage
import numpy as np

try:#scipy est optionnel pour que le code puisse fonctionner meme sans scipy si la donnée n'est pas un sparse
    from scipy.sparse import issparse
except ImportError:
    # Définir une fonction pour éviter les erreurs avant la vérification
    def issparse(X):
        return False
        
def normaliser_data(X):
    """fonction qui converti les donnés entre en données compatibles avec notre aogorithme dbscn"""
    if issparse(X):#verifie si c'est un sparse
        X = X.toarray()
        
    else:
        try:
            if hasattr(X,"values"):
                X = np.asarray(X.values)
            else:
                X = np.array(X)
        except Exception as e:
            print("Erreur :", e)
            print("essayez d'installee scipy pour regler l'erreur")

    # S'assurer que X est bien de la forme liste de liste
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    return X
   

def dbscan(X, minpts, epsilon):
    """X: la donnée,
    minpts: nb de points minimum,
    epsilon: rayon des boules,
    la fonction dbscan retoune une liste groupe 
    qui à chaque groupe[i] associe l'indice du clusteur qui X[i]
    """
  
    """groupes est la liste de l'appartenance de chaque point à un cluster.
    Le i eme éléments de groupes correspond à l'indice du clusteur qui contient X[i] (si i>0),
    si groupes[i] = 0 alors le points est non visité,
    si groupe[i] = -1 le point a été visité.
    A la fin de l'algorithme groupes[i] != 0 pour tout i et
    les X[i] tel que groupes[i] = -1 sont considérés comme bruits"""
    groupes = [0]*len(X)
  
    k = 0 #initialisation de l'indice des clusteur 
  
    for i in range(len(X)):
        #PtsVoisins est l'ensemble des indices des points qui sont de le vosinage de X[i]
        PtsVoisins = Voisinage(X, X[i], epsilon)
        if groupes[i] == 0 :
            if len(PtsVoisins) >= minpts :
                k += 1 #on ajoute un indice de clusteur des qu'un points core n'est dans aucun clusteur(pas encore visité)
                etendre_cluster(X, groupes, i, PtsVoisins, k, epsilon, minpts)#cherche et donne le clusteur contenant X[i] en modifiant groupes
            elif len(PtsVoisins) < minpts :
                groupes[i] = -1 #si ce n'est pas un point core le point est juste marqué comme visité(temporairement un bruit)
                
    return groupes

class mydbscan:
    def __init__(self, minpts, epsilon):
        self.minpts = minpts
        self.epsilon = epsilon
        self.cluster = None
        self.bruits = None
        self.id_cluster = None
      
    #la donnéd X a été nommé Donnee pour moin de confusion.
    #methodes qui crée la liste crée modifie la liste des clusteur et bruits,elle ne retourne rien
    def fit(self,Donnee):  
        Donnee = normaliser_data(Donnee)
        indice_cluster = dbscan(Donnee,self.minpts,self.epsilon)
        self.id_cluster = indice_cluster
      
        #initialisation de la liste des clusteurs ayant pour taille l'indice maximal des clusteur
        max_indice = max(indice_cluster)
        if max_indice != -1 :
            self.cluster = [[] for _ in range(max(indice_cluster))]
        else :
            self.cluster = []
      
        #initialisation de la liste des bruits.
        self.bruits = []
      
        for i in range(len(Donnee)):
            if indice_cluster[i] > 0:
                #ajout de la ieme donnée au clusteur qui la contient(en regardant la valeur indice_clusteur[i]) si il existe
                ((self.cluster)[indice_cluster[i]-1]).append(Donnee[i]) # on fait indice_cluster[i]-1 car la liste commence par l'indice 0 or la incidice_clusteur n'a pas de valeur 0
              
            elif indice_cluster[i] == -1 :
                (self.bruits).append(Donnee[i]) #le point devient un bruit 
              
#exemple d'utilisation:
#projet = mydbscan(5,1)
#X = np.random.randn(50,3)
#projet.fit(X)
#print("les",len(projet.cluster),"clusteur sont")
#print(projet.cluster)                
#print("les bruits sont")
#print(projet.bruits)




















