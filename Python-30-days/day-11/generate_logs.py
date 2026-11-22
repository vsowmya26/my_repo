with open("c:/Users/navee/Documents/Github_sowmya/my_repo/Python-30-days/day-11/large_server.log", 'x') as file:
    file.writelines('''2026-11-20 09:00:01 INFO nginx service started
2026-11-20 09:00:02 WARNING CPU usage reached 82%
2026-11-20 09:00:03 ERROR database connection failed
'''*100000)
    
