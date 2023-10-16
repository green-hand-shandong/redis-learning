from redis import Redis

client = Redis()
print(f"ping : {client.ping()}")

