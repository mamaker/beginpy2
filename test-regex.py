# -*- coding: utf-8 -*-
"""
test-regex.py
This and That
(c) Madhu Vasudevan 2019
"""

import re


def main():

#%%
    print('-'*30)    

    text = 'alpha, beta,,,,gamma    delta'
    print(re.split('[, ]+', text))
    print(re.split('[, ]+', text, maxsplit=0))
    print(re.split('[, ]+', text, maxsplit=1))
    print(re.split('[, ]+', text, maxsplit=2))
#%%
    print('-'*30)    

    text = 'foobarookah'
    print(re.split('o(o)', text))

#%%
    print('-'*30)    

    text = '"Hm... Err -- are you sure?" he said, sounding insecure.'

    pat = '[a-zA-Z]+'
    print(re.findall(pat, text))

    pat = r'[.?\-",]+'
    print(re.findall(pat, text))
    
#%%
    print('-'*30)    

    text = 'Dear {name}...'
    pat = '{name}'
    print(re.sub(pat, 'Mr. Gumby', text))


#%%
    print('-'*30)    

    print(re.escape('www.python.org'))
    'www\\.python\\.org'
    print(re.escape('But where is the ambiguity?'))

#%%
    print('-'*30)
    
    text = 'www.python.org'
    pat = r'www\.(.*)\..{3}'
    m = re.match(pat, text)
    
    for i in range(2):
        print('Group',i)
        print(m.group(i))
        print(m.start(i))
        print(m.end(i))
        print(m.span(i))

#%%
    print('-'*30)

#    emphasis_pattern = r'\*([^\*]+)\*'
    emphasis_pattern = re.compile(r'''
    \*               # Beginning emphasis tag -- an asterisk
    (                # Begin group for capturing phrase
    [^\*]+           # Capture anything except asterisks
    )                # End group
    \*               # Ending emphasis tag
    ''', re.VERBOSE)
    print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!'))

    print('-'*30)    
#%%    

#%%
    print('-'*30)

    emphasis_pattern = r'\*(.+)\*'
    print(re.sub(emphasis_pattern, r'<em>\1</em>', '*This* is *it*!'))

    emphasis_pattern = r'\*\*(.+?)\*\*'
    print(re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**!'))
    print('-'*30)
#%%


if __name__ == '__main__': main()
    