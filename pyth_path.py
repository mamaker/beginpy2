# -*- coding: utf-8 -*-
"""

Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


import os
import sys, pprint
import copy

try:

#%%
    print('-'*30)
    cwd = r'C:\max\PyStuf\beginpy' 
    os.chdir(cwd)

    dirpath = os.getcwd()
    foldername = os.path.basename(dirpath)
    
    print('dirpath:', dirpath)
    print('foldername:', foldername)
    print('-'*30)
    
    print('sys.path:')
    pprint.pprint(sys.path)
    print('-'*30)
    
    print('sys.argv =', sys.argv)
    print('-'*30)
#%%
    
#%%
    os.startfile(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    print('-'*30)
    os.system(r'C:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe')   
    print('-'*30)
    import webbrowser
    webbrowser.open('http://www.python.org')
    print('-'*30)
#%%
    

#%%
    copy_dir=[n for n in dir(copy) if not n.startswith('_')]
    print('copy_dir:\n',copy_dir)
    print('-'*30)
    print('copy.__all__:\n',copy.__all__)
    help(copy.copy)
    print('-'*30)
    print(copy.copy.__doc__)
    print('-'*30)
    print('Source of copy:\n',copy.__file__)
    print('-'*30)
#%%



except Exception as e:
    print('Sorry, error in file i/o:\n',e)

