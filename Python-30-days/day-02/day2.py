cpu_usage = 92
cpu_threshold = 80
memory_usage = 88
memory_threshold = 85
disk_usage = 75
disk_threshold = 90
server_status = True
server_status_threshold = "Must be True"

print("===== PRODUCTION SERVER HEALTH =====")
print(f"CPU Usage: {cpu_usage}%")
print(f"CPU High: {cpu_usage > cpu_threshold}")
print(f"Memory Usage: {memory_usage}%")
print(f"Memory High: {memory_usage > memory_threshold}")
print(f"Disk Usage: {disk_usage}%")
print(f"Disk High: {disk_usage > disk_threshold}")
print(f"Server Status: {server_status}")
print(f"Server Status High: {server_status is True}")
#-------------------------------------------------
cpu_usage = 90
threshold = 80

alert = cpu_usage > threshold

print(alert)
#-------------------------------------------------
cpu_usage = 95
memory_usage = 50

alert = cpu_usage > 90 or memory_usage > 90

print(alert)

#-------------------------------------------------
disk_capacity = 100
disk_used = 75

disk_utlisation = disk_used / disk_capacity * 100

print(f"Disk Utilisation: {disk_utlisation}%")
#-------------------------------------------------
# 1. What is the difference between / and // in Python?
# / peforms division and returns a float, while // performs floor division and returns an integer. For example, 5 / 2 would return 2.5, while 5 // 2 would return 2.
# 2. What does the % operator do? Give an SRE-related example.
# The % operator performs the modulo operation, returning the remainder of a division. For example, 10 % 3 would return 1.
# 3. What is the difference between = and ==?
# = is the assignment operator, used to assign a value to a variable. == is the equality operator, used to compare two values for equality.
# 4. What is the difference between and and or?
# and returns True if both operands are True, while or returns True if at least one operand is True.
# 5. What does the not operator do?
# The not operator negates the boolean value of an expression.
# 6. What is the difference between is and ==?
# is checks for object identity (whether two variables refer to the same object in memory), while == checks for equality of values.   
# 7. How would you check whether CPU usage exceeds 80%?  
# You would check whether CPU usage exceeds 80% by using a comparison operator like this: `cpu_usage > 80`. If `cpu_usage` is greater than 80, the expression will return True; otherwise, it will return False.  
# 8. If CPU is 95% and memory is 60%, what will the expression cpu > 90 and memory > 90 return? Why?
# It returns False because the first condition `cpu > 90` is True, but the second condition `memory > 90` is False. Since the `and` operator requires both conditions to be True for the overall expression to be True, the result is False.
# 9. Why are comparison operators useful in monitoring and alerting?
# Comparison operators are useful in monitoring and alerting because they allow you to evaluate system metrics against predefined thresholds. By using comparison operators, you can determine if a metric exceeds a certain limit (e.g., CPU usage > 80%) and trigger alerts or notifications when those conditions are met. This helps in proactive monitoring of system health and performance, enabling timely interventions to prevent issues.
# 10. What is operator precedence?
# Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before those with lower precedence. For example, in the expression `3 + 4 * 2`, the multiplication operator `*` has higher precedence than the addition operator `+`, so the multiplication is performed first, resulting in `3 + 8`, which equals `11`. Understanding operator precedence is important to ensure that expressions are evaluated as intended.

#---------------------------------------------------------------------------------------------