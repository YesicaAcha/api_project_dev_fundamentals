import redis


class DBConnector:
    def __init__(self):
        pass

    def save(self, id_save, object_to_save):
        redis_conn = redis.Redis(host="localhost",
                                 port=6379)
        redis_conn.set(id_save, object_to_save)
