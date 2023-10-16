

class AutoComplete:
    def __init__(self, client) -> None:
        self.client = client
    
    def feed(self, content, weight=1, timeout=None):
        for i in range(1, len(content)):
            key = "AutoComplete::" + content[:i]
            self.client.zincrby(key, weight, content)           # z 有序集合
            if timeout is not None:
                self.client.expire(key, timeout)
    def hint(self, prefix, count):
        key = "AutoComplete::" + prefix
        return self.client.zrevrange(key, 0, count-1)
    