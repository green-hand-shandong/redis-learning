from redis import Redis
from  boardcast import Boardcast
import time
# channel
client = Redis()
topic = "chat::peter"

# 订阅者
pc = Boardcast(client, topic)
mac = Boardcast(client, topic)
phone = Boardcast(client, topic)
pad = Boardcast(client, topic)

# 发布者
jack = Boardcast(client, topic)


# 发布消息
jack.publish("hello, this is jack")


# time.sleep(5)


print(pc.listen())
print(mac.listen())
print(pad.listen())


