import redis  # type: ignore
from settings import REDISHOST

r = redis.Redis(host=REDISHOST, port=6379, db=0, decode_responses=True)
if r.ping():
    print('Redis is here!')
