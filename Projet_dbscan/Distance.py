import numpy as np
def distance_euclidienne(p,q):
  V = np.array(p)-np.array(q)
  S = np.sqrt(np.sum(V*V))
  return S
