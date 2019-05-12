# -*- coding: utf-8 -*-
"""
iter_fibo.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

#%%
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self


print('-'*30)
ti = TestIterator()
print(list(ti))
print('-'*30)


#%%

#%%
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self

print('-'*30)
fibs = Fibs()

for f in fibs:
    if f > 1000:
        print(f)
        break

print('-'*30)
#%%


#%%
it = iter([1, 2, 3])

print('next(it):')
print(next(it))
print('-'*30)
print(next(it))
print('-'*30)
print(next(it))
print('-'*30)

print('Alas:',next(it))
print('-'*30)

print('-'*30)
#%%
