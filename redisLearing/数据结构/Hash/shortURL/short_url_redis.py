from baseConvert import base10_to_base36

ID_COUNTER = "ShortUrl::id_counter"
URL_HASH = "ShortUrl::url_hash"                 

# hash  short_id  target_url

class ShortUrl:
    def __init__(self, cli) -> None:
        self.client = cli
    
    def shorten(self, target_url):
        new_id = self.client.incr(ID_COUNTER)            # 根据网址id创建shortUrl（short_id）
        short_id = base10_to_base36(new_id)
        self.client.hset(URL_HASH, short_id, target_url) # hash field value
        return short_id
    
    def restore(self, short_id):
        return self.client.hget(URL_HASH, short_id)       # hash field -> value
    
        
