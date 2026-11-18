# logs = [
#     "INFO: nginx service started successfully",
#     "ERROR: nginx service failed",
#     "WARNING: high memory usage detected",
#     "ERROR: database connection timeout",
#     "INFO: application health check passed",
#     "ERROR: payment service unavailable"
# ]

# ERROR_count = 0
# WARNING_count = 0
# INFO_count = 0

# for log in logs:
#     if "ERROR" in log:
#         ERROR_count += 1
#     elif "WARNING" in log:
#         WARNING_count += 1
#     elif "INFO" in log:
#         INFO_count += 1

# print(f"ERROR: {ERROR_count}")
# print(f"WARNING: {WARNING_count}")
# print(f"INFO: {INFO_count}")

# #----------------------------------------------------------
# service_names = [
#     " NGINX ",
#     "Apache",
#     " MYSQL ",
#     "redis",
#     " POSTGRES "
# ]

# for service in service_names:
#     service = service.strip().lower()
#     print(service)

# #----------------------------------------------------------
# log_message = "2026-11-18 ERROR prod-api-01 payment service failed"

# print(f"Date: {log_message.split()[0]}")
# print(f"Log Level:{log_message.split()[1]}")
# print(f"Server: {log_message.split()[2]}")
# print(f"Message: {' '.join(log_message.split()[3:])}")

# #----------------------------------------------------------

# log_message = "ERROR: nginx service failed"

# if "ERROR" in log_message and "nginx" in log_message and log_message.endswith("failed"):
#     print("Alert: NGINX service failure detected!")

# #----------------------------------------------------------
# # What is the difference between strip() and replace() in Python?
# #strip() - method to remove trailing whitespace
# #replace() - method to replace a substring with another substring

# # What is the difference between find() and the in operator?
# # find() - method to find the index of a substring in a string, returns -1 if not found
# # in operator - checks if a substring exists in a string, returns True or False

# # Why are strings immutable in Python?
# # Strings are immutable in Python because they are designed to be hashable and can be used as keys in dictionaries.

