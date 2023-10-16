from redis import Redis
from articleRedis import Article

client = Redis()
article_id = 100
article = Article(client, article_id)

print(article.get())
article.create("redis-article-msetnx-oldtitle", "no content", "xiwa")
print(article.get())
article.update(title="redis-article-msetnx-newtitle", content="still no content", author="still xiwa")
print(article.get())



print(article.get_content_len())
print(article.get_content_preview(10))