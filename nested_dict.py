server = {
    "hostname": "app01",
    "ip": "192.168.1.10",
    "resources": {
        "cpu": 75,
        "memory": 60
    }
}

print(server["resources"])
print(server["resources"]["cpu"])
print(server["resources"]["memory"])
