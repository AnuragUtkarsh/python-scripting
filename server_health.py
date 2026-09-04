hostname=input("Enter the Hostname: ")
environment=input("Enter the Environment(PRD,QAS,DEV): ")
cpu_usage=int(input("Enter the CPU Utilization Percentage: "))
memory=int(input("Enter the Memory use Percentage: "))
service_status=input("Enter the Service Status(True/False): ")

print("========================\nServer Health Report\n========================")
print("Hostname: ",hostname)
print("Environment: ", environment)
print("CPU Usage: ", cpu_usage)
print("Memory Usage: ",memory)
print("Service: ",service_status)

if service_status == "True":
    print("Health is fine")
    if cpu_usage > 90 or memory > 90:
        print("Resource Utilization is high")
    else:
        print("Resource Utilization is less")
elif service_status == "False":
    print("Status: CRITICAL")
    if (cpu_usage < 90 or memory < 90):
        print("Resource utilization is normal")
    else:
        print("Resource utilization is high") 
elif (cpu_usage > 90 or memory > 90) and service_status == "True":
    print("Status: CRITICAL")
elif (cpu_usage > 90 or memory > 90) and service_status == "False":
    print("Status: CRITICAL")
else:
    print("Status: HEALTHY")
print("========================")
