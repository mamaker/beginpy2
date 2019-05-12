# -*- coding: utf-8 -*-
"""
dict_misc.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

#%%
print(eval(input("Enter an arithmetic expression: ")))
print('-'*30)
#%%


#%%
from math import sqrt

scope = {'y':'anything'}
cmd =   'sqrt = 1             ;\
        x = "something"       ;\
        print("witin scope!")'
exec(cmd, scope)
print('sqrt(4):',sqrt(4))
print('len(scope):',len(scope))
print('scope.keys():',scope.keys())
print('-'*30)
#print('scope.values():',scope.values())
#print('-'*30)
#%%


#%%
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[8])
print('-'*30)
#%%

#%%
print('Matching first letters:')
boys = ['chris', 'arnold', 'bob']
girls = ['alice', 'bernice', 'clarice', 'betty', 'Zalima']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
print('-'*30)
#%%

#%%
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
print(list(zip(names, ages)))
print('-'*30)
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
print('-'*30)
#%%


#%%
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
print('-'*30)

for key in d.keys():
    print(key, 'corresponds to', d[key])
print('-'*30)

for value in d.values():
    print('value:', value)
print('-'*30)

for key,value in d.items():
    print(key, 'corresponds to', value)
print('-'*30)
#%%


#%%
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print("Cecil's phone number is {Cecil}.".format(**phonebook))
print('-'*30)
print("Cecil's phone number is {Cecil}.".format_map(phonebook))
print('-'*30)
#%%


#%%
template = '''
<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
#print(template.format_map(data))
print(template.format(**data))
print('-'*30)
#%%