import numpy as np
import scipy.optimize as optimization

def logistic_function(x, L, k, x0):
    return L/(np.exp(-k*(x-x0)))