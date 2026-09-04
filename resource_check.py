cpu_core=int(input("Enter the CPU Core: "))
memory=int(input("Enter the Memory in GB: "))
if cpu_core > 8 and memory > 16:
    print("High Resource Server")
elif cpu_core < 8 and memory < 16:
    print("Low Resource Server")
else:
    print("Normal Resource Server")
