server_name = "prod-web-01"
environment = "production"
cpu_cores = 8
memory_gb = 16
disk_usage = 85.5
server_running = True

print(f"Server Name: {server_name}")
print(f"Environment: {environment}")
print(f"CPU Cores: {cpu_cores}")
print(f"Memory (GB): {memory_gb}")
print(f"Disk Usage: {disk_usage} GB")
print(f"Server Running: {server_running}")


print(type(server_name))
print(type(environment))
print(type(cpu_cores))
print(type(memory_gb))
print(type(disk_usage))
print(type(server_running))

#--------------------------------

ram = 16
cpu_cores = 8
disk_capacity = 100
disk_usage = 85.5

total_ram = ram * 3
total_cpu_cores = cpu_cores * 3
total_disk_capacity = disk_capacity * 3
remaining_disk_capacity_server_1 = disk_capacity - disk_usage

print(f"Total RAM: {total_ram} GB")
print(f"Total CPU Cores: {total_cpu_cores}")
print(f"Total Disk Capacity: {total_disk_capacity} GB")
print(f"Remaining Disk Capacity on Server_1: {remaining_disk_capacity_server_1} GB")

# '''--------------------------------'''
server_name = "prod-web-01"
cpu_cores = "8"
memory_gb = "16"

total_resources = int(cpu_cores) + int(memory_gb)

print("Server:", server_name)
print("Total resources:", total_resources)

# '''--------------------------------'''
server_name = "prod-db-01"
environment = "Production"
cpu_cores = 16
memory_gb = 32
disk_capacity = 200
disk_usage = 150

print("===== SERVER REPORT =====")
print(f"Server: {server_name}")
print(f"Environment: {environment}")
print(f"CPU: {cpu_cores} cores")
print(f"Memory: {memory_gb} GB")
print(f"Disk Capacity: {disk_capacity} GB")
print(f"Disk Used: {disk_usage} GB")
print(f"Disk Free: {disk_capacity - disk_usage} GB")


