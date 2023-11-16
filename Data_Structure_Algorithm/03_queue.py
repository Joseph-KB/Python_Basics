'''
    Stores items in FirstInFirstOut manner
'''

queue = []

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

print(queue)

queue.pop(0)
queue.pop(0)

print(queue)
