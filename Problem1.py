"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

def printPairs(arr, arr_size, sum):       
    s = set()       
    for i in range(0,arr_size): 
        temp = sum-arr[i] 
        if (temp>=0 and temp in s): 
            print ("Pair ", arr[i], "and", temp) 
        s.add(arr[i])

printPairs([1,2,3,4,5],5,6)
