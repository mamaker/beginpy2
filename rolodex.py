# -*- coding: utf-8 -*-
"""
rolodex.py
Created on Tue Apr 23 17:12:06 2019

@author: madhu
"""


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    return data[label].get(name)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

MyNames = {}
init(MyNames)

store(MyNames, 'Magnus Lie Hetland')
store(MyNames, 'Mr. Gumby')
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
store(MyNames, 'Luke Skywalker', 'Anakin Skywalker')

print('-'*30)
print('Looking up Robin as first name:')
print(lookup(MyNames, 'first', 'Robin'))
print('-'*30)

print('Looking up Lie as middle name:')
print(lookup(MyNames, 'middle', 'Lie'))
print('-'*30)

print('Looking up '' as middle name:')
print(lookup(MyNames, 'middle', ''))
print('-'*30)

print('Looking up Skywalker as last name:')
print(lookup(MyNames, 'last', 'Skywalker'))
print('-'*30)


