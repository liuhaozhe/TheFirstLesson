for i in range (1,10):
    for j in range (1,10):
        if j<=i:
            print (i,"*",j,"=",i*j,end="    ")
    if j == 9:
            print("\n")
