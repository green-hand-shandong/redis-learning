import redis
client = redis.Redis(decode_responses=True)

from db_iterator import DbIterator
iter = DbIterator(client)

# for i in range(50):
#     key = f"key{i}"
#     value = i
#     client.set(key, value)   # string

# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())
# print(iter.next())

for key in client.scan_iter():
    print(key)