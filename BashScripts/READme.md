---
Bash Scripts
---



---
Windows Subsystem for Linux (WSL) scripts:
---

# SystemLog.sh Script Documentation
![Screenshot (459)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/71679da8-0a71-498b-be04-9058162748b5)

## The SystemLog.sh
This bash script is designed to run within the WSL environment.<br>Its primary function is to collect and log various system metrics to a CSV file named `WSL_os_log.csv`.<br>

## How it works

1. Checks if the `WSL_os_log.csv` log file exists. If not, it creates the file and initializes it with a header row.
2. Collects a variety of system metrics including CPU usage, memory usage, disk usage, available disk space, and more.
3. Outputs a confirmation message indicating the data has been successfully logged.


## CSV File Structure
The CSV file `WSL_os_log.csv` contains the following headers:

- **OS Name**: The name of the operating system running within WSL.
- **Date Time**: The timestamp, formatted as `YYYY-MM-DD HH:MM:SS`.
- **CPU Usage**: The percentage of CPU utilization at the time of logging.
- **Memory Usage**: The percentage of memory usage, calculated as the ratio of used memory to total memory.
- **Disk Usage**: The percentage of disk space used on the root filesystem.
- **Available Disk**: The amount of available disk space on the root filesystem.
- **System Load Average**: Averages of the number of processes in the system run queue over the last 1, 5, and 15 minutes.
- **Number of Processes**: The total number of processes running at the time of logging.
- **Uptime**: The total uptime of the system in seconds at the time of logging.

## Usage
To use the `SystemLog.sh` script, ensure you have WSL installed and configured on your Windows system.<br> Navigate to the directory containing `SystemLog.sh`,<br> then execute the script by running:

```bash
chmod +x SystemLog.sh
then enter:
./SystemLog.sh
```


This README provides a basic overview, details of the script's functionality,<br> the structure of the log file, and a brief guide on how to use the script.<br> You should adjust the file paths, URLs, and any specific instructions according to your project's setup and requirements.

