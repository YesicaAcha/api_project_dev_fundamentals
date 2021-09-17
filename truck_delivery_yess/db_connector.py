import redis
import json


class DBConnector:
    __instance = None
    __connection = None

    def __init__(self):
        if DBConnector.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DBConnector.__instance = self
            self.__connection = redis.Redis(host="localhost", port=6379)

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DBConnector.__instance is None:
            DBConnector()
        return DBConnector.__instance

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
        decode_data = json.loads(result_get)
        return decode_data

    def get_all(self):
        """
        Gets all objects saved in the database
        Returns:
            An dictionary with the objects saved in the database
        """
        decode_data = {}
        for key in self.__connection.scan_iter():
            result_get = self.__connection.get(key)
            decode_data[key.decode("utf-8")] = json.loads(result_get)
        return decode_data

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
