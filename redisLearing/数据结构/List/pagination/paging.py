class Paging:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key

    def add(self,item):
        self.client.lpush(self.key, item)

    def get_page(self, page_number, item_per_page):
        start_index = (page_number - 1) * item_per_page
        end_index = page_number * item_per_page - 1
        return self.client.lrange(self.key, start_index, end_index)
    
    def size(self):
        return self.client.llen(self.key)
