
from redis import Redis
from DuplicateChecker import DuplicateChecker

client = Redis(decode_responses=True)
dc = DuplicateChecker(client, "dc")

print(dc.is_duplicated("a"))
print(dc.is_duplicated("a"))
print(dc.is_duplicated("a"))
print(dc.unique_count())