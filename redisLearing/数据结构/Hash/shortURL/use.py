from redis import Redis
from short_url_redis import ShortUrl

client = Redis()
myShortUrl = ShortUrl(client)

print(myShortUrl.shorten("www.baidu1.com"))
print(myShortUrl.shorten("www.baidu2.com"))
print(myShortUrl.shorten("www.baidu3.com"))
print(myShortUrl.shorten("www.baidu4.com"))
print(myShortUrl.restore("1"))
print(myShortUrl.restore("2"))
print(myShortUrl.restore("3"))
print(myShortUrl.restore("4"))