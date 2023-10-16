import random
from redis import Redis
from hashlib import sha256

def generate_new_pw():
    random_string = str(random.getrandbits(256)).encode("utf-8")
    return sha256(random_string).hexdigest()
def reset_user_pw(origin, new):
    # 旧数据库
    origin_db = Redis(db=origin)
    # 新数据库 
    new_db = Redis(db=new)
    for key in origin_db.scan_iter(match="user::*"):
        user_data = origin_db.hgetall(key) # user
        user_data["password"] = generate_new_pw() # pw
        new_db.hmset(key, user_data)
    
    origin_db.swapdb(origin, new)
    new_db.flushdb(asynchronous=True)