
class UniqueCounter:
    def __init__(self, cli, key) -> None:
        self.client = cli
        self.key = key
    
    def count_in(self, item):
        return self.client.sadd(self.key, item) == 1
    def get_result(self):
        return self.client.scard(self.key)