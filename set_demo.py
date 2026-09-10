servers={"app01", "app02", "app01", "db01"}

print(servers)
servers.add("app03")
print()
print(servers)
servers.remove("db01")
print()
print(servers)
if "app01" in servers:
    print("server exist")
