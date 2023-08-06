from tires.tire import Tire

class carriganTires(Tire):
    def __init__(self, tires_wear_sensors):
        self.tires_wear_sensors = tires_wear_sensors


    def needs_service(self):
        return self.tires_wear_sensors >=0.9
            