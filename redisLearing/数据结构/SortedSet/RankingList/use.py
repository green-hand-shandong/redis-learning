from redis import Redis
from RankingList import RankingList

client = Redis(decode_responses=True)
rl = RankingList(client, "music")
print(rl.set_score("jay", 100))
print(rl.set_score("mbl", 75))
print(rl.set_score("xyz", 50))
print(rl.set_score("qkl", 25))
print(rl.get_rank("jay"))
print(rl.incr_score("jay", 20))
print(rl.desc_score("jay", 5))
print(rl.get_score("jay"))
print(rl.remove("jay"))
print(rl.top(4))