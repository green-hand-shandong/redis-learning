from redis import Redis
from VolatileCache import VoatileCache
from time import sleep
 
client = Redis(decode_responses=True)
cache = VoatileCache(client)
cache.set("homepage", "homepage -- welcome", 1)

print(cache.get("homepage"))
sleep(2)
print(cache.get("homepage"))
