from redis import Redis
from paging import Paging

client = Redis(decode_responses=True)
key = "info"
topics = Paging(client, key)

for i in range(1, 20):
    topics.add(i)

print(topics.get_page(1,5))
print(topics.get_page(2,5))
print(topics.get_page(1,10))
print(topics.size())
