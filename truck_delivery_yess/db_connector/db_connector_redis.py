import redis
import json

from singleton_decorator import singleton

from truck_delivery_yess.db_connector.db_connector import DBConnector
from truck_delivery_yess.util.configuration import Configuration


@singleton
class DBConnectorRedis(DBConnector):

    def __init__(self):
        self.__connection = redis.Redis(host=Configuration().get_db_connection_host(),
                                        port=Configuration().get_db_connection_port())

    def save(self, id_save, object_to_save):
        """
        Saves and object in the database
        Args:
            id_save: id of the object to save
            object_to_save: object to save

        Returns:
            True if the object was save, False otherwise
        """
        encode_data = json.dumps(object_to_save)
        result_save = self.__connection.set(id_save, encode_data)
        return result_save

    def get_by_id(self, id):
        """
        Gets an object by id
        Args:
            id: id of the object to get
        Returns:
            The object with the id
        """
        result_get = self.__connection.get(id)
        if result_get is None:
            return None
        else:
            decode_data = json.loads(result_get)
            return decode_data

    def get_all(self):
        """
        Gets a list of max 20 objects saved in the database
        Returns:
            A list with the objects saved in the database
        """
        list_objects = []
        list_ids = [id for id in self.__connection.scan_iter(count=20)]
        if len(list_ids) > 0:
            list_objects = self.__connection.mget(list_ids)
            list_objects = [json.loads(obj) for obj in list_objects]
        return list_objects

    def get_by_pattern(self, pattern):
        """
        Gets a list of max 20 objects saved in the database that match with a pattern
        Args:
            pattern: String to filter objects saved in the database.
        Returns:
            A list with the objects saved in the database that match the pattern
        """
        pattern = f"{pattern}*"
        list_objects = []
        list_ids = [id for id in self.__connection.scan_iter(match=pattern, count=20)]
        if len(list_ids) > 0:
            list_objects = self.__connection.mget(list_ids)
            list_objects = [json.loads(obj) for obj in list_objects]
        return list_objects

    def delete_by_id(self, id):
        """
        Deletes an object by id
        Args:
            id: id of the object to remove

        Returns:
            True if the object was removed, false otherwise
        """
        result_delete = self.__connection.delete(id)
        return result_delete is 1
