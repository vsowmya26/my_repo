#Task 1 - Build a server inventory.
servers = {
    "prod-web-01": {
        "ip": "10.0.1.10",
        "cpu": 45,
        "memory": 65,
        "status": "running"
    },
    "prod-api-01": {
        "ip": "10.0.1.20",
        "cpu": 92,
        "memory": 88,
        "status": "running"
    },
    "prod-db-01": {
        "ip": "10.0.1.30",
        "cpu": 78,
        "memory": 90,
        "status": "stopped"
    },
    "prod-worker-01": {
        "ip": "10.0.1.40",
        "cpu": 55,
        "memory": 70,
        "status": "running"
    }
}

print(f"Complete Infra inventory: {servers}\n")
server_running_count = 0
server_stopped_count = 0
for server in servers:
    print(f"Server - {server} : IP - {servers[server]['ip']}")
    print(f"Server - {server} : CPU  - {servers[server]['cpu']}% : Memory -  {servers[server]['memory']}% )\n")
    if servers[server]['status'] == "running":
        server_running_count += 1
    else:
        print(f"CRITICAL : Server {server} is stopped. Please check \n")
        server_stopped_count += 1

    if servers[server]['cpu'] >= 80:
        print(f"WARNING : CPU Usage is above 80% for server {server} - {servers[server]['cpu']}%\n")
    
print(f"\nTotal number of servers: {len(servers)}\n")
print(f"Total number of running servers: {server_running_count}\n")
print(f"Total number of stopped servers: {server_stopped_count}\n")

#Task 2 - Update infrastructure records
servers["prod-web-01"]["cpu"] = 85

servers.update({
    "prod-cache-01": {
        "ip": "10.0.1.50",
        "cpu": 30,
        "memory": 40,
        "status": "running"
    }
})

servers.pop("prod-worker-01")
print(f"Updated Inventory: {servers}")

#Task 3 - Safe dictionary access
server = {
    "name": "prod-web-01",
    "ip": "10.0.1.10",
    "cpu": 75
}

print(server.get("name"))
print(server.get("memory"))
if server.get("memory") is  None:
  print("Memory information unavailable")

try:
  print(server["memory"])
except KeyError as e:
  print(f"key {e} does not exist in the server dictionary")

#Task 4 - Production health summary
running_list = []
stopped_list = []


for server in servers:
    if servers[server]['status'] == "running" : 
        running_list.append(server)
    else:
        stopped_list.append(server)



print("Servers list which are in running state:")
print(f"Running servers: {running_list}")
print("Servers list which are in stopped state:")
print(f"Stopped servers: {stopped_list}")

#Higest CPU usage server
highest_cpu = 0
highest_cpu_server = ""
for server_name, details in servers.items():
    if details['cpu'] > highest_cpu:
        highest_cpu = details['cpu']
        highest_cpu_server = server_name
print(f"Server with highest CPU usage: {highest_cpu_server} - {highest_cpu}%")

#Highest Memory usage server
highest_memory = 0
highest_memory_server = ""
for server_name, details in servers.items():
    if details['memory'] > highest_memory:
        highest_memory = details['memory']
        highest_memory_server = server_name
print(f"Server with highest Memory usage: {highest_memory_server} - {highest_memory}%")

#Averaege CPU usage across all servers
total_cpu = 0
for server in servers:
    total_cpu += servers[server]['cpu']
average_cpu = total_cpu / len(servers)
print(f"Average CPU usage: {average_cpu}%")



#---------------------Q & A---------------------
# What is the difference between a list and a dictionary?
#list - A list is an ordered collection of items that can be accessed by their index. It allows duplicate values and is defined using square brackets [].
#dictionary - A dictionary is an unordered collection of key-value pairs, where each key is unique. It allows for fast lookups and is defined using curly braces {}.


# What is a nested dictionary, and where would you use it in SRE automation?
#nested dictionary is a dictionary that contains another dictionary as its value or dictionary within a dictionary. It allows for organizing data in a hierarchical structure. In SRE automation, nested dictionaries can be used to represent complex configurations, such as server inventories, where each server has multiple attributes like IP address, CPU usage, memory usage, and status.


# What is the difference between dict["key"] and dict.get("key")?
#dict["key"] raises a KeyError if the key does not exist in the dictionary, while dict.get("key") returns None (or a specified default value) if the key is not found, allowing for safer access to dictionary values.


# What does the items() method return?
# items() method returns  dictionary's key-value tuple pairs.


# Can dictionary keys be lists? Why or why not?
# No , dictoionary keys cannot be lists as , keys should be unique , where as lists are immutable in nature and can be modified. Therefore, lists cannot be used as keys in a dictionary.