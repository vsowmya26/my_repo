#Task 1 — Create a CPU health-check function
def check_cpu(cpu_usage):
    if cpu_usage >= 80:
        return "WARNING"
    else :
        return "HEALTHY"
# Checking for 3 different values
result_cpu = check_cpu(75)
print(result_cpu)

result_cpu = check_cpu(80)
print(result_cpu)

result_cpu = check_cpu(95)
print(result_cpu)

# Task 2 — Create memory and disk functions
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90
def check_memory(memory_usage):
    if memory_usage >= MEMORY_THRESHOLD:
        return "WARNING"
    else :
        return "HEALTHY"
# Checking for 3 different values
result_memory = check_memory(85)
print(result_memory)

result_memory = check_memory(70)
print(result_memory)

result_memory = check_memory(90)
print(result_memory)

def check_disk(disk_usage):
    if disk_usage >= DISK_THRESHOLD:
        return "WARNING"
    else:
        return "HEALTHY"
# Checking for 3 different values
result_disk = check_disk(85)
print(result_disk)

result_disk = check_disk(70)
print(result_disk)

result_disk = check_disk(90)
print(result_disk)

#Task 4 — Challenge: Create an overall health function
def over_all_health(cpu_status, memory_status, disk_status):

    if cpu_status == "HEALTHY" and memory_status == "HEALTHY" and disk_status == "HEALTHY":
        return "SERVER HEALTHY"
    else: 
        return "SERVER UNHEALTHY"

#Task 3 — Build a reusable server health checker
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
    },
    "prod-worker-01": {
        "cpu": 40,
        "memory": 50,
        "disk": 60
    }
}

overall_server_warning_count = 0
server_with_atleast_1_warning_count = 0
for server_name , details  in servers.items():
    
    cpu_usage = servers[server_name]['cpu']
    memory_usage = servers[server_name]['memory']
    disk_usage = servers[server_name]['disk']
    result_cpu = check_cpu(cpu_usage)
    result_memory = check_memory(memory_usage)
    result_disk = check_disk(disk_usage)
    print(f"Server_name : {server_name}, CPU - {result_cpu}, MEMORY -  {result_memory} ,DISK - {result_disk} ")
    if result_cpu == "WARNING" or result_memory == "WARNING" or result_disk == "WARNING":
        server_with_atleast_1_warning_count += 1
    if result_cpu == "WARNING" and result_memory == "WARNING" and result_disk == "WARNING":
        overall_server_warning_count += 1   
    overall_health = over_all_health(result_cpu, result_memory, result_disk )
    print(f"{server_name}\nOverall Health: {overall_health}\n")
print(f"Number of servers with atleast 1 WARNING state {server_with_atleast_1_warning_count}")
print(f"Number of servers in warning state {overall_server_warning_count}")
    


#----------------------Q & A -----------------------------------------

# What is a function in Python, and why do we use functions in production automation?
# function in python is used to create reusable block of code to avoid writing repetative steps multiple time
# We use function in production environmnets so that the same code can be reused for mltiple servers to calculate teh metrics and check srever health and same code can be reused if any new servers added without modifying the current block of code

# What is the difference between a parameter and an argument?
# parameter - variable declared in function definition
# arguments -value to parameter while calling function

# What is the difference between print() and return?
# print() - displays the result
# return - send the result back to caller so it can be used in other part of program 


# What happens if a function does not explicitly return anything?
# it returns None


# Can a Python function return multiple values? Explain with an example.
# Yes it can return multiple values , in this overall heal if we want to check for Unhealthy server which parameter (cpu, memory or disk)s unhealthy which is making overall server status unhealty , we can use the rtur statement as return "UNHEALTHY" ,"CPU-STATUS" cpu_status, "MEMORY_STATUS" memory_status, "DISK STATUS" disk_status