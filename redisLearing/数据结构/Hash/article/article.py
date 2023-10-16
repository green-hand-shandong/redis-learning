from time import time


class Article:
    def __init__(self, client, article_id) -> None:
        self.client = client
        self.article_id = str(article_id)
        self.article_hash = "article::" + self.article_id
        
    def is_exist(self):
        return self.client.hexists(self.article_hash, "title")

    def create(self, title, content, author):
        if self.is_exist():
            return False
        article_data = {
            "title"   : title,
            "content" : content,
            "author"  : author, 
            "create_at": time()
        }
        self.client.hmset(self.article_hash, article_data)
    
    def get(self):
        article_data = self.client.hgetall(self.article_hash)
        article_data["id"] = self.article_id
        return article_data

    def update(self, title=None, content=None, author=None):
        if not self.is_exist():
            return False
        
        article_data = {}
        if title is not None:
            article_data["title"] = title
        if content is not None:
            article_data["content"] = content
        if author is not None:
            article_data["author"] = author
        return self.client.hmset(self.article_hash, article_data)
    
    