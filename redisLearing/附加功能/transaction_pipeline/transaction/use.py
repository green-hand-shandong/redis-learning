from redis import Redis
from MLPOP import MLPOP

client = Redis(decode_responses=True)

client.rpush("lst", "1", "2", "3")
print(MLPOP(client,"lst", 3))