i=int(input("Enter Number of servers: "))
for j in range(1,i+1,1):
    cpu_usage=int(input("Enter CPU Usage: "))
    print("Checking Server: ",j)
    if cpu_usage == 45:
        print("Normal")
    elif cpu_usage == 95:
        print("High CPU")
    elif cpu_usage == 70:
        print("Threshold")
