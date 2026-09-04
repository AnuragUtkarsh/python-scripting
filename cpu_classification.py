cpu_core=int(input("Enter The Number of CPU: "))

if cpu_core <= 4:
    print("Small Server")
elif cpu_core <= 8:
    print("Medium Server")
else:
    print("Large Server")
