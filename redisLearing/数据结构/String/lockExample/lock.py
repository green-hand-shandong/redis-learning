from redis import Redis
from lockRedis import Lock


client = Redis()
key = "test-lock"               # 
mutex = Lock(client, key)


print(mutex.release())
print(mutex.acquire())
print(mutex.acquire())
print(mutex.release())
print(mutex.acquire())