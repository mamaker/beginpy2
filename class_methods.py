# -*- coding: utf-8 -*-
"""
class_methods.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


class MyClass:
    
    @staticmethod
    def smeth():
        print('This is a static method')
#    smeth = staticmethod(smeth)

    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)
#    cmeth = classmethod(cmeth)

print('-'*30)

MyClass.smeth()
print('-'*30)

MyClass.cmeth()
print('-'*30)
