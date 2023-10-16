def make_item_key(item):
    return "InversedIndex::" + item + "::keywords"
def make_keyword_key(keyword):
    return "InversedIndex::" + keyword + "::items"

class InvertedIndex:
    def __init__(self, client) -> None:
        self.client = client
    
    def add_index(self, item, *keywords):
        item_key = make_item_key(item)
        result = self.client.sadd(item_key, *keywords)
        for keyword in keywords:
            keyword_key = make_keyword_key(keyword)
            self.client.sadd(keyword_key, item)
        return result

    def remove_keyword(self, item, *keywords):
        item_key = make_item_key(item)
        result = self.client.srem(item_key, *keywords)
        for keyword in keywords:
            keyword_key = make_keyword_key(keyword)
            self.client.srem(keyword_key, item)
        return result

    def get_keywords(self, item):
        return self.client.smembers(make_item_key(item))
    