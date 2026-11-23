# Task 1 — Append server audit logs
server_name = "prod-web-01"
cpu_usage = 75
memory_usage = 85
disk_usage = 78

with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/server_audit.log", 'a') as file:
    file.write(f"{server_name} | CPU: {cpu_usage}% | Memory: {memory_usage}% | Disk: {disk_usage}% ")

# Task 2 — Extract only ERROR logs
error_count = 0
error_file = ""
with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/application.log", 'r') as file, open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/error_only.log", 'a') as error_file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
            error_file.writelines(line)


    print(f"Total ERROR entries extracted: {error_count}")

# Task 3 — Build a dynamic service incident report
service_count = 0
started_count = 0
failed_count = 0
failed_service = []
failed_service_list = ""
with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/service.log", 'r') as servicefile:
    for line in servicefile:
        service_count += 1
        if "FAILED" in line :
            failed_count += 1
            failed_service.append(line)

        else:
            started_count +=1
            
    for index, service in enumerate(failed_service, start=1):
        failed_service_list += f"{index}. {service.strip()}\n"

    print("SERVICE STATUS REPORT\n---------------------")
    print(f"Total services: {service_count}\nStarted services: {started_count}\nFailed services: {failed_count}\n")
    if failed_service_list:
        print(f"FAILED SERVICES:\n{failed_service_list}")
    else:
        print("FAILED SERVICES:\nNo failed services found.")

# # Task 4 — Advanced challenge: Process a large log file
log_entries = 0
warning_count = 0
with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/production.log", 'r') as largefile, open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/warning_report.log", 'a') as warningfile:
    for line in largefile:
        log_entries += 1
        if "WARNING" in line:
            warning_count += 1
            warningfile.writelines(line)

    print(f"Total log entries processed: {log_entries}\n")
    print(f"WARNING entries found: {warning_count}\n")
    print("WARNING report generated successfully.")

