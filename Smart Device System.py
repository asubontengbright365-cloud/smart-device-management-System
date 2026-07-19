import random


class SmartDevice:
    def __init__ (self, __device_id, name):
        self.__device_id = device_id    # private attribute
        self.__power_status = False   # private attribute
        self.Name = name  #public attribute

# Getters using the @property decorator to control access to the private attribute
@property
def device_id(self):
        return self.__device_id
@property
def power_status(self):
    if self.__power_status == True:
        return "True"
    else:
        return "False"

# setter with validation
@power_status.setter
def power_status(self, status):
    if isinstance(status, bool):
        self.__power_status = status
    else:
        print("Error power status must be True or False")

def turn_on(self):
        self.__power_status = True
        print(self.Name + "is turned on ")

def turn_off(self):
        self.__power_status = False
        print(self.Name + "is turned off ")

def display_info(self):
    print(f"Name: {self.Name}")
    print(f"Device ID: {self.device_id}")
    print(f"Power Status: {self.power_status}")


#inheritance: child class 1
class TemperatureSensor(SmartDevice):
    def __init__(self, __device_id, name, temperature = 0.0):
        super().__init__(device_id, name)
        self.temperature = temperature

#Additional attribute for Temperature Sensor
    def read_temperature(self):
            self.temperature = round(random.uniform(18.5, 31.0), 1)
            print(f"{self.Name} current temperature: {self.temperature} Celsius")


#inheritance class 2
class SmartLight(SmartDevice):
    def __init__(self, __device_id, name, brightness =0):
        super().__init__(device_id, name)   #To call parent constructor
        self.__brightness = brightness #0-100

#Encapsulation for brightness
    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, value):
        if 0<= value <= 100:
            self.__brightness = value
        else:
            print("Error brightness must be between 0 and 100")

    def increase_brightness(self, amount=10):
        new_brightness = self.__brightness + amount
        self.brightness = min(100, new_brightness)
        print(f"{self.Name} brightness was to {self.brightness}")

    def decrease_brightness(self, amount=10):
        new_brightness = self.__brightness - amount
        self.brightness = max(0, new_brightness)
        print(f"{self.Name} brightness was decreased to {self.brightness}")


#inheritance class 3 with encapsulation
class SecurityCamera(SmartDevice):
    def __init__(self, __device_id, name, recording_status=False):
        super().__init__(device_id, name)
        self.recording_status = recording_status

    def start_recording(self):
        self.recording_status = True
        print(f"{self.Name} has started recording")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.Name} has stopped recording")

def main():
    temp_Sensor = TemperatureSensor ("FE-00-24", "Room Temperature Sensor")
    smart_light = SmartLight ("DS-76-01", "Room Automated Light")
    security_camera = SecurityCamera ("GF-97-34", "Room Security Camera")

    devices = [temp_Sensor, smart_light, security_camera]
#Menu Interface
    while True:
        print("\n                   SMART DEVICE MANAGEMENT SYSTEM               ")
        print("1. Display Device Information")
        print("2. Turn On")
        print("3. Turn Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start Recording")
        print("7. Exit")

        choice = int(input("Enter your choice(1-7): "))
        if choice == 1:
            print("\n **** Device Information ****")
            for device in devices:
                device.display_info()

        elif choice == 2:
            for device in devices:
                device.turn_on()

        elif choice == 3:
            for device in devices:
                device.turn_off()

        elif choice == 4:
            for device in devices:
                device.display_info()

        elif choice ==5:
            action = input("Enter '>' to increase or '<' to decrease brightness: ")
            if action =='>':
                smart_light.increase_brightness()
            elif action =='<':
                smart_light.decrease_brightness()
            else:
                print("Error action must be '>' or '<'")

        elif choice ==6:
            security_camera.start_recording()

        elif choice ==7:
            print("Exiting Smart Device Management System ")
            break
        else:
            print("Error! input must be a number between 1 and 7")

if __name__ == "__main__":
    main()


