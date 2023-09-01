import psutil
import tkinter as tk
from tkinter import Label


class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        font_style = ("Helvetica", 12, "bold")

        self.cpu_label = Label(root, text="CPU Usage:", font=font_style, width=30)
        self.cpu_label.pack()

        self.memory_label = Label(root, text="Memory Usage:", font=font_style)
        self.memory_label.pack()

        self.disk_label = Label(root, text="Disk Usage:", font=font_style)
        self.disk_label.pack()

        self.update_labels()

    def get_system_performance(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        return cpu_usage, memory_usage, disk_usage

    def update_labels(self):
        cpu_usage, memory_usage, disk_usage = self.get_system_performance()

        self.cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage:.2f}%")
        self.disk_label.config(text=f"Disk Usage: {disk_usage:.2f}%")

        self.root.after(5000, self.update_labels)  # Update every 5 seconds


def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# This is a simple system monitor application built using Python's psutil library and the Tkinter framework. 
# It provides real-time information on CPU usage, memory usage, and disk usage.
# Usage
# Once the application is running, you will see a window displaying the following information:

# CPU Usage: Shows the current CPU usage as a percentage.
# Memory Usage: Displays the current memory (RAM) usage as a percentage.
# Disk Usage: Shows the current disk usage as a percentage for the root directory.
# The information is updated every 5 seconds to provide real-time data on your system's performance.
