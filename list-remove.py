servers=["app01", "app02", "web01", "web02", "db01", "db02"]
for i in servers:
    print(i)
print()
servers.append("db03")
for i in servers:
    print(i)

print()
servers.remove("web01")
for i in servers:
    print(i)



