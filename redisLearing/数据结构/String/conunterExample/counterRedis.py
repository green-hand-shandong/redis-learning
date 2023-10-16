class Counter:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def increase(self, n=1):
        return self.client.incr(self.key, n)
    
    def decrease(self, n=1):
        return self.client.decr(self.key, n)
    
    def get(self):
        value = self.client.get(self.key)
        if value is None:
            return 0
        return value
    
    def reset(self):
        old_value = self.client.getset(self.key, 0)
        if old_value is None:
            return 0
        return old_value
    
