i=int(input("Enter list of servers: "))
servers=[]
for j in range(1,i+1,1):
    server_name=input("Enter name of server: ")
    cpu=int(input("Enter CPU use: "))
    memory=int(input("Enter the Memory: ")) 
    servers.append([server_name,cpu,memory])

#servers.append(["app03",76,45])
#print(servers[0])
#for k in servers:
#    print(k)

print()
#print(servers[0][0])
#print(servers[0][1])
#print(servers[0][2])

for k in servers:
    if k[1] > 90:
        print("high CPU server: ",k[0])



