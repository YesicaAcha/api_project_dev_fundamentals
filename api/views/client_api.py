import json

from flask import (
    jsonify,
    request,
    abort,
    make_response,
    Blueprint
)

from api.constants import API_NAME
from truck_delivery_yess.model.client import Client
from truck_delivery_yess.client_manager import ClientManager

client = Blueprint('client', __name__, url_prefix=API_NAME)


@client.route("/clients", methods=["GET"])
def get_clients():
    """
    get_clients --> list all the clients
    Return:
        clients(list): list with all the clients
    """
    client_manager = ClientManager()
    return jsonify(client_manager.get_all())


@client.route("/clients/<int:client_id>", methods=["GET"])
def get_client_by_id(client_id):
    """
    get_client_by_id --> gets a client by id
    Args:
        client_id(int): The client id
    Return:
        client(dict): The client information
    """
    client_manager = ClientManager()
    client_to_return = client_manager.get_document(client_id)
    if client_to_return is None:
        abort(404, f"The client with id {client_id} does not seem to exist. Please enter a valid client id.")
    else:
        return jsonify(client_to_return)


@client.route("/clients", methods=["POST"])
def save_client():
    """
    save_client --> saves a client
    Args:
        request(json): Json with client information
    Return:
        A successful message
    """
    client_dict = request.json
    client = Client(client_dict.get("ci"), client_dict.get("name"), client_dict.get("email"),
                    client_dict.get("cellphone"), client_dict.get("address"), client_dict.get("nit"))
    client_manager = ClientManager()

    if client_manager.get_document(client.ci) is None:
        client_manager.save_document(client)
        return jsonify({"message": "The client was saved successfully."})
    else:
        abort(409, f"The client: {client.name} with CI: {client.ci} already exists")


@client.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client_by_id(client_id):
    """
    delete_client_by_id --> deletes a client by id
    Args:
        client_id(int): Driver ID to delete
    Return:
        driver(dict): The truck information that was deleted
    """
    client_manager = ClientManager()

    if client_manager.get_document(client_id) is None:
        abort(404, f"The client with ci {client_id} was not deleted because it doesn't seem to exist. "
                   "Please enter a valid client ci.")
    else:
        client_manager.delete(client_id)
        return make_response(f"Client with ci {client_id} successfully deleted", 200)
