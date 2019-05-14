'''
test1.py
This and That
(c) Madhu Vasudevan
'''


#%%
print('-'*30)
a = {1, 2, 3}
b = {2, 3, 4}

print('a.union(b):',a.union(b), a | b)

print('a.intersection(b):', a.intersection(b), a & b)

c = a & b
print('c.issubset(a):', c.issubset(a))

c <= a

c.issuperset(a)
c >= a
print('-'*30)

#%%

#%%
my_sets = []
for i in range(10):
    my_sets.append(set(range(i, i+5)))

# reduce(set.union, my_sets)
#%%
    
