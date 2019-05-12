# -*- coding: utf-8 -*-
"""
class_misc.py
Created on Sat Apr 23 11:19:17 2019

@author: madhu

"""


#%%
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()
sb.eat()

print('-'*30)
#%%


#%%
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print('Hi, my value is', self.value)

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
x = '1 + 2 * 3'
tc.calculate(x)
tc.talk()
print('-'*30)

print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))
print(callable(getattr(tc, 'talk', None)))
print(getattr(tc, 'fnord', None))
print(callable(getattr(tc, 'fnord', None)))
setattr(tc, 'name', 'Mr. Gumby')
print(tc.name)
print('-'*30)
#%%



#%%
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
    def init(self): # Overrides init method from Filter superclass
        self.blocked = ['SPAM']

f = Filter()
f.init()
seq = [1, 2, 3]
print('filter:',f.filter(seq))

s = SPAMFilter()
s.init()
seq = ['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']
print('SPAMFilter:', s.filter(seq))

print('-'*30)
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))
print(Filter.__bases__)

print('-'*30)
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))
print(SPAMFilter.__bases__)
print('-'*30)
#%%


#%%
class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

m1 = MemberCounter()
m1.init()
print(MemberCounter.members)

m2 = MemberCounter()
m2.init()
print(MemberCounter.members)

print(m1.members)
print(m2.members)

m1.members = 'Two'
print(m1.members)
print(m2.members)

print('-'*30)
#%%


#%%
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

x = Secretive()
#s.__inaccessible()
x.accessible()
x._Secretive__inaccessible()
print('-'*30)
#%%

#%%
class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()
print('-'*30)
#%%


#%%
class Class:
    def method(self):
        print('I have a self!')

def function():
    print("I don't...")

instance = Class()
instance.method() # I have a self!
instance.method = function
instance.method() # I don't...

print('-'*30)
#%%

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))

#%%    
foo = Person()
foo.set_name('Luke Skywalker')
print(foo.get_name(), '=', foo.name)
foo.greet()
Person.greet(foo)
print('-'*30)
#%%

#%%
bar = Person()
bar.set_name('Anakin Skywalker')
print(bar.get_name(), '=', bar.name)
bar.greet()  
bar.name = 'Yoda'
Person.greet(bar)  
print('-'*30)
#%%


