# Task 1 – Update a JSON server inventory
# import json
# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'r') as file_json:
#     server_data = json.load(file_json)
#     server_data.update({"prod-db-01": 
#                         {"cpu": 85,
#         "memory": 73,
#         "disk": 81,
#         "status": "running"
#     }})
    
#     server_data["prod-web-01"]['cpu'], server_data["prod-api-01"]['status'] = 80, "maintenance"



# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'w') as file:
#     json.dump(server_data, file , indent=4)

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'r') as file_final:   
#     print(json.load(file_final))

# Task 2 – JSON Infrastructure Health Report
# import json
# # server_count = 0

# server_cpu_unhealthy = []
# server_cpu_unhealthy_count = 0

# server_memory_unhealthy = []
# server_memory_unhealthy_count = 0

# server_disk_unhealthy = []
# server_disk_unhealthy_count = 0

# cpu_count = 0
# memory_count = 0
# disk_count = 0


# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/monitoring.json",'r') as file_monitor:
#     monitoring = json.load(file_monitor)
#     server_count = len(monitoring["servers"])
    
#     for server in monitoring["servers"]:
#         # server_count += 1
        
#         cpu_count += server['cpu']
        
#         memory_count += server['memory']
#         disk_count += server['disk']
#         if server["cpu"] > 80:
#             server_cpu_unhealthy.append(server['name'])
#             server_cpu_unhealthy_count += 1
#         if server["memory"] > 85:
#             server_memory_unhealthy.append(server['name'])
#             server_memory_unhealthy_count += 1
#         if server["disk"] > 90:
#             server_disk_unhealthy.append(server['name'])
#             server_disk_unhealthy_count += 1


      
#     if server_count > 0:
#         average_cpu = cpu_count/server_count
#         average_memory = memory_count/server_count
#         average_disk = disk_count/server_count
#         highest = max(monitoring["servers"], key=lambda server: server["cpu"])
#         print(f"Average CPU utilisation is : {average_cpu}")
#         print(f"Average Memory utilisation is : {average_memory}")
#         print(f"Average Disk utilisation is : {average_disk}")
#         print(f"Server with maximu cpu utilisation is: {highest['name']} with CPU utilisation of {highest['cpu']}%")
#     else:
#         print("No server records found")


    
    
#     print(f"Total Servers in list: {server_count}")   
#     print(f"Total server breaches CPU threshold: {server_cpu_unhealthy_count}\nServers List with CPU greater than 80 %:\n{", ".join(server_cpu_unhealthy)}\n")
#     print(f"Total server breaches Memory threshold: {server_memory_unhealthy_count}\nServers List with Memory greater than 85 %:\n{", ".join(server_memory_unhealthy)}\n")
#     print(f"Total server breaches Disk threshold: {server_disk_unhealthy_count}\nServers List with Disk greater than 90 %:\n{", ".join(server_disk_unhealthy)}\n")

# Task 3 – Filter production servers from CSV
# import csv
# production_server_list = []
# production_server_breach_metrics = []
# unhealthy_server_list = []


# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_metrics.csv",'r') as file_csv:
#     metrics = csv.DictReader(file_csv)

#     for server in metrics:
#         reason = []
#         if server["environment"] == "production":
#             production_server_list.append(server["server_name"])
#             if int(server["cpu"]) > 80 or int(server["memory"]) > 85 or int(server["disk"]) > 90:
#                 production_server_breach_metrics.append(server["server_name"])
                

#             if int(server['cpu']) > 95 or int(server['memory']) > 95 or int(server['disk']) > 95:
#                 server["severity"] = "CRITICAL"
#             elif int(server['cpu']) > 80 or int(server['memory']) > 85 or int(server['disk']) > 90:
#                 server["severity"] = "WARNING"
#             else:
#                 server["severity"] = "HEALTHY"
                            
#             if int(server["cpu"]) > 80:
#                 reason.append("CPU above 80%")
                
            
#             if int(server["memory"]) > 85:
#                 reason.append("Memory above 85%")


#             if int(server["disk"]) > 90:
#                 reason.append("Disk above 90%")
#             server["reason"] = ", ".join(reason)
#             if reason:
#                 unhealthy_server_list.append(server)
    
# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/unhealthy_servers.csv",'w', newline="") as file_csv_1:
#     fieldnames = ["server_name", "environment", "cpu", "memory", "disk", "status","severity", "reason"]
#     writer = csv.DictWriter(file_csv_1, fieldnames=fieldnames)
#     writer.writeheader()
   
   
    
#     for server in unhealthy_server_list:
#         writer.writerow(server)

#     print(f"Production server list in metrics inventory:\n{'\n'.join(production_server_list)}")
#     print()
#     print(f"servers where CPU, memory or disk breaches its threshold:\n{'\n'.join(production_server_breach_metrics)}")
#     print(unhealthy_server_list)


# Task 4: CSV to JSON conversion
# import json
# import csv
# list_server = []
# # prod_server_count = 0 
# prod_server_list = []
# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_metrics.csv",'r') as file_csv:
#     metrics = csv.DictReader(file_csv)
#     for server in metrics:
#         server["cpu"] = int(server["cpu"])
#         server["memory"] = int(server["memory"])
#         server["disk"] = int(server["disk"])
#         list_server.append(server)

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'w') as file_json:
#     json.dump(list_server, file_json, indent=4)

# with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'r') as file_json_read:
#     inventory= json.load(file_json_read)
#     for server in inventory:
#         # if server["server_name"]:
#         #     prod_server_count += 1
#         if server["environment"] == "production":
#             prod_server_list.append(server["server_name"])
#     print(f"Total nummber fo servers in inventory: {len(inventory)}")
#     print(f"Production server list:\n{'\n'.join(prod_server_list)}")





# ----------------Q & A -------------------------
# Interview-ready answer
# Method	Purpose
# json.dump()	Serializes a Python object and writes it to a JSON file.
# json.dumps()	Serializes a Python object into a JSON string.
# json.load()	Reads JSON from a file and deserializes it into a Python object.
# json.loads()	Deserializes a JSON string into a Python object.

# Easy way to remember
# - dump → file output
# - dumps → string output
# - load → file input
# - loads → string input