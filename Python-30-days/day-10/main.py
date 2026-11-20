import cpu_monitor as cpu
import memory_monitor as memory
import disk_monitor as disk 

servers = {
    "prod-web-01": {
        "cpu": 75,
        "memory": 60,
        "disk": 70
    },
    "prod-api-01": {
        "cpu": 92,
        "memory": 88,
        "disk": 95
    },
    "prod-db-01": {
        "cpu": 65,
        "memory": 91,
        "disk": 80
    }
}
server_count_warning_state = 0
for server_name , details in servers.items():
    cpu_status = cpu.check_cpu(details["cpu"])
    memory_status = memory.check_memory(details["memory"])
    disk_status = disk.check_disk(details["disk"])
    print(f"\nServer: {server_name}\nCPU: {cpu_status}\nMemory: {memory_status}\nDisk: {disk_status}")
    if cpu_status ==  "WARNING" or memory_status  ==  "WARNING" or disk_status ==  "WARNING":
        server_count_warning_state += 1
print(f"Total server count with atleast one metric with WARNING state {server_count_warning_state}")
