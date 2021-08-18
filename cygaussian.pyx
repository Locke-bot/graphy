# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 05:29:26 2021

@author: Unrated
"""

def GaussianElimination(list nested_fractions):
    cdef int i, j, k, n
    # cdef float inner_temp, temp
    cdef list aug_matrix
    n = len(nested_fractions)
    aug_matrix = [None]*n # static typed as Fraction #declare an array to store the elements of augmented-matrix
    
    for i in range(n): # pivotization
        for k in range(i+1, n):
            if abs(nested_fractions[i][i])<abs(nested_fractions[k][i]):
                for j in range(0, n+1):
                    nested_fractions[i][j], nested_fractions[k][j] = nested_fractions[k][j], nested_fractions[i][j]
    
    for i in range(n-1):            # loop to perform the gauss elimination
        inner_temp = nested_fractions[i][i]; # static fraction
        for k in range(i+1, n):
            temp = nested_fractions[k][i]/inner_temp#static fraction
            for j in range(n+1):
                nested_fractions[k][j] -= temp*nested_fractions[i][j] # make the elements below the pivot elements equal to zero or eliminate the variables
                
    for i in range(n-1, -1, -1): # back-substitution
        aug_matrix[i] = nested_fractions[i][n] # make the variable to be calculated equal to the rhs of the last equation
        for j in range(i+1, n): 
            if j!=i: # then subtract all the lhs values except the coefficient of the variable whose value is being calculated
                aug_matrix[i] -= nested_fractions[i][j]*aug_matrix[j]
        aug_matrix[i] = aug_matrix[i]/nested_fractions[i][i] # now finally divide the rhs by the coefficient of the variable to be calculated
        
    return aug_matrix