# Task 3 — Create the disk module.
def check_disk(disk_usage, threshold=90):
    if disk_usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"
        
if __name__ == "__main__":
    print(check_disk(80))