# -*- coding: utf-8 -*-
"""
exceptions.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""

#%%
from warnings import warn, filterwarnings

filterwarnings("ignore", category=DeprecationWarning)
warn("Another deprecation warning.", DeprecationWarning)
warn("Something else.")
#%%

#%%
from warnings import warn, filterwarnings

filterwarnings("error")
warn("This function is really old...", DeprecationWarning)
#%%

#%%
from warnings import warn, filterwarnings

filterwarnings("error")
warn("Something is very wrong!")
#%%


#%%
from warnings import warn, filterwarnings

filterwarnings("ignore")
warn("Anyone out there?")
#%%

#%%
from warnings import warn

warn("I've got a bad feeling about this.")
#%%

#%%
def describe_person(person):
    print('Description of', person['name'])
    print('Age:', person['age'])
    try:
        print('Occupation:', person['occupation'])
    except KeyError: pass

a_person = {'name':'Throatwobbler Mangrove',
#            'occupation': 'camper',
            'age': 42}

describe_person(a_person)
#%%

#%%
def faulty():
    raise Exception('Something is wrong')

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')

#ignore_exception()
handle_exception()        
#%%

#%%
try:
    1 / x
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")
#%%


#%%
x = None
try:
    x = 1 / 0
finally:
    print('Cleaning up ...')
    del x
#%%

#%%
try:
    print('A simple task', 1/0)
except:
    print('What? Something went wrong?')
else:
    print('Ah ... It went as planned.')
#%%

#%%
try:
    1/0
except ZeroDivisionError:
    raise ValueError from None 
#    raise ValueError
#%%
    
#%%
class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

calculator = MuffledCalculator()
print(calculator.calc('10 / 2'))
#print(calculator.calc('10 / 0'))
MuffledCalculator.muffled = True
#calculator.muffled = True
print(calculator.calc('10 / 0'))

#%%

#%%

while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print('x / y is', value)
#    except:
#        print('Invalid input. Please try again.')
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break
#%%

#%%
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except (ZeroDivisionError, ValueError, TypeError) as e:
    print("Your numbers were bogus.\n",e)
except :
    print('Something wrong happened ...')    
#%%
    
#%%
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except ValueError:
    print("That wasn't a number, was it?")    
#%%



#%%
class SomeCustomException(Exception): pass

raise SomeCustomException('Some Custom Message!')
#raise SomeCustomException
#%%

#%%
raise ArithmeticError
#raise Exception('hyperdrive overload')
#raise Exception
#1/0
#%%
