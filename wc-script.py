# -*- coding: utf-8 -*-
"""
wc-script.py
This and That
(c) Madhu Vasudevan 2019
"""

import sys

def main():

#%%
    text = sys.stdin.read()
    words = text.split()
    wordcount = len(words)
    print('Wordcount:', wordcount)
#%%

if __name__ == '__main__': main()
