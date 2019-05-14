# -*- coding: utf-8 -*-
"""
wc-script.py
This and That
(c) Madhu Vasudevan 2019
"""

import pprint

def process(string):
    print('Processing:', string)

def main():

#%%
    print('-'*30)

    f = open('simplefile.txt')
    print(f.read(7))
    print(f.read(4))
    f.close()

#%%
    print('-'*30)

    f = open('simplefile.txt')
    print(f.read())
    f.close()

#%%
    print('-'*30)

    f = open('simplefile.txt')
    for i in range(3):
            print(str(i) + ': ' + f.readline(), end='')
    f.close()

#%%
    print('-'*30)

    f = open('simplefile.txt')
    i = 0
    nextline = f.readline()
    while nextline :
            print(str(i) + ': ' + nextline, end='')
            nextline = f.readline()
            i += 1
    f.close()

#%%
    print('-'*30)
    
    with open('simplefile.txt') as f:
        char = f.read(1)
        while char:
            process(char)
            char = f.read(1)

#%%
    print('-'*30)
    
    with open('simplefile.txt') as f:
        for char in f.read():
            process(char)

#%%
    print('-'*30)
    
    with open('simplefile.txt') as f:
        for line in f.readlines():
            process(line)

#%%
    print('-'*30)
    
    with open('simplefile.txt') as f:
        line = f.readline()
        while line:
            process(line)
            line = f.readline()

#%%
    print('-'*30)
    
    with open('simplefile.txt') as f:
        line = f.readline()
        while line:
            process(line)
            line = f.readline()

#%%
    print('-'*30)

    import fileinput
    for line in fileinput.input('simplefile.txt'):
        process(line)

#%%
    print('-'*30)

    with open('simplefile.txt') as f:
        for line in f:
            process(line)


#%%
    print('-'*30)

    for line in open('simplefile.txt'):
        process(line)
        
#%%
    print('-'*30)

    f = open('somefile2.txt', 'w')
    print('First', 'line', file=f)
    print('Second', 'line', file=f)
    print('Third', 'and final', 'line', file=f)
    f.close()

    lines = list(open('somefile2.txt'))
    print(lines)
    f.close()
    
    print('-'*30)
    first, second, third = open('somefile2.txt')
    print(first)
    print(second)
    print(third)
    f.close()

#%%
    print('-'*30)

    f = open('simplefile.txt')
    lines = f.readlines()
    print(lines)
    f.close()
    lines[1] += "This line was inserted...\n"
    f = open('simplefile.txt', 'w')
    f.writelines(lines)
    f.close()

#%%
    print('-'*30)
    pprint.pprint(open('simplefile.txt').readlines())

    print('-'*30)
#%%

if __name__ == '__main__': main()
