from truck_delivery_yess.content_manager import ContentManager
from truck_delivery_yess.util.constants import CLIENT_ID_PREFIX


class ClientManager(ContentManager):

    def __init__(self):
        super(ClientManager, self).__init__()

    def save_document(self, client):
        client_id = f"{CLIENT_ID_PREFIX}-{client.ci}"
        client_json = client.to_dict()
        return self._db_connector.save(client_id, client_json)

    def get_document(self, client_ci):
        client_id = f"{CLIENT_ID_PREFIX}-{client_ci}"
        return self._db_connector.get_by_id(client_id)

    def get_all(self):
        return self._db_connector.get_by_pattern(CLIENT_ID_PREFIX)

    def delete(self, client_ci):
        client_id = f"{CLIENT_ID_PREFIX}-{client_ci}"
        return self._db_connector.delete_by_id(client_id)
