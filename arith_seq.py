# -*- coding: utf-8 -*-
"""
arith_seq.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


def check_index(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        Initialize the arithmetic sequence.
        start - the first value in the sequence
        step - the difference between two adjacent values
        changed - a dictionary of values that have been modified by
        the user
        """
        self.start = start # Store the start value
        self.step = step # Store the step value
        self.changed = {} # No items have been modified
    
    def __getitem__(self, key):
        """
        Get an item from the arithmetic sequence.
        """
        check_index(key)
        try: return self.changed[key] # Modified?
        except KeyError: # otherwise ...
            return self.start + key * self.step # ... calculate the value
    
    def __setitem__(self, key, value):
        """
        Change an item in the arithmetic sequence.
        """
        check_index(key)
        self.changed[key] = value # Store the changed value

s = ArithmeticSequence(1, 2)

#%%
print('s[4] :',s[4])

s[4] = 2
print('s[4] :',s[4])

print('s[5] :',s[5])
#%%

#%%
s["four"]
#%%

#%%
s[-42]
#%%


