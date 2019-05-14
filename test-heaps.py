"""
test-heaps.py
This and That
(c) Madhu Vasudevan 2019
"""

from heapq import *
from random import shuffle


#%%
print('-'*30)

data = list(range(10))
shuffle(data)
print('data:', data)

heap = []
for n in data:
    heappush(heap, n)
print('heap:', heap)

heappush(heap, 0.5)
print('heap:', heap)

print('Gonna Pop:', heap[0])
print('popped:', heappop(heap))
print('popped:', heappop(heap))
print('popped:', heappop(heap))
print('popped:', heappop(heap))
#%%


#%%
print('-'*30)
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print('heap:', heap)
heapreplace(heap, 10)
print('heap:', heap)
#%%


print('-'*30)
#%%
    
