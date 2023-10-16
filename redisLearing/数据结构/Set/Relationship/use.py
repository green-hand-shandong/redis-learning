from redis import Redis
from Relationship import RelationShip

client = Redis(decode_responses=True)
peter = RelationShip(client, "peter")
jack = RelationShip(client, "jack")

print(jack.follow("peter"))
print(peter.follow("mary"))
print(peter.get_all_following())
print(peter.get_all_follower())
print(peter.count_follower())
print(peter.count_following())

print(peter.unfollow("mary"))
print(peter.get_all_following())
print(peter.get_all_follower())
print(peter.count_follower())
print(peter.count_following())
