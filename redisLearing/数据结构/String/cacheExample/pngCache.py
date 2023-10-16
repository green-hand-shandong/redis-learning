from redis import Redis
from cacheRedis import Cache

# conn
client = Redis()
print(f"ping : {client.ping()}")

# pngCache
pngCache = Cache(client)
# png
pngImage = open("blue.png", "rb")
data = pngImage.read()
pngImage.close()

# operation set -> get
pngCache.set("blue.png", data)
print(pngCache.get("blue.png")[:20])
