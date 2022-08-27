def comb():
    for i in range(10):
        if i == len(range(10)) - 1:
            print(i)
        else:
            print(str(i) + ', ', end = '')
comb()
