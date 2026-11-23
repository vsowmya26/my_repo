# Task 1 — Safe disk utilization calculator
disk_capacity = 0
disk_used = 85

try:
    disk_utilisation = (disk_used/disk_capacity)* 100
   

except ZeroDivisionError:
    print("Error: Disk capacity cannot be Zero")

else:
    print(f"Disk utilisation: {disk_utilisation}%")

finally:
    print("Disk utilization check completed")

# Task 2 — Production log file reader
error_count = 0
warning_count = 0
info_count = 0
log_file_path = "c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/server.log"
try:
    with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/server.log" , 'r') as file :
        for line in file:
            if "ERROR" in line:
                error_count += 1
            if "WARNING"  in line:
                warning_count += 1
            if "INFO" in line:
                info_count += 1

except FileNotFoundError:
    print(f"{log_file_path} Not Found")

except PermissionError:
    print(f"Read permission to file {log_file_path} is not there ")

else:
    print(f"Error Count: {error_count}\nWarning Count: {warning_count}\nInfo Count: {info_count}")

finally:
    print("Production log file reader completed")

# Task 3 — Validate server monitoring data
disk_capacity = "-100"
disk_used = "85"

try:
    disk_capacity_n = float(disk_capacity)
    disk_used_n = float(disk_used)
    disk_utlisation = (disk_used_n/disk_capacity_n) * 100

    
except ValueError:
    print("Error: Invalid Value conversion, only numbers can be type converted to float/int")

except ZeroDivisionError:
    print("Error: Disk capacity cannot be Zero")

else:
    print(f"Disk Utlisation : {disk_utlisation}%")

finally:
    print("Disk utilization check completed")

# Task 4 — Raise your own exception
def check_disk_usage(disk_usage):
    if disk_usage > 90:
        raise ValueError("Usage exceeds threshold, server is unhealthy")
    else:
         return "HEALTHY"
    

try: 
     result = check_disk_usage(95)   

except ValueError as error:
        print(error)

else:
     print(result)

# -----------------Q & A ----------------------------------------

# What is the difference between an error and an exception in Python?
# error - error occurs when code cannot execute/failed and cannot proceed until fixed
# exception- cathing the error and print a valid message for teh exception to handle the error , but code can proceed to execute further 

# Exceptions are events that disrupt normal execution and may be handled. Errors is a broader informal term; syntax errors are one example.


# What is the difference between except and finally?
# execpt - block of code to cathe the specific exception with a meaningfule messsage
# finally - block of code written at end to print a message , so that we can ensure the complete script has been executed without any error (with execption being caught if any)

# Correct basic understanding. finally is primarily useful for cleanup and always runs during normal exception handling flow.

# What is the purpose of the else block in exception handling?
# else: this block runs only when no exception occurs .



# Why should we avoid using a bare except: in production scripts?
#  Beacuse it catches all exceptions , this might cause unkowing problems getting caught and not getting fixed in the code 
# It can catch unexpected exceptions and hide important failures.

# What is the difference between raise and try/except?
# raise - raise an exception deliberatily when condition occurs
# try/except handles  built in python exceptions

# raise deliberately raises an exception; try/except handles exceptions. raise can also re-raise an existing exception.

# In an SRE automation script, why is handling FileNotFoundError important?
# It is important to avoid unexpetd termination of the script because file is not present

# 	Prevents an unexpected crash and allows graceful failure handling.