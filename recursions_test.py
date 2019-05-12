# -*- coding: utf-8 -*-
"""
recursions_test.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
print('-'*30)
#%%

#%%
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(3, 4))
print('-'*30)
#%%
    
#%%
def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

print(search(range(10), 5))
print('-'*30)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
print('-'*30)
print(search(seq, 67))
print('-'*30)#%%
