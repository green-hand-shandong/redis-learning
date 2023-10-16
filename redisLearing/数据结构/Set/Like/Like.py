class Like:
    def __init__(self, client, k) -> None:
        self.key = k 
        self.client = client
    
    def cast(self, user):
        return self.client.sadd(self.key, user) == 1
    def undo(self, user):
        return self.client.srem(self.key, user)

    def is_liked(self, user):
        return self.client.sismember(self.key, user)
    def get_all_users(self):
        return self.client.smembers(self.key)
    def count(self):
        return self.client.scard(self.key)
