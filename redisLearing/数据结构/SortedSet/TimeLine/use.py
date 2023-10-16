from redis import Redis
from TimeLine import TimeLine

client = Redis(decode_responses=True)
tl = TimeLine(client, "blog_timeline")

print(tl.add("a", 20230925))
print(tl.add("b", 20230924))
print(tl.add("c", 20230923))
print(tl.add("d", 20230922))
print(tl.add("e", 20230921))
print(tl.add("f", 20230920))
print(tl.pagging(1,4,with_time=True))
print(tl.count())
print(tl.remove("a"))
print(tl.count())
print(tl.fetch_by_time_range(20230920, 20230925, 1,4, True))