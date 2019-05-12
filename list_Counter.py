# -*- coding: utf-8 -*-
"""
list_Counter.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


class CounterList(list):

    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)#%%


print('-'*30)
cl = CounterList(range(10))
print(cl)
print('-'*30)

cl.reverse()
print(cl)
print('-'*30)

del cl[3:6]
print(cl)
print('-'*30)

print(cl.counter)
print('-'*30)

cl[4] + cl[2]
print(cl.counter)
print('-'*30)


