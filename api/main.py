from flask import (
    Flask,
    jsonify
)

from api.views import (
    client_api,
    driver_api,
    truck_api
)

from truck_delivery_yess.util.exceptions import DataBaseConnectionError

app = Flask(__name__)

app.register_blueprint(client_api.client)
app.register_blueprint(driver_api.driver)
app.register_blueprint(truck_api.truck)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Truck Manager</h1><p>This site is a prototype API to handle trucks and drivers information.</p> "


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify(error=str(error)), 404


@app.errorhandler(DataBaseConnectionError)
def data_not_available(error):
    return {"message": f"The data is not available. {error.message}"}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True,
            use_reloader=True,
            port=5000)
