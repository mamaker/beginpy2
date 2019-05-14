"""
test-randoms.py
This and That
(c) Madhu Vasudevan 2019
"""

from random import *
from time import *

#%%
'''
Some Important Functions in the time Module
Function            Description
asctime([tuple])    Converts a time tuple to a string
localtime([secs])   Converts seconds to a date tuple, local time
gmtime([secs])      Converts seconds to a date tuple, universal time
mktime(tuple)       Converts a time tuple to local time
sleep(secs)         Sleeps (does nothing) for secs seconds
strptime(string[, format]) Parses a string into a time tuple
time()              Current time (seconds since the epoch, UTC)

'''

'''
The Fields of Python Date Tuples
Index   Field       Value
0       Year        For example, 2000, 2001, and so on
1       Month       In the range 1–12
2       Day         In the range 1–31
3       Hour        In the range 0–23
4       Minute      In the range 0–59
5       Second      In the range 0–61
6       Weekday     In the range 0–6, where Monday is 0
7       Julian day  In the range 1–366
8       Daylight savings 0, 1, or –1

time-tuple = (year, month, day, hour, minut, sec, weekday, julian-day, daylight-saving)
'''

'''
Some Important Functions in the random Module
Function                Description
random()        Returns a random real number n such that 0 ≤ n ≤ 1
getrandbits(n)  Returns n random bits, in the form of a long integer
uniform(a, b)   Returns a random real number n such that a ≤ n ≤ b
randrange([start], stop, [step]) Returns a random number from range(start, stop, step)
choice(seq)     Returns a random element from the sequence seq
shuffle(seq[, random]) Shuffles the sequence seq in place
sample(seq, n)  Chooses n random, unique elements from the sequence seq
'''
#%%

#%%
print('-'*30)
print('Time:', asctime())

print('-'*30)
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
print('date1:',date1, 'time1:',time1)
print('date2:',date2, 'time2:',time2)

print('-'*30)
#%%
    

#%%
print('-'*30)
random_time = uniform(time1, time2)
print('Random Time:',asctime(localtime(random_time)))
print('-'*30)
#%%

#%%
print('-'*30)
num   = int(input('How many dice? '))
sides = int(input('How many sides per die? '))
sum = 0
for i in range(num): 
    die = randrange(sides) + 1
    sum += die
    print('die',i,':',die )
print('The sum of dice :', sum)

print('-'*30)
#%%






