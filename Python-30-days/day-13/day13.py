# Task 1 — Create a server inventory JSON file
# import json
# servers = {
#     "prod-web-01": {
#         "cpu": 75,
#         "memory": 65,
#         "disk": 80,
#         "status": "running"
#     },
#     "prod-api-01": {
#         "cpu": 92,
#         "memory": 88,
#         "disk": 95,
#         "status": "running"
#     },
#     "prod-db-01": {
#         "cpu": 65,
#         "memory": 70,
#         "disk": 75,
#         "status": "running"
#     }
# }

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/servers.json", 'w') as file : 
#     json.dump(servers, file, indent=4)

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/servers.json", 'r') as file1:
#     server_data = json.load(file1)
#     print(server_data)

#     for server ,metrics in server_data.items():
#         print(f"\nServer Name: {server}")
#         print(f"CPU: {metrics['cpu']}%")
#         print(f"Memory : {metrics['memory']}%")
#         print(f"Disk: {metrics['disk']}%")
#         print(f"Status: {metrics['status']}")


# Task 2 — Process JSON monitoring data
# import json
# server_count = 0
# cpu_unhealthy = 0
# memory_unhealthy = 0
# disk_unhealthy = 0
# server_cpu_unhealthy = []
# server_memory_unhealthy = []
# server_disk_unhealthy = []


# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/servers.json", 'r') as file:
#     server_data = json.load(file)
#     # print(server_data)

#     for server ,metrics in server_data.items():
#         server_count += 1
#         if metrics['cpu'] > 80:
#             cpu_unhealthy += 1
#             server_cpu_unhealthy.append(server)
            
#         if metrics['memory'] > 85:
#             memory_unhealthy += 1
#             server_memory_unhealthy.append(server)
            
#         if metrics['disk'] > 90:
#             disk_unhealthy += 1
#             server_disk_unhealthy.append(server)
            

#     print(f"Total Servers in inventory: {server_count}\n")
#     print(f"\nTotal Servers with CPU crossing Threshold 80%: {cpu_unhealthy}\nServer List with CPU Umhealthy:\n{", ".join(server_cpu_unhealthy)}\n")
#     print(f"\nTotal Servers with Memory crossing Threshold 80%: {memory_unhealthy}\nServer List with Memory Umhealthy:\n{", ".join(server_memory_unhealthy)}")
#     print(f"\nTotal Servers with Disk crossing Threshold 80%: {disk_unhealthy}\nServer List with Disk Umhealthy:\n{", ".join(server_disk_unhealthy)}")

# # Task 3: Export server inventory to CSV
import csv
import json
with  open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/servers.json", 'r') as file:
    server_data = json.load(file)
    # print(type(server_data))

with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.csv", 'w',  newline="") as file_csv:
    fieldnames = ["server_name", "cpu", "memory", "disk", "status"]
    writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
    writer.writeheader()
    for server, metrics in server_data.items():
        row = {
            "server_name": server,
            "cpu": metrics['cpu'],
            "memory": metrics['memory'],
            "disk": metrics['disk'],
            "status": metrics['status']

        }
        writer.writerow(row)

# Task 4: Read CSV and identify unhealthy servers
# import csv
# # cpu_unhealthy_servers = []
# # memory_unhealthy_servers = []
# # disk_unhealthy_servers = []

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.csv", 'r') as file_csv:
#         reader = csv.DictReader(file_csv)

#         for row in reader:
#                 reason =[]

#                 if int(row['cpu']) > 80:
                        
#                         # cpu_unhealthy_servers.append(row['server_name'])
#                         reason.append(f"- CPU usage: {row['cpu']}%")
                        
                        
#                 if int(row['memory']) > 85:
                        
#                         # memory_unhealthy_servers.append(row['server_name'])
#                         reason.append(f"- Memory usage: {row['memory']}%")

#                 if int(row['disk']) > 90:
                        
#                         # disk_unhealthy_servers.append(row['server_name'])
#                         reason.append(f"- Disk usage: {row['disk']}%")
#                 if reason:
#                     print(f"\nUnhealthy Server: {row['server_name']}")
#                     print("Reasons:")
#                     for index , reasons in enumerate(reason, start=1) :
#                                 print(reasons)

        # print(f"CPU is unhealthy for servers as usage is above 80%:\n{'\n'.join(cpu_unhealthy_servers)}\n")
        # print(f"Memory is unhealthy for servers as usage is above 85%:\n{'\n'.join(memory_unhealthy_servers)}\n")
        # print(f"Disk is unhealthy for servers as usage is above 90%:\n{'\n'.join(disk_unhealthy_servers)}\n")

#-----------------Q & A ------------------------
# Q1. What is the difference between json.load() and json.loads()?
# json.load() - works with file - it reads json file and converts to python object
# json.loads() - works with strings - connverts json string to python object

# Q2. What is the difference between json.dump() and json.dumps()?
# json.dump() - works with file - Writes a Python  objects to json file
# json.dumps() - works with strings - converts python object to json string

# Q3. Why do we commonly use JSON in REST APIs?
# JSON is commonly used in REST APIs because it is lightweight, human-readable, language-independent, and supports structured data such as nested objects and arrays. It allows different systems and programming languages to exchange data easily.

# For example, a monitoring API could return CPU, memory, disk and server status in one JSON response.

# Q4. What is the difference between JSON and CSV? Give an SRE/DevOps use case for each.
# JSON - will be have key value pair , suited  for API responses, configurations
# Example : 
# {
#     "prod-web-01": {
#         "cpu": 75,
#         "memory": 65,
#         "disk": 80,
#         "status": "running"
#     }
# }

# CSV - Comma separated Value , suited for reports, inventories
# server_name,cpu,memory,disk,status
# prod-web-01,85,65,80,running
# prod-api-01,92,80,95,running
# prod-db-01,65,90,75,running

# Q5. Why does csv.DictReader() return values as strings, even when a column contains numbers?
#  CSV is a text-based format and does not store data types or schemas. Therefore, csv.DictReader() reads field values as strings. We must explicitly convert numeric fields using int() or float() when performing calculations or comparisons.

# This is an important distinction: CSV doesn't know that 92 represents CPU usage rather than a string.

# Q6. What happens if you try to read a JSON file containing invalid JSON syntax? Which exception should you handle?
# when we try to read invalide json file code will stop executing with JSONDecodeError error, we should handle JSONDecodeError exception

# Q7. Why do we use newline="" when opening CSV files for writing, especially on Windows?    
    # It prevents unwanted blank lines between records on some platforms, particularly Windows.   