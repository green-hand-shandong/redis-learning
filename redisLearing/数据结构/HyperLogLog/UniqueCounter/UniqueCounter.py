class UniqueCounter:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def count_in(self, item):
        self.client.pfadd(self.key, item)
    
    def get_result(self):
        return self.client.pfcount(self.key)
    