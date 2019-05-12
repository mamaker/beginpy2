# -*- coding: utf-8 -*-
"""
string_formats.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

# Print a formatted price list with a given width
width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)


#%%
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)
#%%

#%%
produce = {
        'Apples': 0.4,
         'Pears': 0.5,
         'Cantaloupes': 1.92,
         'Dried Apricots (16 oz.)': 8,
         'Prunes (4 lbs.)': 12,
         }
for item,key in produce.items():
    print(fmt.format(item, key))
print('=' * width)
    
#%%
