# -*- coding: utf-8 -*-
"""
beginpy_misc.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
z = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
print(reduce(lambda x, y: x + y, z))
print('Sum:', sum(z))
print('-'*30)
#%%


#%%
# Equivalent to [str(i) for i in range(10)]
seq = range(10)
x = list(map(str, seq)) 
print('list(map(str, range(10))):', x)
print('-'*30)
#%%

#%%
seq = ["foo", "x41", "?!", "***"]
x = filter(lambda x: x.isalnum(), seq)
#x = list(filter(lambda x: x.isalnum(), seq))
print('seq filtered through lambda function:', x)
print('-'*30)
#%%

#%%
for n in range(99, 0, -1):
    root = pow(n, 0.5)
    if root == int(root):
        print('Largest square below 100 is:',n)
        break
print('-'*30)
#%%

#%%
number = int(input('Enter a number between 1 and 10: '))
if 1 <= number <= 10:
    print('Great!')
else:
    print('Wrong!')
print('-'*30)
#%%

#%%
name = input('Please enter your name: ').strip() or '<unknown>'
print('Hi', name)
print('-'*30)

#%%

#%%
age = 10
assert 0 < age < 100
age = -1
assert 0 < age < 100, 'The age must be realistic'
#%%
    
