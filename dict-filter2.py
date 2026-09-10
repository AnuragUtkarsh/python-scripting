servers = [ {"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60, "environment": "PRD"}, {"hostname": "app02", "ip": "192.168.1.11", "role": "db", "cpu": 87, "memory": 53, "environment": "QAS"}, {"hostname": "db01", "ip": "192.168.1.12", "role": "db", "cpu": 50, "memory": 95, "environment": "DEV"} ]

for server in servers:
    if server["environment"] == "PRD":
        print("environment-PRD", server["hostname"])
    elif server["environment"] == "QAS":
        print("enviroment-QAS", server["hostname"])
    else:
        print("enviroment-DEV", server["hostname"])


