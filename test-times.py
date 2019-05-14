"""
test-times.py
This and That
(c) Madhu Vasudevan 2019
"""

import time

#%%
print('-'*30)

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

print('Time:',time.asctime())
print('-'*30)
#%%
    
