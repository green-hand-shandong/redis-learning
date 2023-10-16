from redis import Redis
from logRedis import Log

# client = Redis(decode_responses=True)
client = Redis(decode_responses=True)       # 
key = "redis-log-of-xiwa"
log = Log(client, key)

log.add("00001")
log.add("00002")
log.add("00003")

print(log.all())