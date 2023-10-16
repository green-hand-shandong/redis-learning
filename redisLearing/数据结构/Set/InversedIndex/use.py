from redis import Redis
from InversedIndex import InvertedIndex

client = Redis(decode_responses=True)
ii = InvertedIndex(client)

print(ii.add_index("desktop", "screen", "keyboard", "mouse", "earphone", "sth"))
print(ii.get_keywords("desktop"))
print(ii.remove_keyword("desktop", "sth"))
print(ii.get_keywords("desktop"))