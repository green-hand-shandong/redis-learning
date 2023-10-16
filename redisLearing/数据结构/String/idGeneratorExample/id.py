from redis import Redis
from idGeneratorRedis import idGenerator


client = Redis(decode_responses=True)
key = "user::id"
myIDGenerator = idGenerator(client, key)


myIDGenerator.reserve(1000000)
print(myIDGenerator.get())
myIDGenerator.produce()
print(myIDGenerator.get())
myIDGenerator.produce()
print(myIDGenerator.get())
