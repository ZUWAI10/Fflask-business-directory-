# models.py
from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.timestamp = datetime.now()

class ClinicQueue:
    def __init__(self):
        self.queue = []

 s   # Add patient (FIFO)
    def register_patient(self, patient):
        self.queue.append(patient)

    # Remove patient
    def see_patient(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    # Get waiting list
    def waiting_list(self):
        return [p.name for p in self.queue]

    # Total patients seen today
    def total_seen(self):
        return len(self.queue)