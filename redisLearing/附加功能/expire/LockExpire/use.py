from redis import Redis
from TimeingLocak import TimingLock
from time import sleep
client = Redis(decode_responses=True)
lock = TimingLock(client, "test-lock")


print(lock.acquire(5))
print(lock.release())
print(lock.acquire(5))
print(lock.acquire(5))
sleep(5)
print(lock.acquire(5))