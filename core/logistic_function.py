import numpy as np

def logistic_function(x, L, k, x0):
    return L/(np.exp(-k*(x-x0)))