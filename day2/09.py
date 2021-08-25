for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print("{}X{}={}".format(j, i, i * j), end=" ")
    print("")