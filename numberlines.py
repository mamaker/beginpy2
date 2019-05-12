# -*- coding: utf-8 -*-                            #  1
"""                                                #  2
numberlines.py                                     #  3
Created on Fri Apr 26 20:38:57 2019                #  4
                                                   #  5
@author: madhu                                     #  6
"""                                                #  7
                                                   #  8
import fileinput                                   #  9
                                                   # 10
for line in fileinput.input(inplace=True):         # 11
    line = line.rstrip()                           # 12
    num = fileinput.lineno()                       # 13
    print('{:<50} # {:2d}'.format(line, num))      # 14
