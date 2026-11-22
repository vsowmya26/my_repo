# Task 1 — Read a server log file
error_count = 0
warning_count = 0
info_count = 0
error_logs = []
total_log_entries = 0

with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/server.log", 'r') as file:
    for line in file:
        total_log_entries += 1
        # print(line.strip())
# Task 2 — Count log severity levels
        if "ERROR" in line:
           error_count += 1  
# Task 3 — Extract critical errors
           error_logs.append(line.strip())

           
        if "WARNING" in line:
            warning_count +=1
        if "INFO" in line:
            info_count += 1

print(f"\nTotal ERROR messages:{error_count}")
print(f"Total WARNING messages:{warning_count}")
print(f"Total INFO messages:{info_count}\n")



# Task 4 — Generate an incident report        
with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/incident_report.txt", 'w') as file1:
    file1.writelines(f"PRODUCTION INCIDENT REPORT\n--------------------------\nTotal log entries: {total_log_entries}\nERROR count: {error_count}\nWARNING count: {warning_count}\nINFO count:{info_count}\n\nCRITICAL ERRORS: \n")
    for  index, critical_error in enumerate(error_logs, start=1):
        parts = critical_error.split()
        message = " ".join(parts[3:])
        file1.write(f"{index}. {message}\n")
    
   
    

print(f"Error Logs:{error_logs}")


with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/incident_report.txt", 'r') as file1:
    report = file1.read()
    print(report)


# Task 5 — Advanced SRE challenge
count_error = 0
latest_error = None
with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/large_server.log", 'r') as largefile:
    for line in largefile:
        if "ERROR" in line:
            latest_error = line.strip()
            count_error +=1
    print(f"Total number of Error count: {count_error}")
    print(latest_error)


# -------------Q & A---------------"
# Q1. What is the difference between "w" and "a" file modes?
# w - write file by overwriting existing Connection
# a - write file by appending the contnet

# Q2. Why is with open() preferred over simply using open()?
#  with open() - will open the file and perform auto close after read/write operation
#  open() - will open the file and need to file.close() expilictly , if not mentioned memory leak might happen   

# Q3. What happens when you try to open a nonexistent file using "r" mode?
# file not found error will occur

# Q4. What is the difference between read(), readline(), and readlines()?
# read() - read entire content
# readline() - read one line
# readlines() - read line by line and store the contnet in list 

# Q5. Why is reading a large log file line by line better than loading the entire file into memory?
# Line by line reading is better with less proceesing time and less memory consumption , more cpu will be consumed while script run to read large file