
class Cache:
    def __init__(self, client):
        self.client = client
    
    def set(self, key, value):
        self.client.set(key, value)
    
    def get(self, key):
        return self.client.get(key)
    
    def update(self, key, new_value):
        '''
        返回 old_value
        设置 new_value
        '''
        return self.client.getset(key, new_value)
    
