i= int(input("Enter number of servers: "))
print("========================\nServer Monitoring Report\n========================")
for j in range(1,i+1,1):
    cpu_usage=int(input("Enter CPU Usage: "))
    memory=int(input("Enter Memory Usage: "))
    if cpu_usage >= 45 and memory <= 60:
        print("Server: ",j)
        print("CPU Usage: ", cpu_usage,"%")
        print("Memory Usage: ",memory,"%")
        print("Status: Healthy")
        print()
    elif cpu_usage >= 95 or memory >= 50:
        print("Server: ",j)
        print("CPU Usage: ", cpu_usage,"%")
        print("Memory Usage: ",memory,"%")
        print("Status: Critical")
        print()
    elif cpu_usage <= 50 or memory >= 95:
        print("Server: ",j)
        print("CPU Usage: ", cpu_usage,"%")
        print("Memory Usage: ",memory,"%")
        print("Status: Critical")
        print()
    elif cpu_usage >= 90 and memory >= 90:
        print("Server: ",j)
        print("CPU Usage: ", cpu_usage,"%")
        print("Memory Usage: ",memory,"%")
        print("Status: Critical")
        print()

print("========================")




