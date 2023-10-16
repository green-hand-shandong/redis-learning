from redis import Redis
from Vote import Vote

v = Vote(Redis(decode_responses=True), "question::10086")

print(v.vote_up("xiwa 1"))
print(v.vote_up("xiwa 2"))
print(v.vote_down("xiwa 1"))
print(v.vote_down("xiwa 2"))
print(v.get_vote_up_user())
print(v.get_vote_down_user())
print(v.vote_up_count())
print(v.vote_down_count())

print(v.undo("xiwa 1"))
print(v.get_vote_up_user())
print(v.get_vote_down_user())
print(v.vote_up_count())
print(v.vote_down_count())
