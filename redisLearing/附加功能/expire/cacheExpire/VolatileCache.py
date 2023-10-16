class VoatileCache:
    def __init__(self, client) -> None:
        self.client = client
    
    def set(self, key, value, timeout):
        self.client.set(key,value)
        self.client.expire(key, timeout)
    
    def get(self, key):
        return self.client.get(key)
    
