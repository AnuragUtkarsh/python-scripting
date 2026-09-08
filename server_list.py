servers = ["app01", "app02", "web01", "web02", "db01", "db02"]

print(len(servers))
print()

for i in servers:
    print(i)

print()

if "db01" in servers:
    print("Server Present")
else:
    print("Server Absent")

print()

servers.append("app03")

servers.remove("web01")

print()

for i in servers:
    print(i)

