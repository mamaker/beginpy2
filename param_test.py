# -*- coding: utf-8 -*-
"""
param_test.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
def story(**kwds):
    print( 'Once upon a time, there was a ' \
'{job} called {name}.'.format_map(kwds))

story(job='king', name='Gumby')
print('-'*30)
story(name='Sir Robin', job='brave knight')
print('-'*30)
params = {'job': 'language', 'name': 'Python'}
story(**params)
print('-'*30)
del params['job']
story(job='stroke of genius', **params)
print('-'*30)

print('-'*30)
#%%

#%%
def add(x, y):
    return x + y

nums_tup = (1,2)
print(add(*nums_tup))
print('-'*30)
#%%


#%%
def hello_3(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))
    
greet_dic = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**greet_dic)
print('-'*30)
#%%

#%%
def with_stars(**kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

args_dic = {'name': 'Mr. Gumby', 'age': 42}

with_stars(**args_dic)
print('-'*30)
#with_stars(args_dic)
#print('-'*30)
#%%

#%%
def without_stars(kwds):
    print(kwds['name'], 'is', kwds['age'], 'years old')

args_dic = {'name': 'Mr. Gumby', 'age': 42}
without_stars(args_dic)
print('-'*30)
#without_stars(**args_dic)
#print('-'*30)
#%%


