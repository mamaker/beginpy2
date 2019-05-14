"""
test-heaps.py
This and That
(c) Madhu Vasudevan 2019
"""

from collections import deque


#%%
print('-'*30)

q = deque(range(5))
print('q:', q)
q.append(5)
print('q:', q)
q.appendleft(6)
print('q:', q)

print(q.pop())
print('q:', q)
print(q.popleft())
print('q:', q)
print('-'*30)

q.rotate(3)
print('q:', q)
q.rotate(-1)
print('q:', q)
#%%
    
