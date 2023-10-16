import redis
from ActionRecord import ActionRecorder

ar = ActionRecorder(redis.Redis(decode_responses=True), "read the book")
print(ar.perform_by(1))
print(ar.perform_by(2))
print(ar.perform_by(4))
print(ar.perform_by(5))
print(ar.is_performed_by(3))
print(ar.count_performed())