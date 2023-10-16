
def following_key(user):
    return user + "::following"
def follower_key(user):
    return user + "::follower"

class RelationShip:
    def __init__(self, client, user) -> None:
        self.client = client
        self.user = user

    def follow(self, target):
        user_following_set = following_key(self.user)
        self.client.sadd(user_following_set, target)

        target_follower_set = follower_key(target)
        self.client.sadd(target_follower_set, self.user)
    def unfollow(self, target):
        user_following_set = following_key(self.user)
        self.client.srem(user_following_set, target)

        target_follower_set = follower_key(target)
        self.client.srem(target_follower_set, self.user)

    def is_following(self, target):
        user_following_set = following_key(self.user)
        return self.client.sismember(user_following_set, target)
    def get_all_following(self):
        user_following_set = following_key(self.user)
        return self.client.smembers(user_following_set)
    def get_all_follower(self):
        user_follower_set = follower_key(self.user)
        return self.client.smembers(user_follower_set)
    
    def count_following(self):
        user_following_set = following_key(self.user)
        return self.client.scard(user_following_set)
    def count_follower(self):
        user_follower_set = follower_key(self.user)
        return self.client.scard(user_follower_set)
