from MQ import MQ
from redis import Redis
from Group import Group

client = Redis(decode_responses=True)
mq = MQ(client, "mq1")
group = Group(client, "mq1", "group1")

# ids = []
# for i in range(10):
#     key = "key{0}".format(i)
#     value = "value{0}".format(i)
#     msg = {key : value}
#     ids.append(mq.add_message(msg))

# print(ids)

# print(mq.get_message(ids[0]))
# print(mq.get_message(ids[1]))
# print(mq.get_by_range("-", "+", 3))
# print(mq.iterate(0, 3))
# print(mq.iterate(ids[0], 3))


# group.create("1695889963814-0")
print(group.read_message("consumer1", "0"))  # ">"表示从上次读取消息的位置之后开始读取。
print(group.read_message("consumer1", "1"))  # ">"表示从上次读取消息的位置之后开始读取。
# print(group.info())
# print(group.consumer_info())