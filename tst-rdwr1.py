# -*- coding: utf-8 -*-
"""
tst-rdwr1.py
This and That
(c) Madhu Vasudevan 2019
"""


def main():

#%%
    print('-'*30)
    filename = 'somefile.txt' 
    f = open(filename, 'w')
    f.write('Hello, ')
    f.write('World!')
    f.close()

#%%
    print('-'*30)
    filename = 'somefile.txt' 
    f = open(filename, 'r')
    print(f.read(4))
    print(f.read())
    f.close()

#%%
    print('-'*30)
    filename = 'somefile.txt' 
#    f = open(filename, 'w')
    with open(filename, 'w') as f:
        f.write('01234567890123456789')
        f.seek(5)
        f.write('Hello, World!')
#    f.close()

#%%
    print('-'*30)
    filename = 'somefile.txt' 
#    f = open(filename)
    with open(filename) as f:
        print(f.read())
#    f.close()
    
#%%
    print('-'*30)
    filename = 'somefile.txt' 
#    f = open(filename)
    with open(filename) as f:
        print(f.read(3))
        print(f.read(2))
        print(f.tell())
#    f.close()


#%%
if __name__ == '__main__': main()
