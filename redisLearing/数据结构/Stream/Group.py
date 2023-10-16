from MQ import reconstruct_message_list, get_message_from_nested_list

class Group:
    def __init__(self, client, stream, group) -> None:
        self.client = client
        self.stream = stream
        self.group = group
    
    def create(self, start_id):
        self.client.xgroup_create(self.stream, self.group, start_id)

    def destroy(self):
        self.client.xgrou_destroy(self.stream, self.group)
    
    def read_message(self, consumer, id, count=1):
        reply = self.client.xreadgroup(self.group, consumer, {self.stream:id}, count)
        if reply == 0:
            return list()
        else:
            message = get_message_from_nested_list(reply)
            return reconstruct_message_list(message)

    def ack_message(self, id):
        self.client.xack(self.stream, self.group, id)
    
    def info(self):
        for group_info in self.client.xinfo_groups(self.stream):
            if group_info["name"] == self.group:
                return group_info
            else:
                return dict()
    
    def consumer_info(self):
        return self.client.xinfo_consumers(self.stream, self.group)
    
    def delete_consumer(self, consumer):
        self.client.xgroup_delconsumer(self.stream, self.group, consumer)
    
    