servers=[{"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60},{"hostname": "app02", "ip": "192.168.1.11", "role": "db", "cpu": 87, "memory": 53}]
for server in servers:
    for key, value in server.items():
        if key=="hostname" or key=="cpu":
            print(key,value)

