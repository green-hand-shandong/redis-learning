
class DuplicateChecker:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key    = key

    def is_duplicated(self, item):
        return self.client.pfadd(self.key, item) == 0
    
    def unique_count(self):
        return self.client.pfcount(self.key)