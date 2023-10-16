
class FIFOqueue:
    def __init__(self, client, list_key) -> None:
        self.client = client
        self.key = list_key
    
    def enqueue(self, item):
        return self.client.lpush(self.key, item)

    def dequeue(self):
        return self.client.rpop(self.key)
    