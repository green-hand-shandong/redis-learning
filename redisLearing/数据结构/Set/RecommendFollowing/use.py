from RecommendFollowing import RecommendFollowing
from redis import Redis
client = Redis(decode_responses=True)

rf = RecommendFollowing(client, "jacky")
print(rf.calculate(2))
print(rf.fetch_result(2))


