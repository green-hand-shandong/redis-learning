class Counter:
    def __init__(self, client, key, counter_name) -> None:
        self.client = client                # conn
        self.hash_key = key                 # field
        self.counter_name = counter_name    # value
    
    def incr(self, n=1):
        return self.client.hincrby(self.hash_key, self.counter_name, n)
    def decr(self, n=1):
        return self.client.hincrby(self.hash_key, self.counter_name, -n)
    def get(self):
        value = self.client.hget(self.hash_key, self.counter_name)
        return value if value is not None else 0
    def reset(self):
        self.client.hset(self.hash_key, self.counter_name, 0)