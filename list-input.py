i=int(input("Enter number of servers: "))
servers=[]
for j in range(1,i+1,1):
    server_name=input("Enter the server name: ")
    servers.append(server_name)

for k in servers:
    print(k)
