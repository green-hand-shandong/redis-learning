class VoatileCache:
    def __init__(self, client) -> None:
        self.client = client
    
    def set(self, key, value, timeout):
        self.client.set(key,value, ex=timeout)
    
    def get(self, key):
        return self.client.get(key)
    
