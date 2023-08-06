import redis
from settings import *

r = redis.Redis(host=REDISHOST, port=6379, db=0, decode_responses=True)  
print(r.ping())  