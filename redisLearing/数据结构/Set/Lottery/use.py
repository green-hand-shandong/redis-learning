import redis 
from Lottery import Lottery

l = Lottery(redis.Redis(decode_responses=True), "lottery")

print(l.add_player("tom", "jack", "mary"))
print(l.get_all_players())
print(l.get_players_count())
print(l.draw())
print(l.draw(-5))