import csv
import os
import psutil  # type: ignore
import GPUtil  # type: ignore
import time
from datetime import datetime


class GPTSystemLogger:
    def __init__(self, filename="GPT_OS_system_log.csv"):
        self.filename = filename
        self.fieldnames = ["Event", "Name", "Date & Time", "Available RAM (GB)", "Available Memory (%)", "GPU Name", "GPU Memory (MB)", "Temperature (C / F)"]
        self.init_csv()
        self.temperature_celsius = []

    def init_csv(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()

    def log_system_stats(self, event):
        stats = self.get_system_stats()
        stats["Event"] = event
        self.write_to_csv(stats)

    def get_system_stats(self):
        mem = psutil.virtual_memory()
        gpus = GPUtil.getGPUs()
        gpu_info = gpus[0] if gpus else None
        gpu_name = gpu_info.name if gpu_info else "N/A"
        gpu_memory = gpu_info.memoryFree if gpu_info else "N/A"
        gpu_temp_c = gpu_info.temperature if gpu_info else "N/A"
        gpu_temp_f = (gpu_temp_c * 9/5) + 32 if gpu_temp_c != "N/A" else "N/A"
        if gpu_temp_c != "N/A":
            self.temperature_celsius.append(gpu_temp_c)

        stats = {
            "Name": os.name,
            "Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Available RAM (GB)": round(mem.available / (1024 ** 3), 2),
            "Available Memory (%)": mem.percent,
            "GPU Name": gpu_name,
            "GPU Memory (MB)": gpu_memory,
            "Temperature (C / F)": f"{gpu_temp_c} / {gpu_temp_f}"
        }
        return stats

    def write_to_csv(self, stats):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writerow(stats)

    def log_before_training(self):
        self.log_system_stats("Before Training")

    def log_during_training(self, epoch):
        if epoch % 5 == 0:
            self.log_system_stats(f"During Training (Epoch {epoch})")

    def log_after_training(self):
        avg_temp_c = sum(self.temperature_celsius) / len(self.temperature_celsius) if self.temperature_celsius else "N/A"
        avg_temp_f = (avg_temp_c * 9/5) + 32 if avg_temp_c != "N/A" else "N/A"
        stats = self.get_system_stats()
        stats["Event"] = "After Training"
        stats["Temperature (C / F)"] = f"{avg_temp_c} / {avg_temp_f}"
        self.write_to_csv(stats)
        self.write_blank_line()

    def write_blank_line(self):
        with open(self.filename, mode='a', newline='') as file:
            file.write('\n')

if __name__ == "__main__":
    system_logger = GPTSystemLogger()
    system_logger.log_before_training()

    for epoch in range(1, 21):
        time.sleep(1)
        system_logger.log_during_training(epoch)
    system_logger.log_after_training()