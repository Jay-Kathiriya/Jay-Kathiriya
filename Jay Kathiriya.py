import csv
import os
from datetime import datetime

# Appointment types
APPT_TYPES = {
    0: 'Available',
    1: 'Mens Cut $50',
    2: 'Ladies Cut $80',
    3: 'Mens Colouring $50',
    4: 'Ladies Colouring $120'
}

# Define the Appointment class
class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.client_name = ''
        self.client_phone = ''
        self.appt_type = 0  # 0 represents 'Available'
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour

    def schedule(self, client_name, client_phone, appt_type):
        self.client_name = client_name
        self.client_phone = client_phone
        self.appt_type = appt_type

    def cancel(self):
        self.client_name = ''
        self.client_phone = ''
        self.appt_type = 0

    def is_scheduled(self):
        return self.appt_type != 0

    def __str__(self):
        return f"{self.client_name:20}{self.client_phone:15}{self.day_of_week:10}" \
               f"{self.start_time_hour:02}:00 - {self.start_time_hour+1:02}:00" \
               f"{APPT_TYPES[self.appt_type]}"

def create_weekly_calendar():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    calendar = [Appointment(day, hour) for day in days for hour in range(9, 17)]
    return calendar

def load_appointments(calendar):
    while True:
        filename = input('Enter appointment filename: ')
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    for appt in calendar:
                        if appt.day_of_week == row[3] and int(appt.start_time_hour) == int(row[4]):
                            appt.schedule(row[0], row[1], int(row[2]))
            print("Appointments loaded successfully!")
            break  # Exit the loop if loading is successful
        else:
            print(f"File not found: {filename}. Please enter a valid filename.")