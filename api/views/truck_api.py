import json

from flask import (
    jsonify,
    request,
    Blueprint
)

from api.constants import API_NAME

trucks = [
    {
        'id': 0,
        'plate': '5318XZA',
        'brand': 'Chevrolet',
        'model': 'Chevy Kodiak',
        'color': 'Red'
    },
    {
        'id': 1,
        'plate': '4419TND',
        'brand': 'Fiat',
        'model': 'Strada',
        'color': 'Silver'
    },
    {
        'id': 2,
        'plate': '2461EDC',
        'brand': 'Daimler',
        'model': 'Cascadia',
        'color': 'White'
    }
]

truck = Blueprint('truck', __name__, url_prefix=API_NAME)


@truck.route("/trucks", methods=["GET"])
def get_trucks():
    """
    get_trucks --> list all the trucks
    Return:
        trucks(list): list with all the trucks
    """
    return jsonify(trucks)


@truck.route("/trucks/<int:truck_id>", methods=["GET"])
def get_truck_by_id(truck_id):
    """
    get_truck_by_id --> gets a truck by ID
    Args:
        truck_id(int): The truck id
    Return:
        truck(dict): The truck information
    """
    truck_to_return = {}
    for truck in trucks:
        if truck_id == truck.get('id'):
            truck_to_return = truck
            break

    if truck_to_return != {}:
        return jsonify(truck_to_return)
    else:
        return jsonify({"message": "The truck doesn't seem to exist. Please enter another truck id."}), 404


@truck.route("/trucks", methods=["POST"])
def save_truck():
    """
    save_truck --> Adds a new truck to the truck manager
    Args:
        request(json): Json with truck information
    Return:
        A successful message
    """
    truck_json = request.json
    trucks.append(truck_json)
    return jsonify({"message": "The truck was saved successfully."})


@truck.route("/trucks/<int:truck_id>", methods=["DELETE"])
def delete_truck_by_id(truck_id):
    """
    delete_truck_by_id --> deletes a truck by id
    Args:
        truck_id(int): The truck id to be deleted
    Return:
        truck(dict): The truck information that was deleted
    """
    truck_to_remove = {}
    for truck in trucks:
        if truck_id == truck.get('id'):
            truck_to_remove = truck
            trucks.remove(truck_to_remove)
            break

    if truck_to_remove != {}:
        return jsonify(truck_to_remove)
    else:
        return jsonify({"message": "The truck was not deleted because it doesn't seem to exist. "
                                   "Please enter a valid truck ID."})
