# -*- coding: utf-8 -*-
"""
queens8.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

print('-'*30)

print('queens(4) :',list(queens(4)))
print('-'*30)

sols = list(queens(8))
print('Num of queens(8) solutions:', len(sols))
for solution in sols:
    print(solution)
print('-'*30)

import random
prettyprint(random.choice(sols))




#%%


