from abc import ABCMeta, abstractmethod

from truck_delivery_yess.db_connector.db_connector_redis import DBConnectorRedis


class ContentManager(metaclass=ABCMeta):
    def __init__(self, connector=None):
        self._db_connector = connector if connector else DBConnectorRedis()

    @abstractmethod
    def save_document(self, document):
        pass

    @abstractmethod
    def get_document(self, document_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, document_id):
        pass
