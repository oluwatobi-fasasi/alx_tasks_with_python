import collections

stack = collections.deque()
for i in range(5):
    stack.append(i)

print(stack)

stack.pop() # This removes the last element fro the list
print(stack, type(stack))

listStack = list(stack) #Casting the daque into list
tupleStack = tuple(stack) #Casting the daque into tuple

print(listStack, type(listStack))
print(tupleStack, type(tupleStack))

