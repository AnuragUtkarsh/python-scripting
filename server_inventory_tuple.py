i=int(input("Enter number of servers: "))
servers=[]
for j in range(1,i+1,1):
    server_name=input("Enter the server name: ")
    cpu_usage=int(input("Enter the CPU Usage: "))
    memory=int(input("Enter the Memory Usage: "))
    one_server=(server_name,cpu_usage,memory)
    servers.append(one_server)

print("========================")
print("Server Inventory Report")
print("========================")

for k in servers:
    print("Servers: ", k[0])
    print("Servers: ", k[1])
    print("Servers: ", k[2])

    if k[1] > 90 or k[2] > 90:
        print("Status CRITICAL")
    else:
        print("Status HEALTHY")


