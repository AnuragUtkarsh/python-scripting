server={"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60}

server["environment"]="prod"
print(len(server))
print(server)
del server["role"]
print()
print(len(server))
print(server.keys())
print(server.values())
print(server.items())
print(list(server.keys()))
print(list(server.values()))
print(list(server.items()))
print(server)
print()
for key in server.keys():
    print(key)

print()
for item in server.items():
    print(item)

print()
for key,value in server.items():
    print(key,value)
