def comb4():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i < j and j < k:
                    print(str(i) + str(j) + str(k) + ', ', end ='')

comb4()
