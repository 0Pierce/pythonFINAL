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
        #Example parameters should be changed and set in GUI by user
        self.value_generator = DataGen(10, 50, 10)
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)
        self.setup_gui()

    def setup_gui(self):

        firstlbl = tk.Label(root, text="Hewwo", bd=5, padx=20, pady=20)
        firstButton = tk.Button(root, text='Load Data.', bd=10, fg="blue")

        firstButton.pack()
        pass



    def get_data(self):
        print("test")


    def send_data(self):
        value = self.value_generator.generate_value()
        package = self.value_generator.package_value(value)
        self.client.publish("test/topic", package)

        if random.random() < 0.01:
            return
        self.client.loop()





if __name__ == "__main__":
    root = tk.Tk()
    gui = PublisherGUI(root)
    root.mainloop()
