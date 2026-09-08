i=int(input("Enter number of server: "))
servers=[]
for j in range(1,i+1,1):
    server_name=input("Enter Server name: ")
    cpu=int(input("Enter CPU usage: "))
    memory=int(input("Enter Memory Usage: "))
    one_server=(server_name,cpu,memory)
    servers.append(one_server)

for k in servers:
    if k[1]>90:
        print("High CPU Server: ", k[0])



