def comb4():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i == 7 and j == 8 and k == 9:
                    print(str(i) + str(j) + str(k))
                elif i < j and j < k:
                    print(str(i) + str(j) + str(k) + ', ', end ='')

comb4()
