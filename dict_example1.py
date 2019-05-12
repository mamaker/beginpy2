# -*- coding: utf-8 -*-
"""
dict_example1.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

# A simple database
# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# number and address, respectively.
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Name: ').strip().title()
# Are we looking for a phone number or an address?
request = input('Phone number (p) or address (a)? ').strip().lower()

# Use the correct key:
key = request # In case the request is neither 'p' nor 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary:
#if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

# Use get to provide default values:
label = labels.get(key, key)
person = people.get(name, {})
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))



