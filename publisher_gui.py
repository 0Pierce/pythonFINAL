import tkinter as tk
from random import random
from tkinter import messagebox
from data_gen import DataGen
import paho.mqtt.client as mqtt

class PublisherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Publisher")
        root.geometry("600x400")
        # Example parameters should be changed and set in GUI by user

        self.value_generator = DataGen(10, 50, 10)
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)
        self.setup_gui()

    def setup_gui(self):
        # Parameter inputs
        self.min_value_entry = tk.Entry(self.root)
        self.max_value_entry = tk.Entry(self.root)
        self.pattern_interval_entry = tk.Entry(self.root)

        # Shows generated data
        self.generated_data_label = tk.Label(self.root, text="Generated Data: ")

        # Current parameters
        self.min_value_label = tk.Label(self.root, text="Min Value: ")
        self.max_value_label = tk.Label(self.root, text="Max Value: ")
        self.pattern_interval_label = tk.Label(self.root, text="Pattern Interval: ")

        # Buttons
        self.update_params_button = tk.Button(self.root, text='Update Parameters', command=self.update_parameters)
        self.send_data_button = tk.Button(self.root, text='Send Data', command=self.send_data)

        # Packing widgets
        self.min_value_entry.pack()
        self.max_value_entry.pack()
        self.pattern_interval_entry.pack()
        self.update_params_button.pack()
        self.send_data_button.pack()
        self.generated_data_label.pack()
        self.min_value_label.pack()
        self.max_value_label.pack()
        self.pattern_interval_label.pack()

    def update_parameters(self):
        min_value = int(self.min_value_entry.get())
        max_value = int(self.max_value_entry.get())
        pattern_interval = int(self.pattern_interval_entry.get())
        self.value_generator.update_parameters(min_value, max_value, pattern_interval)
        # Update labels to reflect new values
        self.min_value_label.config(text=f"Min Value: {min_value}")
        self.max_value_label.config(text=f"Max Value: {max_value}")
        self.pattern_interval_label.config(text=f"Pattern Interval: {pattern_interval}")

    def send_data(self):
        value = self.value_generator.generate_value()
        package = self.value_generator.package_value(value)
        self.client.publish("test/topic", package)
        self.generated_data_label.config(text=f"Generated Data: {package}")
        self.client.loop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = PublisherGUI(root)
    root.mainloop()
