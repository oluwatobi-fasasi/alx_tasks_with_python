queueList = []
for i in range(5):
    queueList.append(i)
    print(queueList)
print('------------------')
for i in range(5):
    queueList.pop(0)
    print(queueList)

print(queueList, type(queueList))
