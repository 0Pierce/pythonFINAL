import random
import json
import time

class DataGen:
    def __init__(self, min_value, max_value, pattern_interval):
        self.min_value = min_value
        self.max_value = max_value
        self.pattern_interval = pattern_interval

    def update_parameters(self, min_value, max_value, pattern_interval):
        self.min_value = min_value
        self.max_value = max_value
        self.pattern_interval = pattern_interval

    def generate_value(self):
        value = random.randint(self.min_value, self.max_value)
        if time.time() % self.pattern_interval == 0:
            value += 1
        return value

    def package_value(self, value):
        package = {
            "timestamp": time.time(),
            "packet_id": random.randint(1000, 9999),
            "value": value
        }
        return json.dumps(package)
