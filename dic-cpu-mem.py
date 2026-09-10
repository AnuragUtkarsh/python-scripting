servers = [
    {"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60},
    {"hostname": "app02", "ip": "192.168.1.11", "role": "db", "cpu": 87, "memory": 53},
    {"hostname": "db01", "ip": "192.168.1.12", "role": "db", "cpu": 50, "memory": 95}
]

for server in servers:
    if server["cpu"] > 80 or server["memory"] > 80:
        print("CRITICAL", server["hostname"])
    else:
        print("NORMAL", server["hostname"])

print()

for server in servers:
    if server["role"]=="db":
        print("DB Server: ", server["hostname"])
    else:
        print("App Server: ", server["hostname"])
