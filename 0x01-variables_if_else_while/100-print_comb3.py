def numComb():
    for i in range(10):
        for j in range(10):
            if(i == 8 and j == 9):
                print(str(i) + str(j))
            elif i < j:
                print(str(i) + str(j) + ', ', end='')
    print('')
numComb()
