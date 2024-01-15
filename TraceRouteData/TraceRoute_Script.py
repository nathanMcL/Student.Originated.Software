#!/usr/bin/env python3

import subprocess
import re
import csv
import platform
from datetime import datetime
import numpy as np
import os


def perform_traceroute(destination):
    # Determine the command based on the operating system
    command = "tracert" if platform.system().lower() == "windows" else "traceroute"

    # Execute the traceroute command
    result = subprocess.run([command, destination], capture_output=True, text=True)

    return result.stdout


def parse_traceroute_output(output):
    # Regular expression to extract round-trip times
    regex = r'\d+\s+ms' if platform.system().lower() == "windows" else r'\d+\.\d+\s+ms'

    # Find all round-trip times
    times = re.findall(regex, output)

    # Convert times to float and calculate the number of routers
    times = [float(time.split()[0]) for time in times]
    num_routers = len(set(re.findall(r'\d+\s+ms', output))) if times else 0

    # Calculate average and standard deviation
    avg_delay = np.mean(times) if times else 0
    std_dev = np.std(times) if times else 0

    return num_routers, avg_delay, std_dev


def write_to_csv(data, filename="traceroute_data.csv"):
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0
    # Write the data to a CSV file
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the headers
        if not file_exists:
            headers = ["Hour", "Destination", "Num_Routers", "Avg_Delay", "Std_Dev"]
            writer.writerow(headers)

        writer.writerow(data)


# Main Execution
if __name__ == "__main__":
    destination = "google.com"
    hour = datetime.now().strftime("%H:%M:%S")

    output = perform_traceroute(destination)
    num_routers, avg_delay, std_dev = parse_traceroute_output(output)

    # Prepare data for CSV
    csv_data = [hour, destination, num_routers, avg_delay, std_dev]

    # Write to CSV
    write_to_csv(csv_data)
