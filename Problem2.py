"""
Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
"""

from functools import reduce 
def productexceptme(arr):
    prod = reduce((lambda x, y: x * y), arr)
    sol = []
    for elems in arr:
        sol.append(prod/elems)
    return sol
    
print (productexceptme([1, 2, 3, 4, 5]))
        
