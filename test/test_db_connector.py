import pytest

from truck_delivery_yess.db_connector import DBConnector


def test_save_object():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    db_connector = DBConnector()
    db_connector.save()

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save
