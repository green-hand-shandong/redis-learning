def following_key(user):
    return user + "::following"

class CommonFollowing:
    def __init__(self, cli) -> None:
        self.client = cli   
    
    def calculate(self, user, target):
        user_following_set = following_key(user)
        target_following_set = following_key(target)
        return self.client.sinter(user_following_set, target_following_set)
    
    def calculate_and_store(self, user, target):
        user_following_set = following_key(user)
        target_following_set = following_key(target)
        return self.client.sinter(user_following_set, target_following_set)
    
