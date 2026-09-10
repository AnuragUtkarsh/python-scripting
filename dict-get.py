server={"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60}

#print(server.get("hostname", "Not_defined"))
#print(server.get("environment", "NOT_DEFINED"))
#print(server.get("port", "8080"))
for key, value in server.items():
    if key=="cpu" or key=="memory":
        print(key,value)
