# -*- coding: utf-8 -*-
"""
string_misc.py
Created on Tue Apr 23 17:12:06 2019

@author: madhu
"""
print('-'*30)
#%%
a_string = 'Hello, world!'
print(sorted(a_string, key=str.lower))
print(list(reversed(a_string)))
print(''.join(reversed(a_string)))
print('-'*30)
#%%


#%%
mesg = '!!! $$$ Get rich now!!! $$$ Get rich now!!! $$$ Get rich now!!!'
patch = '$$$'
loc = mesg.find(patch)
while  loc >= 0:
    print ('found',patch,'@ loc:',loc )
    loc = mesg.find(patch, loc+1)
print('-'*30)
#%%

   
#%%
table = str.maketrans('cs', 'kz')
print('table:',table)
print('this is an incredible test'.translate(table))
print('-'*30)

#%%

#%%
table = str.maketrans('cs', 'kz', ' ')
print('table:',table)
print('this is an incredible test'.translate(table))
print('-'*30)

#%%

#%%
trans_dict = {'c':'k', 's':'z', ' ':None}
table = str.maketrans(trans_dict)
print('table:',table)
print('this is an incredible test'.translate(table))
print('-'*30)

#%%

#%%
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('-'*30)
print('C:' + '\\'.join(dirs))
print('-'*30)
#%%


#%%
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))
print('-'*30)
#%%

#%%
import string
print('string.digits:',string.digits)
print('string.ascii_letters:',string.ascii_letters)
print('string.ascii_lowercase:',string.ascii_lowercase)
print('string.ascii_uppercase:',string.ascii_uppercase)
#print('string.printable :',string.printable)
print('string.punctuation:',string.punctuation)
print('string.ascii_uppercase :',string.ascii_uppercase)
print(string.capwords("that's all, folks"))
print("that's all, folks".title())
print('-'*30)
#%%








