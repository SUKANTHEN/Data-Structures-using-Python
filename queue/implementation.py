queue = [] 
# Adding elements to the queue
queue.append('s')
queue.append('u')
queue.append('k')
queue.append('a')
queue.append('n')

print("After Inserting into queue or Enqueue:")
print(queue)
 
# Removing elements from the queue as per FIFO Principle
print("\nElements dequeued from queue:")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
