from truck_delivery_yess.content_manager import ContentManager
from truck_delivery_yess.util.constants import DRIVER_ID_PREFIX


class DriverManager(ContentManager):

    def __init__(self):
        super(DriverManager, self).__init__()

    def save_document(self, driver):
        driver_id = f"{DRIVER_ID_PREFIX}-{driver.ci}"
        driver_json = driver.to_dict()
        return self._db_connector.save(driver_id, driver_json)

    def get_document(self, driver_ci):
        driver_id = f"{DRIVER_ID_PREFIX}-{driver_ci}"
        return self._db_connector.get_by_id(driver_id)

    def get_all(self):
        return self._db_connector.get_by_pattern(DRIVER_ID_PREFIX)

    def delete(self, driver_ci):
        driver_id = f"{DRIVER_ID_PREFIX}-{driver_ci}"
        return self._db_connector.delete_by_id(driver_id)
