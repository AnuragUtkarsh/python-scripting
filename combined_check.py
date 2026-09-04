cpu_usage=int(input("Enter the CPU Usage: "))
memory_usage=int(input("Enter the memory usage: "))
service_status=input("Enter the service Status(True/False): ")

if (cpu_usage > 90 or memory_usage > 90) and service_status == "True":
    print("Critical Resource Alert")
else:
    print("No Critical Alert")
