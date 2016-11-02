import numpy as np
from scipy.optimize import curve_fit

def logistic_function(x, L, k, x0, y0):
    return L/(1+np.exp(-k*(x-x0)))+y0
    
def growth_curve_fit(xdata,ydata,params0,bounds):
    
    #fit the curve to the data
    popt, pcov = curve_fit(logistic_function,xdata,ydata,p0 = params0, bounds = bounds)
    
    #plot data versus fit
    
    
    
    #return fitted parameters
    return popt, pcov