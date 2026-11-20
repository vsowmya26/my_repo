# Task 2 — Create the memory module
def check_memory(memory_usage, threshold=85):
    if memory_usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"
        
if __name__ == "__main__":
    print(check_memory(80))