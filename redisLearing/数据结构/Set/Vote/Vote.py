def vote_up_key(vote_target):
    return vote_target + "::voteUP"
def vote_down_key(vote_target):
    return vote_target + "::voteDOWN"

class Vote:
    def __init__(self, client, vote_target) -> None:
        self.client = client
        self.vote_up_set = vote_up_key(vote_target)
        self.vote_down_set = vote_down_key(vote_target)
    
    def is_voted(self, user):
        in_vote_up_set = self.client.sismember(self.vote_up_set, user)
        in_vote_down_set = self.client.sismember(self.vote_down_set, user)
        return in_vote_up_set or in_vote_down_set
    
    def vote_up(self, user):
        if self.is_voted(user):
            return False
        return self.client.sadd(self.vote_up_set, user) == 1
    def vote_down(self, user):
        if self.is_voted(user):
            return False        
        return self.client.sadd(self.vote_down_set, user)

    def undo(self, user):
        self.client.srem(self.vote_up_set, user)
        self.client.srem(self.vote_down_set, user)

    def vote_up_count(self):
        return self.client.scard(self.vote_up_set)
    def vote_down_count(self):
        return self.client.scard(self.vote_down_set)

    def get_vote_up_user(self):
        return self.client.smembers(self.vote_up_set)
    def get_vote_down_user(self):
        return self.client.smembers(self.vote_down_set)