class Drone:

    def __init__(self, model, battery, status):
        self.model = model
        self.battery = battery
        self.status = status

    def is_ready(self):
        return self.battery >= 40 and self.status == "Idle"

    def __str__(self):
        return f"{self.model} ({self.battery}%) - {self.status}"
