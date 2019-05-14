"""
test-sets.py
This and That
(c) Madhu Vasudevan 2019
"""


#%%
print('-'*30)
a = {1, 2, 3}
b = {2, 3, 4}
print('a:',a, 'b:',b)

print('a.union(b):',a.union(b), a | b)
print('a.intersection(b):', a.intersection(b), a & b)
print('a.difference(b):',a.difference(b),a - b)
print('a.symmetric_difference(b):',a.symmetric_difference(b), a ^ b)

c = a & b
print('-'*30)
print('a:',a, 'b:',b, 'c:',c)
print('c.issubset(a):', c.issubset(a), c <= a)
print('c.issuperset(a):',c.issuperset(a), c >= a)

print('-'*30)
print('a:',a, 'a.copy():',a.copy)
print('a.copy() is a:',a.copy() is a, a.copy == a)
print('-'*30)
x = a.copy
print('a:',a, 'a.copy():',x)
print('a.copy() is a:',a.copy() is x, a.copy == x)
print('-'*30)


#%%

#%%
my_sets = []
for i in range(10):
    my_sets.append(set(range(i, i+5)))

# reduce(set.union, my_sets)
print('-'*30)
#%%
    
