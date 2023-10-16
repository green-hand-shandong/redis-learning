def reconstruct_message_list(message_list):
    """
    为了让多条消息能够以更结构化的方式返回给调用者，
    将Redis返回的多条消息从原来的格式：
    [(id1, {k1:v1, k2:v2, ...}), (id2, {k1:v1, k2:v2, ...}), ...]
    转换成以下格式：
    [{id1: {k1:v1, k2:v2, ...}}, {id2: {k1:v1, k2:v2, ...}}, ...]
    """
    result= []

    for id, kvs in message_list:
        result.append({id: kvs})
    return result

def get_message_from_nested_list(lst):
    """
    从嵌套列表中取出消息本体
    """
    return lst[0][1]

class MQ:
    """
    使用Redis流实现的消息队列
    """

    def __init__(self, client, stream_key):
        self.client = client
        self.stream = stream_key

    def add_message(self, key_value_pairs):
        """
        将给定的键值对存入消息中，并返回相应的消息ID
        """
        return self.client.xadd(self.stream, key_value_pairs)

    def get_message(self, message_id):
        """
        根据给定的消息ID返回相应的消息，如果消息不存在则返回None
        """
        reply = self.client.xrange(self.stream, message_id, message_id)
        if len(reply) == 1:
            return get_message_from_nested_list(reply)

    def remove_message(self, message_id):
        """
        根据给定的消息ID删除相应的消息，如果消息不存在则忽略该动作
        """
        self.client.xdel(self.stream, message_id)

    def len(self):
        """
        返回消息队列的长度
        """
        return self.client.xlen(self.stream)

    def get_by_range(self, start_id, end_id, max_item=10):
        """
        根据给定的ID区间范围返回队列中的消息
        """
        reply = self.client.xrange(self.stream, start_id, end_id, max_item)
        return reconstruct_message_list(reply)

    def iterate(self, start_id=0, max_item=10):
        """
        对消息队列进行迭代，返回最多N条大于给定ID的消息
        """
        reply = self.client.xread({self.stream: start_id}, max_item)
        if len(reply) == 0:
            return list()
        else:
            print("reply of iter: ", reply)
            messages = get_message_from_nested_list(reply)
            return reconstruct_message_list(messages)
