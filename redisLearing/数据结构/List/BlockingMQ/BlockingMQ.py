class BlockingMQ:
    def __init__(self, client, mq) -> None:
        self.client = client
        self.mq_key = mq
    
    def add_message(self, message):
        self.client.rpush(self.mq_key, message)

    def get_message(self, timeout=0):
        result = self.client.blpop(self.mq_key, timeout)
        if result is not None:
            source_queue, poped_item = result
            return poped_item
        else:
            return None

    def len(self):
        return self.client.llen(self.mq_key)