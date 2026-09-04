cpu_usage=int(input("Cpu Percentage: "))
memory_usage=int(input("Memory Percentage: "))

if cpu_usage > 90 or memory_usage > 90:
    print("High Resource Alert")
else:
    print("Normal Resource")

