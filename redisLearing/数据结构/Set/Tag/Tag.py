def make_tag_key(item):
    return item + "::tags"

class Tagging:
    def __init__(self, c, k) -> None:
        self.client = c
        self.key    = make_tag_key(k)
    
    def add(self, *tags):
        return self.client.sadd(self.key, *tags)
    def remove(self, *tags):
        return self.client.srem(self.key, *tags)

    def is_include(self, tag):
        return self.client.sismember(self.key, tag)

    def get_all_tags(self):
        return self.client.smembers(self.key)

    def count(self):
        return self.client.scard(self.key)
    

        