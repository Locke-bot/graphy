# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:45:37 2021

@author: Unrated
"""
def GaussianElimination(nested_fractions):
    n = len(nested_fractions)
    aug_matrix = [None]*n # static typed as Fraction #declare an array to store the elements of augmented-matrix
    
    for i in range(n): # pivotization
        for k in range(i+1, n):
            if abs(nested_fractions[i][i])<abs(nested_fractions[k][i]):
                for j in range(0, n+1):
                    temp = nested_fractions[i][j] # static typed as Fraction
                    nested_fractions[i][j] = nested_fractions[k][j]
                    nested_fractions[k][j] = temp
    
    for i in range(n-1):            # loop to perform the gauss elimination
        inner_temp = nested_fractions[i][i]; # static fraction
        for k in range(i+1, n):
            temp = nested_fractions[k][i]/inner_temp#static fraction
            for j in range(n+1):
                nested_fractions[k][j] -= temp*nested_fractions[i][j] # make the elements below the pivot elements equal to zero or eliminate the variables
                
    # print('='*10)
    # print(nested_fractions)
    # print('='*10)
    
    for i in range(n-1, -1, -1): # back-substitution
        nf = nested_fractions[i][n]
        aug_matrix[i] = nf # make the variable to be calculated equal to the rhs of the last equation
        for j in range(i+1, n): 
            if j!=i: # then subtract all the lhs values except the coefficient of the variable whose value is being calculated
                aug_matrix[i] -= nested_fractions[i][j]*aug_matrix[j]
        aug_matrix[i] = aug_matrix[i]/nested_fractions[i][i] # now finally divide the rhs by the coefficient of the variable to be calculated
        
    return aug_matrix

if __name__ == '__main__':
    import sys, numpy as np
    from fractions import Fraction
    n = 100
    print('hare')
    def prepare_lists(x_array, y_array):
        for i in range(len(y_array)): # augmenting
            x_array[i].append(*y_array[i])
    #     for i in range(len(x)):
    #         for j in range(len(x[i])):
    #             x[i][j] = fractions.Fraction(str(x[i][j]))
    #     return x    
    x_array = np.random.uniform(-500, 500, [n, n])
    y_array = [[np.random.randint(-5000, 5000)] for i in range(n)]
    x_array = np.ndarray.tolist(x_array)
    prepare_lists(x_array, y_array)            
    thelist = np.array(x_array, dtype="object")
    for i in range(len(thelist)):
        for j in range(len(thelist[0])):
            thelist[i][j] = Fraction(thelist[i][j])    
    # print(thelist+Fraction())
    # print(thelist)
    # fc = GaussianElimination(x_array)