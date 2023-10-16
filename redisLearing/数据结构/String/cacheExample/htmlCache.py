from redis import Redis
from cacheRedis import Cache

# conn
client = Redis()
print(f"ping : {client.ping()}")
# Cache()
htmlCache = Cache(client)
# set -> get -> getset
htmlKey = "greeting-page"
oldHtmlValue = "<html><p> this is a redis HTML old value </p></html>"
newHtmlValue = "<html><p> this is a redis HTML new value </p></html>"
htmlCache.set(htmlKey, oldHtmlValue)
print(htmlCache.update(htmlKey, newHtmlValue))
print(htmlCache.get(htmlKey))
