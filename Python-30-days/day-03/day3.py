#----------------------Server Health Monitoring Script-------------------------#
server_name = "prod-web-01"

cpu_usage = 95
memory_usage = 87
disk_usage = 70


cpu_warning = 80
cpu_critical = 90

memory_warning = 85
memory_critical = 95

disk_warning = 80
disk_critical = 90

service_running = True


print(f"Server: {server_name} Health Report")
#----------------CPU HEALTH-------------------------#

if cpu_usage >= cpu_critical:
    cpu_health = "CRITICAL"
elif cpu_usage >= cpu_warning:
    cpu_health = "WARNING"
else:
    cpu_health = "NORMAL"
print(f"CPU Health: {cpu_health}")

#----------------MEMORY HEALTH-------------------------#
if memory_usage >= memory_critical:
    memory_health = "CRITICAL"
elif memory_usage >= memory_warning:
    memory_health = "WARNING"
else:
    memory_health = "NORMAL"
print(f"Memory Health: {memory_health}")    

#----------------DISK HEALTH-------------------------#
if disk_usage >= disk_critical:
    disk_health = "CRITICAL"
elif disk_usage >= disk_warning:
    disk_health = "WARNING"
else:
    disk_health = "NORMAL"
print(f"Disk Health: {disk_health}")    

#----------------SERVICE HEALTH-------------------------#
if service_running:
    service_health = "RUNNING"
else:
    service_health = "DOWN"
print(f"Service is : {service_health}")   

#----------------Overall Server HEALTH-------------------------#

if cpu_health == "CRITICAL" or memory_health == "CRITICAL" or disk_health == "CRITICAL" or service_health == "DOWN" :
    print("Overall Server Health: CRITICAL")
elif cpu_health == "WARNING" or memory_health == "WARNING" or disk_health == "WARNING":
    print("Overall Server Health: WARNING")
else:
    print("Overall Server Health: NORMAL")

# #----------------------Challenge 1 — Boundary testing-------------------------#
server_name = "prod-web-01"

cpu_usage = 70
memory_usage = 70
disk_usage = 90


cpu_warning = 80
cpu_critical = 90

memory_warning = 85
memory_critical = 95

disk_warning = 80
disk_critical = 90

service_running = True


print(f"Server: {server_name} Health Report")
#----------------CPU HEALTH-------------------------#

if cpu_usage >= cpu_critical:
    cpu_health = "CRITICAL"
elif cpu_usage >= cpu_warning:
    cpu_health = "WARNING"
else:
    cpu_health = "NORMAL"
print(f"CPU Health: {cpu_health}")

#----------------MEMORY HEALTH-------------------------#
if memory_usage >= memory_critical:
    memory_health = "CRITICAL"
elif memory_usage >= memory_warning:
    memory_health = "WARNING"
else:
    memory_health = "NORMAL"
print(f"Memory Health: {memory_health}")    

#----------------DISK HEALTH-------------------------#
if disk_usage >= disk_critical:
    disk_health = "CRITICAL"
elif disk_usage >= disk_warning:
    disk_health = "WARNING"
else:
    disk_health =  "NORMAL"
print(f"Disk Health: {disk_health}")    

#----------------SERVICE HEALTH-------------------------#
if service_running:
    service_health = "RUNNING"
else:
    service_health = "DOWN"
print(f"Service is : {service_health}")   

#----------------Overall Server HEALTH-------------------------#
if cpu_health == "CRITICAL" or memory_health == "CRITICAL" or disk_health == "CRITICAL" or service_health == "DOWN" :
    print("Overall Server Health: CRITICAL")
elif cpu_health == "WARNING" or memory_health == "WARNING" or disk_health == "WARNING":
    print("Overall Server Health: WARNING")
else:
    print("Overall Server Health: NORMAL")


# #----------------------Challenge 2 — Multiple failures-------------------------#
server_name = "prod-web-01"

cpu_usage = 95
memory_usage = 97
disk_usage = 95
service_running = False


cpu_warning = 80
cpu_critical = 90

memory_warning = 85
memory_critical = 95

disk_warning = 80
disk_critical = 90




print(f"Server: {server_name} Health Report")
#----------------CPU HEALTH-------------------------#

if cpu_usage >= cpu_critical:
    cpu_health = "CRITICAL"
elif cpu_usage >= cpu_warning:
    cpu_health = "WARNING"
else:
    cpu_health = "NORMAL"
print(f"CPU Health: {cpu_health}")

#----------------MEMORY HEALTH-------------------------#
if memory_usage >= memory_critical:
    memory_health = "CRITICAL"
elif memory_usage >= memory_warning:
    memory_health = "WARNING"
else:
    memory_health = "NORMAL"
print(f"Memory Health: {memory_health}")    

#----------------DISK HEALTH-------------------------#
if disk_usage >= disk_critical:
    disk_health = "CRITICAL"
elif disk_usage >= disk_warning:
    disk_health = "WARNING"
else:
    disk_health =  "NORMAL"
print(f"Disk Health: {disk_health}")    

#----------------SERVICE HEALTH-------------------------#
if service_running:
    service_health = "RUNNING"
else:
    service_health = "DOWN"
print(f"Service is : {service_health}")   

#----------------Overall Server HEALTH-------------------------#
if cpu_health == "CRITICAL" or memory_health == "CRITICAL" or disk_health == "CRITICAL" or service_health == "DOWN" :
    print("Overall Server Health: CRITICAL")
elif cpu_health == "WARNING" or memory_health == "WARNING" or disk_health == "WARNING":
    print("Overall Server Health: WARNING")
else:
    print("Overall Server Health: NORMAL")


# -------------------Challenge 3 — Maintenance mode-----------------------
server_name = "prod-web-01"

cpu_usage = 95
memory_usage = 87
disk_usage = 70


maintenance_mode = True
cpu_warning = 80
cpu_critical = 90

memory_warning = 85
memory_critical = 95

disk_warning = 80
disk_critical = 90

service_running = True

if maintenance_mode:
    print(f"Server: {server_name} is under maintenance")
else:
    print(f"Server: {server_name} Health Report")
    #----------------CPU HEALTH-------------------------#

    if cpu_usage >= cpu_critical:
        cpu_health = "CRITICAL"
    elif cpu_usage >= cpu_warning:
        cpu_health = "WARNING"
    else:
        cpu_health = "NORMAL"
    print(f"CPU Health: {cpu_health}")

    #----------------MEMORY HEALTH-------------------------#
    if memory_usage >= memory_critical:
        memory_health = "CRITICAL"
    elif memory_usage >= memory_warning:
        memory_health = "WARNING"
    else:
        memory_health = "NORMAL"
    print(f"Memory Health: {memory_health}")    

    #----------------DISK HEALTH-------------------------#
    if disk_usage >= disk_critical:
        disk_health = "CRITICAL"
    elif disk_usage >= disk_warning:
        disk_health = "WARNING"
    else:
        disk_health =  "NORMAL"
    print(f"Disk Health: {disk_health}")    

    #----------------SERVICE HEALTH-------------------------#
    if service_running:
        service_health = "RUNNING"
    else:
        service_health = "DOWN"
    print(f"Service is : {service_health}")   

    #----------------Overall Server HEALTH-------------------------#
    if cpu_health == "CRITICAL" or memory_health == "CRITICAL" or disk_health == "CRITICAL" or service_health == "DOWN":
        print("Overall Server Health: CRITICAL")
    elif cpu_health == "WARNING" or memory_health == "WARNING" or disk_health == "WARNING":
        print("Overall Server Health: WARNING")
    else:
        print("Overall Server Health: NORMAL")


# What is the difference between if, elif, and else? Give an example from a production server monitoring scenario.
# if - when only one condition needs to be checked for a specific action. For example, if the CPU usage is above 90%, we can set the CPU health to "CRITICAL".
# elif - when multiple conditions need to be checked in sequence, and only one of them should be executed. For example, if the CPU usage is between 80% and 90%, we can set the CPU health to "WARNING".
# else - when none of the previous conditions are met, and we want to execute a default action. For example, if the CPU usage is below 80%, we can set the CPU health to "NORMAL".


# What is the difference between and and or? How would you use each when checking CPU, memory, and disk health?
# and - when all conditions need to be true for a specific action. For example, if the CPU usage is above 90% and the memory usage is above 95%, we can set the overall health to "CRITICAL" , when all the conditions met.
# or - when any of the conditions need to be true for a specific action. For example, if the CPU usage is above 90% or the memory usage is above 95%, we can set the overall health to "CRITICAL" if any of the conditions are met.

# Why should a monitoring script check critical thresholds before warning thresholds? What kind of bug can happen if the order is reversed?
# If the order is reversed, a server might be reported as "WARNING" when it should be reported as "CRITICAL", leading to delayed response times and potential issues.