cpu_core=int(input("Enter the CPU Core: "))

if cpu_core < 8:
    print("Low CPU Server")
elif cpu_core == 8:
    print("Sufficient CPU")
else:
    print("High CPU Server")

