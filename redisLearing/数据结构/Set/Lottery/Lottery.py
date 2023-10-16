class Lottery:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key    = key
    
    def add_player(self, *playsers):
        return self.client.sadd(self.key, *playsers)

    def get_all_players(self):
        return self.client.smembers(self.key)
    
    def get_players_count(self):
        return self.client.scard(self.key)

    def draw(self, n=1):
        return self.client.srandmember(self.key, n)