servers = [
    {"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60},
    {"hostname": "app02", "ip": "192.168.1.11", "role": "db", "cpu": 87, "memory": 53}
]

for server in servers:
    if server["cpu"] > 80:
        print("High CPU Server: ",server["hostname"])
