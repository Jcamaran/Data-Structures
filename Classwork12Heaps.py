import random

#import a list of 200 random numbers

L = []
for i in range(200):
    x = random.randint(0,1000)
    L.append(x)
print("Unsorted List:")
print(L)
# throw all numbers into the heap
import heapq

Heap = []
for i in range(200):
    x = L[i]
    heapq.heappush(Heap, x)
print("Heap:")
print(Heap)

#pop all numbers out of the heap

Sorted = []
for i in range(0,200):
    x = heapq.heappop(Heap)
    Sorted.append(x)
print("Sorted Numbers:")
print(Sorted)

