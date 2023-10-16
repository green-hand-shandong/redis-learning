from Matrix01 import Matrix01
import redis

m = Matrix01(redis.Redis(decode_responses=True), "mattrix-test", 5, 5)

print(m.set(0,0, 1))
print(m.set(0,2, 1))
print(m.set(0,4, 1))
print(m.get(0,0))
print(m.show())
