import numpy as np
from scipy.stats import kstest

def cdf(T):
    """Analytical CDF"""
    return (2 / np.pi) * np.arcsin(np.sqrt(T))

def ks_test(data):
    """
    Perform the Kolmogorov-Smirnov test for the given data against the analytical CDF.
    
    Parameters:
    - data: NumPy array of numerical data points.
    
    Returns:
    - D statistic: the K-S test statistic.
    - p-value: the p-value for the K-S test.
    """
    D_statistic, p_value = kstest(data, cdf)
    
    return D_statistic, p_value