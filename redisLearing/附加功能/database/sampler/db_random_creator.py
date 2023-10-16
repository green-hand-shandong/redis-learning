import random

def create_string(client, key):
    client.set(key, "")
def create_hash(client, key):
    client.hset(key, "", "")
def create_list(client, key):
    client.rpush(key, "")
def create_set(client, key):
    client.sadd(key, "")
def create_zset(client, key):
    client.zadd(key, {"":0})
def create_stream(client, key):
    client.xadd(key, {"":""})



def create_random_type_keys(client, number):
    for i in range(number):
        key = f"key:{i}"
        create_key_func = random.choice([create_string, create_hash, create_list, 
                                         create_set, create_zset, create_stream])
        create_key_func(client, key)