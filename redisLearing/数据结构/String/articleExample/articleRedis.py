from time import time 

class Article:
    def __init__(self, client, article_id) -> None:
        self.client = client
        self.id = str(article_id)
        self.title_key = "article::"+self.id+"::title"
        self.content_key = "article::"+self.id+"::content"
        self.author_key = "article::"+self.id+"::author"
        self.create_at_key = "article::"+self.id+"::create_at"
    
    def create(self, title, content, author):
        article_data = {
            self.title_key      : title,
            self.content_key    : content ,
            self.author_key     : author,
            self.create_at_key  : time() ,
        }
        return self.client.msetnx(article_data)  # dict
    
    def get(self):
        result = self.client.mget(self.title_key, self.content_key, self.author_key, self.create_at_key)
        return {
            "id"         : self.id,
            "title"      : result[0],
            "content"    : result[1],
            "author"     : result[2],
            "create_at"  : result[3]
        }
    
    def update(self, title=None, content=None, author=None):    # 可选择地进行更新，传入谁更新谁
        article_data = {}
        if title is not None:
            article_data[self.title_key] = title
        if content is not None:
            article_data[self.content_key] = content
        if author is not None:
            article_data[self.author_key] = author
        
        return self.client.mset(article_data)

    def get_content_len(self):
        return self.client.strlen(self.content_key)
    
    def get_content_preview(self, preview_len):
        start_index = 0
        end_index = preview_len - 1
        return self.client.getrange(self.content_key, start_index, end_index)
    

    