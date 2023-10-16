from AutoComplete import AutoComplete
from redis import Redis
from time import sleep

client = Redis(decode_responses=True)
ac = AutoComplete(client)

print(ac.feed("tom", timeout=1))
print(ac.feed("tom", timeout=1))
print(ac.feed("top", timeout=3))
print(ac.hint("to", 2))
sleep(1)
print(ac.hint("to", 2))
sleep(2)
print(ac.hint("to", 2))
