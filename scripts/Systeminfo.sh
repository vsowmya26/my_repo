#!/bin/bash

cpu_utilisation=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')

Memory_utilisation=$(free)

Disk_Space=$(df -h)

echo "-----Here is teh System infor on CPU , Memeory and Disk utilisation------------------"


echo "CPU : $cpu_utilisation
      Memory : $Memory_utilisation
      Disk : $Disk_Space "
