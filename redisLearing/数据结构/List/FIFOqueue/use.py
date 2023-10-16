from FIFOqueue import FIFOqueue
from redis import Redis

client = Redis()
q = FIFOqueue(client, "buy-request")

print(q.enqueue("milk1"))
print(q.enqueue("milk2"))
print(q.enqueue("milk3"))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())