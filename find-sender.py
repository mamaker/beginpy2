# -*- coding: utf-8 -*-
"""
find-sender.py
This and That
(c) Madhu Vasudevan 2019
"""

import fileinput, re

def main():

#%%
    print('-'*30)    

    print('From:')
    pat = re.compile('From: (.*) <.*?>$')
    for line in fileinput.input():
        m = pat.match(line)
        if m: print(m.group(1))

#%%
    print('-'*30)    

    pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
    addresses = set()
    for line in fileinput.input():
        for address in pat.findall(line):
            addresses.add(address)

    print('Email Addresses:')
    for address in sorted(addresses):
        print(address)
    
    print('-'*30)
#%%


if __name__ == '__main__': main()
