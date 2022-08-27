def numComb():
    i = '0'
    a = '0'

    while i <= '9':
        while a <= '9':
            if not(i > a or i == a):
                print(i, a)
                if i == '8' and a == '9':
                    print('')
                else:
                    print(', ')
            a = a + str(1)
        a = '0'
        i = i + str(1)
    return(0)
numComb()
