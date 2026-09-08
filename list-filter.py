i=int(input("Enter number of servers: "))
servers=[]
for j in range(1,i+1,1):
    server_name=input("Enter name of servers: ")
    servers.append(server_name)

for k in servers:
    if "db" in k:
        print(k)
