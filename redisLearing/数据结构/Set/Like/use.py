from redis import Redis
from Like import Like

l = Like(Redis(decode_responses=True), "topic::10086::like")

print(l.cast("a"))
print(l.cast("b"))
print(l.cast("c"))
print(l.get_all_users())
print(l.count())
print(l.is_liked("a"))

print(l.undo("a"))
print(l.get_all_users())
print(l.count())
print(l.is_liked("a"))

