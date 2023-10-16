class TimeLine:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def add(self, item, time):
        self.client.zadd(self.key, {item:time})
    
    def remove(self, item):
        self.client.zrem(self.key, item)
    
    def count(self):
        return self.client.zcard(self.key)
    
    def pagging(self, number, count, with_time=False):
        start_index = (number-1) * count
        end_index   = number * count - 1
        return self.client.zrevrange(self.key, start_index, end_index, withscores=with_time)
    
    def fetch_by_time_range(self, min_time, max_time, number, count, with_time=False):
        start_index = (number - 1) * count
        return self.client.zrevrangebyscore(self.key, max_time, min_time, start_index, count, withscores=with_time)
        #                                               max      min        offset     count
        