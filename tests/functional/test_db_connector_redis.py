import pytest
from truck_delivery_yess.db_connector.db_connector_redis import DBConnectorRedis


@pytest.mark.skip(reason="redis is not running")
def test_save_object():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnectorRedis()
    result_save = db_connector.save(id_test, object_to_save)
    assert result_save is True


@pytest.mark.skip(reason="redis is not running")
def test_get_by_id():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


@pytest.mark.skip(reason="redis is not running")
def test_get_all():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    second_id_test = "456"
    second_object_to_save = {"456": {"b": "b"}}

    db_connector = DBConnectorRedis()
    db_connector.save(id_test, object_to_save)
    db_connector.save(second_id_test, second_object_to_save)

    result = db_connector.get_all()
    assert result == [object_to_save, second_object_to_save]


@pytest.mark.skip(reason="redis is not running")
def test_delete_by_id():
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector = DBConnectorRedis()
    db_connector.save(id_test, object_to_save)

    result_delete = db_connector.delete_by_id(id_test)
    assert result_delete is True