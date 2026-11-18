##TASK - 1
server_names = [
    "prod-web-01",
    "prod-api-01",
    "prod-db-01",
    "prod-worker-01"
]

cpu_usages = [45, 92, 78, 85]
warning_threshold = 80
critical_threshold = 90
critical_count = 0

print("===== PRODUCTION SERVER CPU MONITOR =====")
for i in range(len(server_names)):       
        server = server_names[i]
        cpu = cpu_usages[i]
        
        
        if cpu >= critical_threshold:    
                print(f"Server: {server}\n CPU Usage:  {cpu}\nStatus : CRITICAL\n-------------------\n")
                critical_count += 1
                
        elif cpu >= warning_threshold:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : WARNING\n-------------------\n")
        else:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : NORMAL\n-------------------\n")
        
print(f"Total number of Servers monitored are {len(server_names)} and critical servers are {critical_count}")       

# ---------------------------------------------------------------------------------------------------
# TASK -2 
attempt = 1
max_attempts = 3
service_ready = False

while service_ready == False and attempt <= max_attempts:
    print("Starting service health check...")
    print(f"Attempt: {attempt}")
    # if attempt == 2:
    #         service_ready = True
    #         print(f"Attempt  {attempt}: Service started successfully!")
    #         break
    if service_ready  :
         print(f"Attempt  {attempt}: Service started successfully!")
         break
    else:
        print(f"Attempt {attempt}: Service not ready. Retrying...")
     
    
    attempt += 1
if service_ready:
           print("Service started successfully")
else:
         print("Service failed after maximum retries")     
print("Health check completed.")

# ---------------------------------------------------------------------------------------------------
TASK -3
server_names = [
    "prod-web-01",
    "prod-api-01",
    "prod-db-01",
    "prod-worker-01"
]

cpu_usages = [45, 92, 78, 85]
warning_threshold = 80
critical_threshold = 90
critical_count = 0
server_count = 0
print("===== PRODUCTION SERVER CPU MONITOR =====")
for i in range(len(server_names)):       
        server = server_names[i]
        cpu = cpu_usages[i]

        if server == "prod-db-01":
                print(f"Server {server} is under maintainance\n")
                continue
        
        if cpu >= critical_threshold:    
                print(f"Server: {server}\n CPU Usage:  {cpu}\nStatus : CRITICAL\n-------------------\n")
                critical_count += 1
                
        elif cpu >= warning_threshold:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : WARNING\n-------------------\n")
        else:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : NORMAL\n-------------------\n")
        server_count += 1
print(f"Total number of Servers monitored are {server_count} and critical servers are {critical_count}")    

# ---------------------------------------------------------------------------------------------------
# TASK -4
server_names = [
    "prod-web-01",
    "prod-api-01",
    "prod-db-01",
    "prod-worker-01"
]

cpu_usages = [45, 92, 78, 85]
warning_threshold = 80
critical_threshold = 90
critical_count = 0
server_count = 0
print("===== PRODUCTION SERVER CPU MONITOR =====")
for i in range(len(server_names)):       
        server = server_names[i]
        cpu = cpu_usages[i]
        server_count += 1
        
        if cpu >= critical_threshold:    
                print(f"Server: {server}\n CPU Usage:  {cpu}\nStatus : CRITICAL\n {server} is in CRTICAL state check immediately\n-------------------\n")
                critical_count += 1
                break
                
        elif cpu >= warning_threshold:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : WARNING\n-------------------\n")
        else:
                print(f"Server: {server}\nCPU Usage:  {cpu}\nStatus : NORMAL\n-------------------\n")
        
print(f"Total number of Servers monitored are {server_count} and critical servers are {critical_count}")    

# -------------------------Q & A ------------------------------------
# Q1. What is the difference between a for loop and a while loop in Python? Give one SRE/DevOps use case for each.
    #  for loop executes until the completion on iteratives 
    #       Example : I have to monitor set of 10 servers and get the metrics of all servers I will go wth for loop 
    # While loop executes until the until condition becomes false
    #       Example : If I have to monitor any readiness of service and try reattempt certain number of time then will go with while loop

# Q2. What is an infinite loop? How can an infinite loop affect a production automation script?
#   Infinite loop occurs when the condition is always true , this will affect because the script keeps running and server performance will degrade and cpu might spike

# Bonus: What is the difference between break and continue?
#   break - Braks the iteration
# conitnue - Skips the current iteration