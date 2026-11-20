# Task 1 — Create the CPU module
def check_cpu(cpu_usage, threshold=80):
    if cpu_usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"

if __name__ == "__main__":
    print(check_cpu(80))