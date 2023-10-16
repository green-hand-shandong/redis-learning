from redis import Redis
from CompactCounter import CompactCounter
client = Redis()
counter = CompactCounter(client, "login_counter", 16, False)  # 创建计数器
print(counter.increase(10086))  # 记录第1次登录
print(counter.increase(10086))  # 记录第2次登录
print(counter.get(10086))        # 获取登录次数
