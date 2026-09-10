server={"hostname": "app01", "ip": "192.168.1.10", "role": "application", "cpu": 75, "memory": 60}
if server["cpu"] > 70:
    print("High CPU")
else:
    print("low CPU")
