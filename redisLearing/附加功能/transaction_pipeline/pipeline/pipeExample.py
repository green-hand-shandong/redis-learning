from redis import Redis
client = Redis(decode_responses=True)
pipe = client.pipeline(transaction=False)
print("prepare pipeline : -------------------- ")
print(pipe.set("msg", "hello this is message"))
print(pipe.incrby("pv_counter::blog", 100))
print(pipe.sadd("a", "b", "c", "d"))
print("pipeline : -------------------- ")
print(pipe.execute())
