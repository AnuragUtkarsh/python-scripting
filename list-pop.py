servers=["app01", "app02", "web01", "web02", "db01", "db02"]
for i in servers:
    print(i)
print()

removed_server=servers.pop(2)

print(removed_server)
