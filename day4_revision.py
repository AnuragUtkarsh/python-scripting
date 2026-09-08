i=int(input("Enter number of server: "))
print("========================\nServer Monitoring Report\n========================")
for j in range(1,i+1,1):
    cpu=int(input("Enter CPU Percentage: "))
    memory=int(input("Enter Memory Percentage: "))
    if cpu < 90 or memory < 90:
        print("Healthy")
    elif cpu >= 90 or memory >= 90:
        print("Critical")
    else:
        print("Healthy")
        print()

print("================================")
