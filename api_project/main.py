from flask import (
    Flask,
    jsonify,
    request
)

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


app = Flask(__name__)

API_NAME = "/api/v1"


@app.route('/', methods=['GET'])
def home():
    return "<h1>Truck Manager</h1><p>This site is a prototype API to handle trucks and drivers information.</p> "


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route(f"{API_NAME}/trucks", methods=["GET"])
def get_trucks():
    """
    get_trucks --> list all the trucks
    Return:
        trucks(list): list with all the trucks
    """
    return jsonify(trucks)


@app.route(f"{API_NAME}/trucks/<int:truck_id>", methods=["GET"])
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


@app.route(f"{API_NAME}/trucks", methods=["POST"])
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


@app.route(f"{API_NAME}/trucks/<int:truck_id>", methods=["DELETE"])
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


@app.route(f"{API_NAME}/drivers", methods=["GET"])
def get_drivers():
    """
    get_drivers --> list all the drivers
    Return:
        drivers(list): list with all the drivers
    """
    return jsonify(drivers)


@app.route(f"{API_NAME}/drivers/<int:driver_id>", methods=["GET"])
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


@app.route(f"{API_NAME}/drivers", methods=["POST"])
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


@app.route(f"{API_NAME}/drivers/<int:driver_id>", methods=["DELETE"])
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
        return jsonify({"message": "The driver was not deleted because it doesn't seem to exist. "
                                   "Please enter a valid driver id."}), 404


@app.route(f"{API_NAME}/drivers/<driver_identifier>/truck", methods=["GET"])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            use_reloader=True,
            port=5000)
