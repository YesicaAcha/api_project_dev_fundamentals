from abc import ABCMeta, abstractmethod


class DBConnector(metaclass=ABCMeta):

    @abstractmethod
    def save(self, id_save, object_to_save):
        """
        Saves and object in the database
        Args:
            id_save: id of the object to save
            object_to_save: object to save

        Returns:
            True if the object was save, False otherwise
        """
        pass

    @abstractmethod
    def get_by_id(self, id):
        """
        Gets an object by id
        Args:
            id: id of the object to get
        Returns:
            The object with the id
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Gets a list of max 20 objects saved in the database
        Returns:
            A list with the objects saved in the database
        """
        pass

    @abstractmethod
    def get_by_pattern(self, pattern):
        """
        Gets a list of max 20 objects saved in the database that match with a pattern
        Args:
            pattern: String to filter objects saved in the database.
        Returns:
            A list with the objects saved in the database that match the pattern
        """
        pass

    @abstractmethod
    def delete_by_id(self, id):
        """
        Deletes an object by id
        Args:
            id: id of the object to remove

        Returns:
            True if the object was removed, false otherwise
        """
        pass
