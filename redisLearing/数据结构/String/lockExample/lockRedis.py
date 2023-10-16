VALUE_OF_LOCK = "locking"

class Lock:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key    = key
    def acquire(self):  
        result = self.client.set(self.key, VALUE_OF_LOCK, nx=True)
        return result is True
    def release(self):
        return self.client.delete(self.key) == 1


