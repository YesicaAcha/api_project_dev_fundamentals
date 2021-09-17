from truck_delivery_yess.vehicle import Vehicle


class Truck(Vehicle):
    """ Class representing a Truck """
    def __init__(self, vehicle_type, name, license_plate, truck_type, model, manufacturer):
        super(Truck, self).__init__(vehicle_type, name)
        self.license_plate = license_plate
        self.truck_type = truck_type
        self.model = model
        self.manufacturer = manufacturer

    def get_location(self):
        pass
