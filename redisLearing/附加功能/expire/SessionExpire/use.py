from redis import Redis
from SessionLogin import SessionLogin
from time import sleep

client = Redis(decode_responses=True)
sl = SessionLogin(client, "peter")

token = sl.create(5)
print(token)
print(sl.validate("wrong token"))
print(sl.validate(token))
print(sl.destroy())
print(sl.validate(token))