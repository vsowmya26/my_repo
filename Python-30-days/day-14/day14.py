# Task - 1 Extract error keywords from logs
# import re
# error_logs = []
# error_count = 0
# logs = [
#     "2026-11-25 10:15:20 ERROR Database connection failed",
#     "2026-11-25 10:16:30 INFO Application started",
#     "2026-11-25 10:17:45 WARNING CPU usage reached 85%",
#     "2026-11-25 10:18:10 ERROR Connection timeout",
#     "2026-11-25 10:19:20 ERROR Disk failure"
# ]

# for line in logs:
#     error_1 = re.search(r"ERROR", line)
    
#     if error_1:
#         error_count += 1
#         error_logs.append(line)
# print(f"Total ERROR count: {error_count}")
# print(f"ERROR LOGS:\n{'\n'.join(error_logs)}")

# Task 2 — Extract IP addresses from production logs
# import re 
# ip_addresses = []

# logs = [
#     "2026-11-25 10:15:20 ERROR Connection failed from 10.0.1.25",
#     "2026-11-25 10:16:30 INFO Application started",
#     "2026-11-25 10:17:45 WARNING Request from 192.168.1.10",
#     "2026-11-25 10:18:10 ERROR Timeout from 172.16.0.5",
#     "2026-11-25 10:19:20 ERROR Failed connection from 10.0.1.25"
# ]

# for line in logs:
#         ip_addresses.extend(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))

# print(f"Total Number of IPs: {len(ip_addresses)}")
# print(f"List of unique IPs:\n{set(ip_addresses)}")

# Task 3: IP Frequency Analysis.
# import re
# ip_addresses = []
# ip_frequency = {}
# logs = [
#     "2026-11-25 10:15:20 ERROR Connection failed from 10.0.1.25",
#     "2026-11-25 10:16:30 INFO Application started",
#     "2026-11-25 10:17:45 WARNING Request from 192.168.1.10",
#     "2026-11-25 10:17:45 WARNING Request from 192.168.1.10",
#     "2026-11-25 10:18:10 ERROR Timeout from 172.16.0.5",
#     "2026-11-25 10:19:20 ERROR Failed connection from 10.0.1.25",
#     "2026-11-25 10:20:10 ERROR Connection refused from 192.168.1.10",
#     "2026-11-25 10:21:10 INFO Request completed from 10.0.1.25"
# ]

# for line in logs:
#     ip_addresses.extend(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line))

# for ip in ip_addresses:
#     if ip in ip_frequency:
#         ip_frequency[ip] += 1
#     else:
#         ip_frequency[ip] = 1
        
# max_occurance = max(ip_frequency, key=ip_frequency.get)
# occurance_count = ip_frequency[max_occurance]

# print(ip_addresses)
# print(f"IP Frequency Report:\n{ip_frequency}")
# print(f"Most Frequent occuring IP:{max_occurance}\nOccurance Count:{occurance_count}  ")

# print(f"Checking IPS with same number of max occurance  count {occurance_count}")
# for ip in ip_frequency:
#     if ip_frequency[ip] == occurance_count:
#         print(ip)

# Task 4: Production Log Pattern Extraction.
# import re
# logs = [
#     "2026-11-26 09:15:20 ERROR Database connection failed",
#     "2026-11-26 09:16:30 INFO Application started",
#     "2026-11-26 09:17:45 WARNING CPU usage reached 85%",
#     "2026-11-26 09:18:10 ERROR Connection timeout",
#     "2026-11-26 09:19:20 ERROR Disk failure detected",
#     "2026-11-26 09:20:10 INFO Health check completed"
# ]



# error_reports = []


# for line in logs:
#     pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+ERROR\s+(.+)"

#     match = re.search(pattern, line)

#     if match:
#         time_stamp = match.group(1)
#         error_message = match.group(2)
#         error_reports.append({
#     "timestamp": time_stamp,
#     "error": error_message
# })
# print("PRODUCTION ERROR REPORT\n")

# for report in error_reports:
#     print(f"Timestamp: {report['timestamp']}")
#     print(f"Error: {report['error']}\n")

# print(f"Total Errors: {len(error_reports)}")   

# Task - Final Build a Production Log Analyzer
import re 


logs = [
    "2026-11-26 09:15:20 ERROR Database connection failed from 10.0.1.25",
    "2026-11-26 09:16:30 INFO Application started from 192.168.1.10",
    "2026-11-26 09:17:45 WARNING CPU usage reached 85% from 10.0.1.25",
    "2026-11-26 09:18:10 ERROR Connection timeout from 172.16.0.5",
    "2026-11-26 09:19:20 ERROR Disk failure detected from 10.0.1.25",
    "2026-11-26 09:20:10 INFO Health check completed from 192.168.1.10",
    "2026-11-26 09:21:10 WARNING Memory usage reached 90% from 192.168.1.10"
]
print("========== PRODUCTION LOG ANALYZER ==========")
error_report = []
total_log_count = 0
error_count = 0
warning_count = 0
info_count = 0
pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(ERROR|WARNING|INFO)\s+(.+)" 

for line in logs:
    #  Extract ERROR, WARNING and INFO counts dynamically

    match = re.search(pattern, line)
    if match:
        total_log_count += 1
        time_stamp = match.group(1)
        log_level = match.group(2)
        message = match.group(3)
        if log_level == "ERROR":
            error_count += 1
        elif log_level == "WARNING":
            warning_count += 1
        else:
            info_count += 1
        # Capturing ERROR INCIDENT DETAILS
        if log_level == "ERROR":
            error_report.append({
    "timestamp": time_stamp,
    "error": message
})
       
print(f"Total Log Entries:{total_log_count}\n")
print(f"LOG LEVEL SUMMARY:\n---------------------\nERROR: {error_count}\nWARNING: {warning_count}\nINFO: {info_count}\n")

# IP ADDRESS FREQUENCY

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ip_frequency = {}

# gathering IP address in log
for line in logs:
    ips = re.findall(ip_pattern, line)

# getting the frequency

    for ip in ips:
        if ip in ip_frequency:
            ip_frequency[ip] += 1
        else:
            ip_frequency[ip] = 1    
max_occurance = max(ip_frequency, key=ip_frequency.get)
occurance_count = ip_frequency[max_occurance]  

print("IP ADDRESS FREQUENCY:\n---------------------")   
for ip in ip_frequency:
    #IP ADDRESS FREQUENCY
    print(f"{ip}: {ip_frequency[ip]}")  
print(f"\nMOST FREQUENT IP:\n-----------------------")
for ip in ip_frequency:
    # MOST FREQUENT IP
    if ip_frequency[ip] == occurance_count:
        print(ip)

print("\nERROR INCIDENT DETAILS:\n-----------------------")

for report in error_report:
    print(f"Timestamp: {report['timestamp']}")
    print(f"Error: {report['error']}\n")




# --------------------Q & A------------------------
# What is Regex, and why do we use it in Python?
# Regex is nothing but Regular expression , which is used to search , match, extract and replace matching object

# What is the difference between re.search() and re.match()?
# re.search () - Finds the first matching anywhere 
# re.match() - checks for teh matches at begining

# What is the difference between re.findall() and re.finditer()?
# re.findall() - returns all matches as a list
# re.finditer() - returns an iterator of matches

# What does \d+ mean?
# \d+ - matches one or more  digit


# Why do we use raw strings such as r"\d+"?
#A raw string tells Python not to interpret backslashes as Python string escape sequences.
# "We use raw strings for Regex patterns because they prevent Python from interpreting backslashes as string escape sequences before the Regex engine processes them." 

# Why does set() reject a list of lists?
# - A Python set can contain only hashable objects.
# - Strings are immutable and hashable, so they can be stored in sets.
# - Lists are mutable and unhashable, so they cannot be elements of a set.
# - A nested list is still a list, so it also produces TypeError: unhashable type: 'list'.
# Interview-ready answer:

# "A Python set stores only hashable elements. Strings are immutable and hashable, whereas lists are mutable and unhashable. Therefore, a set can contain strings but cannot contain lists or nested lists."

# What is the difference between a capturing group () and a non-capturing group (?:)?
# capturing group () - Multiple patterns assigned to  one variable and match whicever required 
# non-capturing group (?:) - single pattern search 

# What does group(0) return compared with group(1)?
# group(0) - will return entire pattern
# group(1) - will return only the first pattern match

# Why should you check if match: before accessing match.group()?
# re.search() returns None when the pattern doesn't match the line. Therefore, calling match.group(1) causes an AttributeError.

# What is the difference between re.findall() and re.finditer()?
# re.findall() - returns all matches as a list
# re.finditer() - returns an iterator of matches

# How would you optimize IP frequency analysis for a very large log file?
# For large log files, I would process the file line by line rather than loading the entire file into memory. I would extract IP addresses and update a frequency dictionary directly instead of storing all IP addresses in a separate list. This reduces memory consumption while maintaining O(n) processing time, where n is the number of extracted IP addresses.


# How would you validate an IP address beyond simply matching its pattern?
# Regex can identify strings that resemble IP addresses, but it doesn't necessarily validate their numerical ranges. I would use Python's built-in ipaddress module to validate whether an address is a valid IPv4 or IPv6 address. Invalid addresses raise a ValueError.
# import ipaddress

# ip = "10.0.1.25"

# try:
#     validated_ip = ipaddress.ip_address(ip)
#     print("Valid IP address")
# except ValueError:
#     print("Invalid IP address")