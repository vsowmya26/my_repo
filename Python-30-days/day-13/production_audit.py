# Task 5: Production Infrastructure Audit Capstone
import json
import csv
prod_server_list = []
unhealthy_server_list = []

try:
    with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/server_inventory.json",'r') as file_json_read:
        inventory = json.load(file_json_read)

        for server in inventory:
            reason = []
            if server["environment"] == "production" :
                prod_server_list.append(server["server_name"])
                if server["status"] == "unkown":
                    server["severity"] = "UNKOWN"
                elif server["status"] == "stopped":
                    server["severity"] = "MAINTENANCE"
                    reason.append("Server status is stopped")
                else:
                    if  server["status"] == "running":
                        if server["cpu"] > 95 or server["memory"] > 95 or server["disk"] > 95:
                            server["severity"] = "CRITICAL"
                        elif server["cpu"] > 80 or server["memory"] > 85 or server["disk"] > 90:
                            server["severity"] = "WARNING"
                        else:
                            server["severity"] = "HEALTHY"
    
                        if server["cpu"] > 80:
                            reason.append("CPU above 80%") 
    
                        if server["memory"] > 85:
                            reason.append("Memory above 85%")
    
                        if server["disk"] > 90:
                            reason.append("Disk above 90%")


                server["reason"] = ", ".join(reason)

                if reason:
                    unhealthy_server_list.append(server)


        print(f"Total number of servers: {len(inventory)}")
        print(f"Production_server list:\n{'\n'.join(prod_server_list)}")
        print(unhealthy_server_list)

except FileNotFoundError as f:
    print(f"Failed Reading file due to  {f}")

except json.JSONDecodeError as j:
    print(f"Failed Reading file due to  {j}")

else:
    print("Reading json file successful, proceeding with csv report generation")
    try:
        with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-13/production_audit_report.csv",'w',newline="") as file_csv:
        
                fieldnames = ["server_name","environment","cpu","memory","disk","status","severity","reason"]
                writer = csv.DictWriter(file_csv, fieldnames=fieldnames )
                writer.writeheader()
                writer.writerows(unhealthy_server_list)
    except PermissionError as p:
        print(f"Failed writing file due to {p}")
    else:
        print("File write successful")
finally:
    print("production audit file preparation activity completed")