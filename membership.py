# -*- coding: utf-8 -*-
"""
membership.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

# Check a user name and PIN code
database = [
            ['albert', '1234'],
            ['dilbert', '4242'],
            ['smith', '7524'],
            ['jones', '9843']
            ]
username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database: print('Access granted')
