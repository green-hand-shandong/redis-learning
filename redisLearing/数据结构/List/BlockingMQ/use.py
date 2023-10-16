from redis import Redis
from BlockingMQ import BlockingMQ


message_queue = "xiwa"

client_producer = Redis(decode_responses=True)
producer = BlockingMQ(client_producer, message_queue)
print(producer.add_message("1"))
print(producer.add_message("2"))
print(producer.add_message("3"))
print(producer.len())

client_consumer = Redis(decode_responses=True)
consumer = BlockingMQ(client_consumer, message_queue)
print(consumer.get_message(timeout=1))
print(consumer.get_message(timeout=2))
print(consumer.get_message(timeout=3))
print(consumer.get_message(timeout=4))
print(consumer.len())