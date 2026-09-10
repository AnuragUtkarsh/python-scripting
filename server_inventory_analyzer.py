servers = [{
    "hostname": "app01",
    "ip": "192.168.1.10",
    "role": "app",
    "environment": "prod",
    "resources": {
        "cpu": 75,
        "memory": 60
    }
},
{
    "hostname": "app02",
    "ip": "192.168.1.11",
    "role": "app",
    "environment": "dev",
    "resources": {
        "cpu": 85,
        "memory": 70
    }
},
{
    "hostname": "db01",
    "ip": "192.168.1.12",
    "role": "db",
    "environment": "QAS",
    "resources": {
        "cpu": 55,
        "memory": 40
    }
}]
critical_count=0
healthy_count = 0
db_server=0
app_server=0
print("==============================\nSERVER INVENTORY REPORT\n==============================")
for server in servers:
    print("Hostname: ",server["hostname"])
    print("Role: ", server["role"])
    print("Environment: ", server["environment"])
    print("CPU: ", server["resources"]["cpu"])
    print("Memory: ", server["resources"]["memory"])
    if server["resources"]["cpu"] > 80 or server["resources"]["memory"] >80:
        print("Status: CRITICAL")
        critical_count+=1
    else:
        print("Status: HEALTHY")
        healthy_count+=1
    if server["role"] == "db":
        db_server+=1
    else:
        app_server+=1

print()
print("==============================\nSUMMARY\n==============================")
print("Total Server: ", len(servers))
print("Critical Server: ", critical_count)
print("Healthy server: ", healthy_count)
print("DB server: ", db_server)
print("App Server: ", app_server)
