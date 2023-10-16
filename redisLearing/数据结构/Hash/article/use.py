from article import Article
from redis import Redis

client = Redis(decode_responses=True)
article_id = 10086
article = Article(client, article_id)

print(article.create("title-of-xiwa", "contenet of xiwa", "xiwa"))
print(article.get())
print(article.is_exist())
print(article.update(author="xiwa-25"))
print(article.get())
