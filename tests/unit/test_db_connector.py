import pytest

from truck_delivery_yess.db_connector import DBConnector


def test_save_mock(mocker):
    mocker.patch("truck_delivery_yess.db_connector.DBConnector.save").return_value = True

    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnector.get_instance()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}
    mocker.patch("truck_delivery_yess.db_connector.DBConnector.save").return_value = True
    mocker.patch("truck_delivery_yess.db_connector.DBConnector.get_by_id").return_value = object_to_save

    db_connector = DBConnector()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save
