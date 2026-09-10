servers = [{
    "hostname": "app01",
    "ip": "192.168.1.10",
    "role": "app",
    "resources": {
        "cpu": 75,
        "memory": 60
    }
},
{
    "hostname": "app02",
    "ip": "192.168.1.11",
    "role": "app",
    "resources": {
        "cpu": 85,
        "memory": 70
    }
},
{
    "hostname": "db01",
    "ip": "192.168.1.12",
    "role": "db",
    "resources": {
        "cpu": 55,
        "memory": 40
    }
}]

for server in servers:
    print(server["hostname"])
    if server["resources"]["cpu"] > 70 or server["resources"]["memory"] >70:
        print("CRITICAL: ", server["hostname"])
    else:
        print("HEALTHY: ", server["hostname"])
   
print()

for server in servers:
    if server["role"] == "db":
        print("it is a DB server: ", server["hostname"])
    else:
        print("it is a App server: ", server["hostname"])
