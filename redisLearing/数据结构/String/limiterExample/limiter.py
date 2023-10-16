from redis import Redis
from limiterRedis import Limiter

def get_account_and_password():
    pass
def password_match():
    pass


client = Redis()
key = "wrong_pw_limiter"
myLimit = Limiter(client, key)

myLimit.set_max_executabel_times(3)

while myLimit.still_valid_to_execute():
    acccount, password = get_account_and_password()
    if password_match(acccount, password):
        print(" login successfully ")
        # 密码正确逻辑
    else:
        print(f"login failed, remain {myLimit.remaining_execute_times()}")
        # 密码错误逻辑

# 密码超次数逻辑