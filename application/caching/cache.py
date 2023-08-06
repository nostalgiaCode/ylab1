import json

import redis


class RedisCache:
    def __init__(self, redis: redis.Redis):
        self.r = redis

    def cache_get(self, key: str):
        value = self.r.get(key)
        if value is not None:
            return json.loads(value)
        else:
            return None
    
    def cache_set(self, key: str, json_object: json):
        self.r.set(key, json_object)

    def cache_delete(self, key: str):
        self.r.delete(key)