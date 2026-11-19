# Task 1 — Positional and keyword arguments
def server_info(server_name, environment, cpu_usage):
    return f"Server : {server_name}\n Environment : {environment}\n CPU : {cpu_usage}"

result = server_info("prod-web-01", "production",85)
result_pos = server_info(cpu_usage=90, server_name="satg-web-01" , environment="staging")
print(result)
print(result_pos)

#Task 2 — Default arguments for CPU monitoring
def check_cpu(cpu_usage, threshold=80):
    if cpu_usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"

print(check_cpu(85))
print(check_cpu(75))
print(check_cpu(75, 70))
print(check_cpu(90, 95))

# Task 3 — Multiple return values
server = {
    "name": "prod-api-01",
    "cpu": 92,
    "memory": 88,
    "disk": 95
}

def get_server_metrics(server):
    return server["cpu"], server["memory"], server["disk"]

cpu,memory,disk = get_server_metrics(server)
print(f"CPU Usge : {cpu}%\nMemory Usage: {memory}%\n Disk Usage: {disk}")

# Task 4 — Advanced SRE challenge
servers = {
    "prod-web-01": {
        "type": "web",
        "cpu": 85,
        "memory": 70
    },
    "prod-db-01": {
        "type": "database",
        "cpu": 75,
        "memory": 82
    },
    "prod-worker-01": {
        "type": "worker",
        "cpu": 88,
        "memory": 92
    }
}

thresholds = {
    "web": {
        "cpu": 80,
        "memory": 85
    },
    "database": {
        "cpu": 70,
        "memory": 80
    },
    "worker": {
        "cpu": 90,
        "memory": 90
    }
}

def check_server_health(server_name, cpu_usage, memory_usage, cpu_threshold, memory_threshold):
    # CPU Usage check
    if cpu_usage >= cpu_threshold:
        cpu_status = "WARNING"
    else:
        cpu_status = "HEALTHY"

    # Memory Usage check 
    if memory_usage >= memory_threshold:
        memory_status = "WARNING"
    else:
        memory_status = "HEALTHY"
    
    return cpu_status, memory_status 

for server_name , details  in servers.items():
    server_type = details["type"]
    cpu_usage = details["cpu"]
    memory_usage =details["memory"]
    cpu_threshold = thresholds[server_type]["cpu"]
    memory_threshold = thresholds[server_type]["memory"]
    cpu_status, memory_status = check_server_health(server_name, cpu_usage, memory_usage, cpu_threshold, memory_threshold)
    print(f"\nServer: {server_name}\n CPU: {cpu_status}\n Memory: {memory_status}")



#-------------------------Q & A----------------------------
# What is the difference between positional and keyword arguments?
# positional arguments - while calling the function we just need to pass teh values to paramaeter and the values will be assigned to parameter in function arguments in sequence
# keyword arguments - while calling function we can assign value to parameter and no need to be concerned about sequence which is define as is in function paramters

# What are default arguments, and why are they useful?
# default arguments -  in this type, parameter will be assigned a default value in function definition itself , we can either pass teh value to default parameter while function call or skip passing it will take the assigned value in function parameter definition .
# this is useful when certain parameters value is mostly fixed or it will not throw any error if missed to provide value while function call  

# Can we pass positional and keyword arguments together? What is the correct order?
# We can pass positional and keyword arguments together , correct order is positional first and then keyword

# How does Python handle multiple return values?
# multiple return values can be returned with comma separted and python packages multiple return values in to tuple and allow us to unpack


# What is the difference between return None and not writing a return statement?
# Both functions return None when called.

# The difference is that the first explicitly returns None, while the second implicitly returns None because no return statement was executed.


# Remember this rule:
    # - Number of arguments passed to a function = number of required input parameters.
    # - Number of variables on the left side of unpacking = number of returned values.
    # These numbers do not need to be equal.