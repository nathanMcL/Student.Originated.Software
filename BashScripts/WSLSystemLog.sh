#!/bin/bash

# Fixed log file name
LOG_FILE="WSL_os_log.csv"

# Insert a blank line after every third log entry
LINE_COUNT=$(wc -l < "$LOG_FILE" 2>/dev/null || echo "0") # Get the current line count or default to 0 if the file doesn't exist
((LINE_COUNT++)) # Increment line count for this entry
INSERT_BLANK_LINE_AFTER=4 # Insert a blank line after every 4 log entries

# Check if the log file exists, and create it with headers if it does not
if [ ! -f "$LOG_FILE" ]; then
    echo "OS Name,Date Time,CPU Usage,Memory Usage,Disk Usage,Available Disk,System Load Average,Number of Processes,Uptime" > "$LOG_FILE" 
    LINE_COUNT=1
fi

# The Operating System name
OS_NAME=$(cat /etc/os-release | grep PRETTY_NAME | awk -F= '{print $2}' | tr -d '"')

# Time and Date
DATE_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# CPU usage calculation 
read cpu a b c idle rest < /proc/stat
CPU_USAGE=$(awk "BEGIN {print ($a+$b+$c) / ($a+$b+$c+$idle) * 100}")

# Memory usage calculation 
MEM_USAGE=$(free -m | awk '/Mem:/ {print ($3-$7)/$2 * 100.0}')

# Disk usage calculation 
DISK_USAGE=$(df -h / | awk '/\/$/ {print $5}')

# Available Disk space
AVAILABLE_DISK=$(df -h / | awk '/\/$/ {print $4}')

# System Load Average
LOAD_AVERAGE=$(cat /proc/loadavg | awk '{print $1", "$2", "$3}')

# Number of processes running
NUM_PROCESSES=$(ps aux | wc -l)

# Uptime
UPTIME=$(awk '{print $1}' /proc/uptime)

# Adjusted log data to CSV file to exclude unavailable data
{
    echo "$OS_NAME,$DATE_TIME,$CPU_USAGE,$MEM_USAGE,$DISK_USAGE,$AVAILABLE_DISK,$LOAD_AVERAGE,$NUM_PROCESSES,$UPTIME"
    # Check if we need to insert a blank line
    if ((LINE_COUNT % INSERT_BLANK_LINE_AFTER == 0)); then
        echo ""
    fi
} >> "$LOG_FILE"

echo "Log saved to $LOG_FILE"
