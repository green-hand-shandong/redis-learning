from redis import Redis
from UniqueCounter import UniqueCounter

client = Redis(decode_responses=True)
uc = UniqueCounter(client, "uniquecounter_hyperloglog")

print(uc.count_in("a"))
print(uc.count_in("a"))
print(uc.count_in("a"))
print(uc.count_in("b"))
print(uc.count_in("b"))
print(uc.count_in("c"))
print(uc.get_result())