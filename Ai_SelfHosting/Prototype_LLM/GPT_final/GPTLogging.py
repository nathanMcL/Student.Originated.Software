import csv
import time
import os


class GPTLogging:
    def __init__(self, log_file):
        self.log_file = log_file
        self.epoch_times = []
        self.log_headers = [
            "Epoch", "Total Steps", "Avg Training Loss", "Avg Validation Loss", "Time per Epoch (seconds)", "Generated Sentence"
        ]

        # Create the log files and write the headers
        if not os.path.isfile(self.log_file):
            with open(self.log_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.log_headers)

    def start_epoch(self):
        self.epoch_start_time = time.time()

    def end_epoch(self, epoch, total_steps, avg_train_loss, avg_val_loss, generated_sentence):
        epoch_end_time = time.time()
        epoch_duration = epoch_end_time - self.epoch_start_time
        self.epoch_times.append(epoch_duration)

        avg_epoch_time = sum(self.epoch_times) / len(self.epoch_times)

        # Log the data to CSV
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                epoch, total_steps, avg_train_loss, avg_val_loss, avg_epoch_time, generated_sentence
            ])