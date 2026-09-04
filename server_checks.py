i=int(input("Enter number of servers: "))
for j in range(1,i+1,1):
    print("Checking server: ",j)
    for k in range(1,4,1):
        if k == 1:
            print("CPU Check")
        elif k == 2:
            print("Memory Check")
        else:
            print("Service Check")

