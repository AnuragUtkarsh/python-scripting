servers=["app01", "app02", "web01", "web02", "db01", "db02"]
for i in servers:
    print(i)
print()

if "db01" in servers:
    print("server Present")
