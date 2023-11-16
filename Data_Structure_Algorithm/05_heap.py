'''
    Used to represent a priority queue. It alwaus gives the smallest element
    whenever element is popped.
    Time complexity is O(log n)
    Two type MinHeap and MaxHeap
'''

import heapq

li=[5,3,7,4,8,9]
print(li)

heapq.heapify(li)
print(li)

heapq.heappush(li,100)
print(li)

heapq.heappop(li)
print(li)
print(li.__str__())

heapq.heappop(li)
print(li)
heapq.heappop(li)
print(li)