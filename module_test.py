# -*- coding: utf-8 -*-
"""
module_test.py
If you run this as a program, 
the hello function is executed; 
if you import it, it behaves like a normal module.
Created on Fri Apr 26 20:03:56 2019

@author: madhu
"""


def hello():
    print("Hello, world!")

def test():
    hello()

if __name__ == '__main__': test()
