# -*- coding: utf-8 -*-
"""
generator1.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

print('-'*30)
r = repeater(42)
print(next(r))
print('-'*30)

print(next(r))
print('-'*30)

r.send("Hello, world!")
print(next(r))
print('-'*30)

print(next(r))
print('-'*30)
#%%


#%%
def a_generator(num):
    for i in range(num):
        yield i

print('-'*30)
x = a_generator(10)
print(next(x))
print('-'*30)
print(next(x))
print('-'*30)

print('-'*30)
for j in a_generator(5):
    print(j)

print('-'*30)
#%%


#%%
def flatten(nested):
    try:
        # Don't iterate over string-like objects:
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
print('-'*30)
nested = [[[1], 2], 3, 4, [5, [6, 7]], 8]

print('Begin Flettened Nested')
for num in flatten(nested):
    print(num, end=',')
print('\nEnd Flettened Nested')
print('-'*30)

print(list(flatten(nested)))
print('-'*30)

print('-'*30)
nested = ['foo', ['bar', ['baz']]]

print('Begin Flettened Nested')
for num in flatten(nested):
    print(num, end=',')
print('\nEnd Flettened Nested')
print('-'*30)

print(list(flatten(nested)))
print('-'*30)
#%%


#%%
def flatten2(nested):
    for sublist in nested:
        for element in sublist:
            yield element

print('-'*30)
nested = [[1, 2], [3, 4], [5]]

for num in flatten2(nested):
    print(num)

print('-'*30)

print(list(flatten2(nested)))
print('-'*30)
#%%

#%%
def flatten3(nested):
    result = []
    for sublist in nested:
        for element in sublist:
            result.append(element)
    return result

print('-'*30)
nested = [[1, 2], [3, 4], [5]]

print(flatten3(nested))

for num in flatten3(nested):
    print(num)

print('-'*30)

print(list(flatten3(nested)))
print('-'*30)
#%%



#%%
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print('-'*30)
print(next(g))
print('-'*30)
print(next(g))
print('-'*30)
#%%

#%%
print(sum(i ** 2 for i in range(10)))
print('-'*30)
#%%


