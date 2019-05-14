# -*- coding: utf-8 -*-
"""
fortune.py
This and That
(c) Madhu Vasudevan 2019
"""

import fileinput, random

fortunes = list(fileinput.input())
print(random.choice(fortunes))
