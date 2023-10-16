from redis import Redis
from Counter import Counter

client = Redis()
peter_counter = Counter(client, "page_view_counter", "/user/peter")
alice_counter = Counter(client, "page_view_counter", "/user/alice")
jacky_counter = Counter(client, "page_view_counter", "/user/jacky")

print(peter_counter.incr())
print(peter_counter.get())
print(alice_counter.incr(2))
print(alice_counter.decr(4))
print(alice_counter.get())
print(jacky_counter.reset())
print(jacky_counter.get())
