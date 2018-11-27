

for x in range(1,11):
    for y in range(1,11):
        z=x*y
        if  z%2==1:
            print("0",end="\t")
        else:
            print(x*y,end="\t")
    print()
