from AutoComplete import AutoComplete
import redis

client = redis.Redis(decode_responses=True)
ac = AutoComplete(client)

ac.feed("xiwa", 20)
ac.feed("xiqw", 100)
print(ac.hint("xi", 2))