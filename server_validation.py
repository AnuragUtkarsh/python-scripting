i=int(input("Enter number of servers: "))
for j in range(1,i+1,1):
    for k in range(1,4,1):
        if k == 1:
            if j==3:
                print("CPU Check Skipped")
                continue
            else:
                print("CPU Check")
        elif j==2 and k==2:
            print("Memory Check Failed")
            break
        elif k==2:
            print("Memory Check")
        else:
            print("Service Check")
