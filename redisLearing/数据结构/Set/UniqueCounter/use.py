from redis import Redis
from UniqueCounter import UniqueCounter

cli = Redis(decode_responses=True)
c = UniqueCounter(cli, "ipCounter")

print(c.count_in("a"))
print(c.count_in("a"))
print(c.count_in("b"))
print(c.count_in("c"))
print(c.get_result())