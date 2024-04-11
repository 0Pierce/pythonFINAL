import tkinter as tk
import paho.mqtt.client as mqtt
import json

class SubscriberGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Subscriber")
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("localhost", 1883, 60)
        self.client.subscribe("test/topic")
        self.setup_gui()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))


    #Process data
    def on_message(self, client, userdata, msg):
        data = json.loads(msg.payload)

        print(f"Received data: {data}")


    #Do GUI stuff here
    def setup_gui(self):


        pass

if __name__ == "__main__":
    root = tk.Tk()
    gui = SubscriberGUI(root)
    root.mainloop()
