server={"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60}
print(server["hostname"])
print(server["cpu"])
server["cpu"]=85
server["environment"]="prod"
print(server)
