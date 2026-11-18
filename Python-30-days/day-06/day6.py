servers = [
    "prod-web-01",
    "prod-api-01",
    "prod-db-01",
    "prod-web-01",
    "prod-worker-01",
    "prod-api-01"
]

print(f"Original List of Servers: {servers}\nTotal servers: {len(servers)}")

unique_servers = set(servers)
print(f"Unique List of Servers: {unique_servers}\nTotal unique servers: {len(unique_servers)}")

if "prod-db-01" in servers:
    print("prod-db-01 is present in the list of servers.")
servers.append("prod-cache-01")
print(f"Final Inventory list: {set(servers)}\nTotal servers: {len(set(servers))}")

# # #-----------------------------------------------------------------------

aws_servers = [
    "web-01",
    "api-01",
    "db-01",
    "worker-01"
]

onprem_servers = [
    "web-01",
    "db-01",
    "monitor-01",
    "backup-01"
]

print(f"Servers available in both environments: {set(aws_servers).intersection(set(onprem_servers))}")
print(f"Servers available only in AWS: {set(aws_servers).difference(set(onprem_servers))}")
print(f"Servers available only in On-Premise: {set(onprem_servers).difference(set(aws_servers))}")
print(f"Total unique servers across both environments: {set(aws_servers).union(set(onprem_servers))}")

# # #-----------------------------------------------------------------------

production_ports = (22, 80, 443, 8080)

for port in production_ports:
    print(f"Port {port} available on production servers.")

print(f"Total number of production ports: {len(production_ports)}")

if 443 in production_ports:
    print("Port 443 is available on production servers.")
 #Below code is  For checking if tuple can be modified and see what error it raises 
try:

        production_ports[0] = 2222
        print(production_ports)  

    
except TypeError as e:
        print(" Error: 'tuple' object does not support item assignment")


# # #-----------------------------------------------------------------------

server_names = [
    "prod-web-01",
    "prod-api-01",
    "prod-db-01",
    "prod-worker-01"
]

failed_servers = [
    "prod-api-01",
    "prod-worker-01"
]
healthy_count = 0
for server in server_names:
    if server not in failed_servers:
        print(f"Healthy server: {server}")
        healthy_count += 1
print(f"Total healthy servers: {healthy_count}")
print(f"Failed servers: {failed_servers}\nTotal failed servers: {len(failed_servers)}")


# # #-----------------------------------------------------------------------

# # What is the difference between a list, tuple, and set?
# # list - ordered, mutable, allows duplicates
# # tuple - ordered, immutable, allows duplicates  
# # set - unordered, mutable, does not allow duplicates


# # Why would you use a set instead of a list in infrastructure automation?
# # To eliminate duplicates


# # What is the difference between remove() and pop() in Python?
# # remove() - removes a specific element from the list by value
# # pop() - Deletes an element from the list by index and returns it


# # Can a tuple contain a list? If yes, can that list be modified?
# # Tuples can contain lists, but the tuple itself is immutable. However, the list inside the tuple can be modified (e.g., adding or removing elements from the list).
