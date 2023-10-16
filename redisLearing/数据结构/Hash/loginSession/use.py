from Session import LoginSession
from redis import Redis

client = Redis(decode_responses=True)           # 不解码时会出现错误
user_id = "xiwa"
mySession = LoginSession(client, user_id)

token = mySession.create()
print(token)

print(mySession.validate("wrong-token"))
print(mySession.validate(token))
print(mySession.destroy())
print(mySession.validate(token))

