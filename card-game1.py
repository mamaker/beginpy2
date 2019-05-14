# -*- coding: utf-8 -*-
"""
card-game1.py
This and That
(c) Madhu Vasudevan 2019
"""

from pprint import pprint
from random import shuffle

values = ['Ace']+list(range(2, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]

#pprint(deck[:12])
print(','.join(deck))
shuffle(deck)
pprint(deck[:12])

while deck: input(deck.pop())
