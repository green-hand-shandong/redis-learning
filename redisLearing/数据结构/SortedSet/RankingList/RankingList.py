class RankingList:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key

    def set_score(self, item, score):
        self.client.zadd(self.key, {item:score})

    def get_score(self, item):
        return self.client.zscore(self.key, item)

    def remove(self, item):
        self.client.zrem(self.key, item)
    
    def incr_score(self, item, increment):
        self.client.zincrby(self.key, increment, item)
    
    def desc_score(self, item, increment):
        self.client.zincrby(self.key, -increment, item)
    
    def get_rank(self, item):
        rank = self.client.zrevrank(self.key, item)
        return rank + 1 if rank is not None else None
    
    def top(self, n, with_score=False):
        return self.client.zrevrange(self.key, 0, n-1, withscores=with_score)

