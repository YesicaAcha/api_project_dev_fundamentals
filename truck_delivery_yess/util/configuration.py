import os

from singleton_decorator import singleton

from truck_delivery_yess.util.yml_reader import YmlReader


@singleton
class Configuration:

    def __init__(self, configuration=None):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        self.config = configuration if configuration else YmlReader(os.path.join(root_dir, "../../truck_delivery_yess"
                                                                                           "/configuration.yml"))
        self.db_connection = self.config.get_var("db_connection")

    def get_db_connection_host(self):
        return self.db_connection.get("host")

    def get_db_connection_port(self):
        return self.db_connection.get("port")
