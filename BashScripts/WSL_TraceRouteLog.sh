#!/bin/bash

# Pre-determined URL or IP address
DESTINATION="127.0.0.1"
LOG_FILE="traceroute_log.csv"

# Get the current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Get the source IP address. 
SOURCE_IP=$(hostname -I | awk '{print $1}')

# Check if the log file exists, and create it with headers if it does not
if [ ! -f "$LOG_FILE" ]; then
    echo "Timestamp,Source IP,Destination,Amount of Hops,RTT,IP Addresses" > "$LOG_FILE"
fi

# Perform traceroute and capture output
TRACEROUTE_OUTPUT=$(traceroute -I $DESTINATION)

# Extract data from the traceroute output
# Placeholder for data extraction logic
HOPS=$(echo "$TRACEROUTE_OUTPUT" | wc -l)
# RTT and IP extraction
RTT=$(echo "$TRACEROUTE_OUTPUT" | tail -n 1 | awk '{print $4}' | tr -d 'ms')
IP_ADDRESSES=$(echo "$TRACEROUTE_OUTPUT" | grep -oP '\(\K[^\)]+')

# Log the extracted data to the CSV file
echo "$TIMESTAMP,$SOURCE_IP,$DESTINATION,$HOPS,$RTT,$IP_ADDRESSES" >> "$LOG_FILE"

echo "Traceroute data logged to $LOG_FILE"
