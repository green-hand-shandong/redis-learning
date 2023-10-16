# import sys
# sys.path.append('C:\\Users\\230800099\\Desktop\\Python\\redisLearing\\Set\\Relationship')

from redis import Redis 
from CommonFollowing import CommonFollowing
from Relationship import RelationShip

client = Redis(decode_responses=True)
peter = RelationShip(client, "peter")
jacky = RelationShip(client, "jacky")

jacky.follow("peter")
jacky.follow("tom")
peter.follow("mary")
peter.follow("tom")

cf = CommonFollowing(client)
print(cf.calculate("peter", "jacky"))
print(cf.calculate_and_store("peter", "jacky"))
