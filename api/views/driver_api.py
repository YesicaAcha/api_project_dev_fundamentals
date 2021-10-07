import json

from flask import (
    jsonify,
    request,
    abort,
    Blueprint
)

from api.constants import API_NAME
from api.views.truck_api import trucks
from truck_delivery_yess.driver_manager import DriverManager

drivers = [
    {
        'id': 0,
        'first_name': 'Santiago',
        'last_name': 'Cabrera',
        'license_number': '123456',
        'phone': '77912345',
        'truck_id': 2
    },
    {
        'id': 1,
        'first_name': 'Maximiliano',
        'last_name': 'Iglesias',
        'license_number': '987321',
        'phone': '77165478',
        'truck_id': 1
    },
    {
        'id': 2,
        'first_name': 'Ben',
        'last_name': 'Barnes',
        'license_number': '112233',
        'phone': '76765432',
        'truck_id': 0
    }
]

driver = Blueprint('driver', __name__, url_prefix=API_NAME)


@driver.route("/drivers", methods=["GET"])
def get_drivers():
    """
    get_drivers --> list all the drivers
    Return:
        drivers(list): list with all the drivers
    """
    driver_manager = DriverManager()
    return jsonify(driver_manager.get_all())


@driver.route("/drivers/<int:driver_id>", methods=["GET"])
def get_driver_by_id(driver_id):
    """
    get_driver_by_id --> gets a driver by id
    Args:
        driver_id(int): The driver id
    Return:
        driver(dict): The driver information
    """
    driver_to_return = {}
    for driver in drivers:
        if driver_id == driver.get('id'):
            driver_to_return = driver
            break

    if driver_to_return != {}:
        return jsonify(driver_to_return)
    else:
        return jsonify({"message": "The driver doesn't seem to exist. Please enter a valid driver ID."})


@driver.route("/drivers", methods=["POST"])
def save_driver():
    """
    save_driver --> saves a driver
    Args:
        request(json): Json with driver information
    Return:
        A successful message
    """
    driver_json = request.json
    drivers.append(driver_json)
    return jsonify({"message": "The driver was saved successfully."})


@driver.route("/drivers/<int:driver_id>", methods=["DELETE"])
def delete_driver_by_id(driver_id):
    """
    delete_driver_by_id --> deletes a driver by id
    Args:
        driver_id(int): Driver ID to delete
    Return:
        driver(dict): The truck information that was deleted
    """
    driver_to_remove = {}
    for driver in drivers:
        if driver_id == driver.get('id'):
            driver_to_remove = driver
            drivers.remove(driver_to_remove)
            break

    if driver_to_remove != {}:
        return jsonify(driver_to_remove)
    else:
        return abort(404, f"The driver with id {driver_id} was not deleted because it doesn't seem to exist. "
                          "Please enter a valid driver id.")


@driver.route("/drivers/<driver_identifier>/truck", methods=["GET"])
def get_truck_by_driver(driver_id_or_name):
    """
    get_truck_by_driver_id --> gets a truck information by driver name or ID
    Args:
        driver_id_or_name(str): Driver name or ID to get Truck information
    Return:
        truck(dict): The truck information
    """
    truck_driver = {}

    for driver in drivers:
        if (driver_id_or_name == driver.get('first_name')) or (int(driver_id_or_name) == driver.get('id')):
            truck_driver = driver
            break
    if truck_driver == {}:
        return jsonify({"message": "The driver doesn't seem to exist. Please enter a valid driver name or ID."})
    else:
        truck_to_return = {}
        for truck in trucks:
            if truck_driver.get('truck_id') == truck.get('id'):
                truck_to_return = truck
                break
        if truck_to_return == {}:
            return jsonify({"message": "The driver doesn't have a valid truck assigned."})
        else:
            return jsonify(truck_to_return)
