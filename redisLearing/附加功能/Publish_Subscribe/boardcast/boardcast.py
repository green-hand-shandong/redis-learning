class Boardcast:
    def __init__(self, client, topic) -> None:
        self.client = client
        self.topic  = topic
        self.pubsub = self.client.pubsub()
        self.pubsub.subscribe(self.topic)
        self.pubsub.get_message(timeout=1)

    def publish(self, content):                              # 创建topic
        self.client.publish(self.topic, content)

    def listen(self, timeout=0):                             # 监听topic 
        result = self.pubsub.get_message(timeout=timeout)
        if result is not None:
            return result["data"]
    
    def status(self):
        result = self.client.pubsub_numsub(self.topic)
        return result[0][1]

    def close(self):
        self.pubsub.unsubscrible(self.topic)