def make_key(a):
    return "auto_complete::" + a

class AutoComplete:
    def __init__(self, client) -> None:
        self.client = client
    
    def feed(self, content, weight=1):
        '''记录： 前缀 -> 完整内容'''
        for i in range(1, len(content)):
            key = make_key(content[:i])
            self.client.zincrby(key, weight, content)
        
    def hint(self, prefix, count):
        '''根据“记录”， 确定完整的内容可能是 top count 中某个'''
        key = make_key(prefix)
        return self.client.zrevrange(key, 0, count-1)