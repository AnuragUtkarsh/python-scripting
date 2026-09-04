cpu_usage=int(input("Enter CPU Value: "))
if cpu_usage < 50:
    print("Less CPU Usage")
elif cpu_usage >=50 and cpu_usage <=80:
    print("Normal CPU")
elif cpu_usage > 80:
    print("High CPU")
else:
    print("invalid Value")

