from redis import Redis
from counterRedis import Counter
client = Redis()
key = "Counter::page_iew"
myCounter = Counter(client, key)

myCounter.increase()
print(myCounter.get())
myCounter.decrease()
print(myCounter.get())
myCounter.increase(10)
print(myCounter.get())
myCounter.reset(404)
print(myCounter.get())
