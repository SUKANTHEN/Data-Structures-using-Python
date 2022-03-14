# Initialize empty list
stack = []
# Inserting data into stack using 'append'
stack.append('s')
stack.append('u')
stack.append('k')
stack.append('a')
stack.append('n')
# print stack
print("After inserting data:")
print(stack)

# .pop() function is used to remove the last inserted element in the stack, following LIFO principle
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# remaining will only be 's' in stack
print('\nAfter removal of elements:')
print(stack)
