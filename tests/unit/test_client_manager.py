import json

import pytest

from truck_delivery_yess.model.client import Client
from truck_delivery_yess.client_manager import ClientManager
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


@pytest.mark.skip(reason="redis is not running")
def test_save_client():
    client = Client("47900124", "Test Client", "test.client", "73777777", "test Street", "47900124")
    client_manager = ClientManager()
    result_save = client_manager.save_document(client)
    assert result_save is True


@pytest.mark.skip(reason="redis is not running")
def test_get_client():
    client = Client("47900124", "Test Client", "test.client", "73777777", "test Street", "47900124")
    client_manager = ClientManager()
    client_manager.save_document(client)

    result = client_manager.get_document(client.ci)
    assert result == client.to_dict()


@pytest.mark.skip(reason="redis is not running")
def test_get_all_clients():
    first_client = Client("47900124", "Test Client", "test.client", "73777777", "test Street", "47900124")
    second_client = Client("49123454", "Second Client", "second.client", "767444999", "Second Street", "49123454")
    client_manager = ClientManager()
    client_manager.save_document(first_client)
    client_manager.save_document(second_client)

    result = client_manager.get_all()
    assert result == [first_client.to_dict(), second_client.to_dict()]


@pytest.mark.skip(reason="redis is not running")
def test_delete_client():
    client = Client("47900124", "Test Client", "test.client", "73777777", "test Street", "47900124")
    client_manager = ClientManager()
    client_manager.save_document(client)

    result = client_manager.delete(client.ci)
    assert result is True
