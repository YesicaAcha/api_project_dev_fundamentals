import json

import pytest

from truck_delivery_yess.db_connector.db_connector_redis import DBConnectorRedis


@pytest.fixture
def db_connector(mocker):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    second_id_test = "456"
    second_object_to_save = {"456": {"b": "b"}}

    mocker.patch("redis.Redis.set").return_value = True
    mocker.patch("redis.Redis.get").return_value = json.dumps(object_to_save)
    mocker.patch("redis.Redis.scan_iter").return_value = [id_test, second_id_test]
    mocker.patch("redis.Redis.mget").return_value = [json.dumps(obj) for obj in [object_to_save, second_object_to_save]]
    mocker.patch("redis.Redis.delete").return_value = 1

    return DBConnectorRedis()


def test_save_mock(db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    result_save = db_connector.save(id_test, object_to_save)
    assert result_save is True


def test_get_by_id_mock(db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector.save(id_test, object_to_save)
    result = db_connector.get_by_id(id_test)
    assert result == object_to_save


def test_get_all_mock(db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    second_id_test = "456"
    second_object_to_save = {"456": {"b": "b"}}

    db_connector.save(id_test, object_to_save)
    db_connector.save(second_id_test, second_object_to_save)

    result = db_connector.get_all()
    assert result == [object_to_save, second_object_to_save]


def test_delete_by_id(db_connector):
    id_test = "123"
    object_to_save = {"123": {"a": "a"}}

    db_connector.save(id_test, object_to_save)

    result_delete = db_connector.delete_by_id(id_test)
    assert result_delete is True
