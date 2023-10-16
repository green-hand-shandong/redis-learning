from redis import Redis
from Tag import Tagging

cli = Redis(decode_responses=True)
key = "CSAPP"
t = Tagging(cli, key)

print(t.add("classic", "awesome"))
print(t.get_all_tags())
print(t.count())

print(t.remove("classic", "awesome"))
print(t.get_all_tags())
print(t.count())