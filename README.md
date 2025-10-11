#  Projet_dbscan

**Projet_dbscan** est une bibliothèque Python qui implémente l’algorithme **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**.  
Ce projet permet de regrouper des points de données en clusters sans utiliser de bibliothèque de machine learning comme scikit-learn.  

---

## Objectif

Le but de ce projet est d’apprendre à :

- Implémenter l’algorithme DBSCAN à partir de zéro (sans `scikit-learn`),

- Structurer une bibliothèque Python réutilisable

- Créer une librairie installable avec `pip`.

---

## Explication de chaque fichier

- **setup.py** : Ce fichier permet de transformer le dossier en bibliothèque Python installable. Il contient les informations nécessaires à pip pour installer le projet.

-  `__init__.py ` : C’est un fichier obligatoire pour que Python reconnaisse le dossier Projet_dbscan/ comme un package.

- **Distance.py** : Ce fichier contient la fonction de distance utilisée par DBSCAN.En général, c’est la distance euclidienne, qui mesure à quel point deux points sont proches.

- **Voisinage.py** : Ce fichier contient la fonction qui permet de trouver tous les points voisins d’un point donné. 

- **Etendre_cluster.py**: Ce fichier gère la fonction qui “étend” un cluster à partir d’un point cœur.

- **main_dbscan.py**: C’est le fichier principal de la librairie, celui qui contient la classe **mydbscan**. C’est cette classe que l’utilisateur importe et utilise directement. Fournit la méthode principale fit(X) pour traiter les données.

## Guide d'installation

 **- Préréquis** :
 Avant d’installer le projet, assurez-vous d’avoir :
   
   - Python 3.6 ou supérieur installé.
   
   - pip pour installer les packages Python. 

**- Cloner le dépôt**

```bash
git clone https://github.com/ProjetDbscan/DBSCAN.git
cd Projet_DBSCAN

```
## Exemple d’utilisation

```python
from Projet_dbscan import mydbscan
import numpy as np

# Jeu de données
X = np.array([
    [1.0, 1.0], [1.1, 1.1], [0.9, 1.2], [1.2, 0.9], [0.8, 1.0],
    [5.0, 5.0], [5.1, 4.9], [4.9, 5.2], [5.2, 5.1], [4.8, 5.0],
    [8.0, 1.0], [0.0, 5.0]
])

# Création du modèle
model = mydbscan(minpts=2, epsilon=2)
model.fit(X)

# Résultats
for i, cluster in enumerate(model.cluster, start=1):
    print(f"C{i} : {cluster}")
print("Bruits :", model.bruits)



