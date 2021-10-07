from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    """ Class to define basic information of a vehicle"""

    def __init__(self, vehicle_type, name):
        self.type = vehicle_type
        self.name = name

    @abstractmethod
    def get_location(self):
        pass
