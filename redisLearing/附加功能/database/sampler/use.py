from db_random_creator import create_random_type_keys
from db_sampler import DbSampler
from redis import Redis

client = Redis(decode_responses=True)
sp = DbSampler(client)

# create_random_type_keys(client, 1000)
sp.sample()
