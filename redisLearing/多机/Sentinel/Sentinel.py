from redis.sentinel import Sentinel

s = Sentinel([('localhost', 26379)])

s.discover_master('website_db')     # 查看主服务器地址
# ('127.0.0.1', 6379)
s.discover_slaves('website_db')     # 查看主服务器的从服务器地址
# [('127.0.0.1', 6380), ('127.0.0.1', 6381)]

master = s.master_for('website_db', decode_responses=True)  # 主服务器实例
master.set("msg", "hello world! ")
# True
slave = s.slave_for('website_db', decode_responses=True)    # 从服务器实例
slave.get('msg')
# 'hello world! '

