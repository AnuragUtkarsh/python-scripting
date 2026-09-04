service_status=input("Enter the service Status(True/False): ")
cpu_usage=int(input("Enter CPU Usage: "))

if service_status == "True":
    print("Service is UP")
    if cpu_usage > 80:
        print("High CPU Usage")
    else:
        print("CPU Usage Normal")
else:
    print("Service is Down")

