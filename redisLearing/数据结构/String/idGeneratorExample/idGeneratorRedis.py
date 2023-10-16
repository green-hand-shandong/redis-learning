class idGenerator:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def produce(self):
        return self.client.incr(self.key)
    
    def reserve(self, n):
        # result = self.client.set(self.key, n)
        result = self.client.set(self.key, n, nx=True) # 避免冲突
        return result is True
    
    def get(self):
        return self.client.get(self.key)
