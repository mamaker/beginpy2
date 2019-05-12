# -*- coding: utf-8 -*-
"""
property_rect.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

#%%
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self. __dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

print('-'*30)
r = Rectangle()
r.width = 10
r.height = 5

print(r.size)
print('-'*30)

r.size = (150, 100)
print(r.width)
print('-'*30)
#%%


#%%
class Rectangle2:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)

print('-'*30)
r = Rectangle2()
r.width = 10
r.height = 5

print(r.get_size())
print(r.size)
print('-'*30)

r.set_size((150, 100))
print(r.width)
r.size = (150, 100)
print(r.width)
print('-'*30)
#%%
