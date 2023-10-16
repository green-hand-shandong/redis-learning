from time import time
from hashlib import sha256
import random

DEFAULT_TIMEOUT = 3600 * 24 * 30

SESSION_TOKEN_HASH = "session::token"                   # 会话令牌                 1. hash : user_id : token 
SESSION_EXPIRE_TS_HASH = "session::expire_timestamp"    # 会话过期时间戳            2. hash : user_id : expire_timestamp

# 会话状态
SESSION_NOT_LOGIN = "SESSION_NOT_LOGIN"
SESSION_EXPIRED = "SESSION_EXPIRED" 
SESSION_TOKEN_CORRECT = "SESSION_TOKEN_CORRECT"
SESSION_TOKEN_INCORRECT = "SESSION_TOKEN_INCORRECT"

def generate_token():
    random_string = str(random.getrandbits(256)).encode('utf-8') 
    return sha256(random_string).hexdigest()

class LoginSession:
    def __init__(self, client, user_id) -> None:
        self.client = client
        self.user_id = user_id
    
    def create(self, timeout=DEFAULT_TIMEOUT): # -> token + expire_time
        user_token = generate_token()
        expire_timestamp = time() + timeout     # 将会在 expire_timestamp 的时间过期
        self.client.hset(SESSION_TOKEN_HASH, self.user_id, user_token)
        self.client.hset(SESSION_EXPIRE_TS_HASH, self.user_id, expire_timestamp)
        return user_token
    
    def validate(self, input_token): 
        # 1. token exist?    expire_time exist?  
        # 2. time()        cmp   expire_time
        # 3. input_token   cmp   token 
        
        user_token = self.client.hget(SESSION_TOKEN_HASH, self.user_id)
        expire_timestamp = self.client.hget(SESSION_EXPIRE_TS_HASH, self.user_id)
        if (user_token is None) or (expire_timestamp is None):
            return SESSION_NOT_LOGIN
        if time() > float(expire_timestamp):
            return SESSION_EXPIRED
        if input_token == user_token:
            return SESSION_TOKEN_CORRECT
        else:
            return SESSION_TOKEN_INCORRECT

    def destroy(self):
        self.client.hdel(SESSION_TOKEN_HASH, self.user_id)
        self.client.hdel(SESSION_EXPIRE_TS_HASH, self.user_id)