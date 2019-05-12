# -*- coding: utf-8 -*-
"""
abs_class.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
print('-'*30)

class Knigget2(Talker):  # yet another abstract class!
    pass

print(issubclass(Knigget2, Talker))
print('-'*30)

class Knigget(Talker):
    def talk(self):
        print("Ni!")

k = Knigget()
print(isinstance(k, Talker))
k.talk()
print('-'*30)

class Herring:
    def talk(self):
        print("Blub.")

h = Herring()
print(isinstance(h, Talker))
print('-'*30)

Talker.register(Herring)
print(isinstance(h, Talker))
print(issubclass(Herring, Talker))
print('-'*30)


#%%
