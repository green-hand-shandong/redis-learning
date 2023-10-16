from Path import Path
import redis

client = redis.Redis(decode_responses=True)
p = Path(client)

p.forward_to("a", "b")
p.forward_to("a", "b")
p.forward_to("a", "c")
p.forward_to("a", "d")
print(p.pagging_record("a", 1, 5, with_time=True))