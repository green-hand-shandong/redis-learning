def get_bitmap_index(index):
    return"#"+str(index)

class CompactCounter:

    def __init__(self, client, key, bit_length, signed=True):
        """
        初始化紧凑计数器，
        其中client参数用于指定客户端，
        key参数用于指定计数器的键名，
        bit_length参数用于指定计数器存储的整数位长，
        signed参数用于指定计数器存储的是有符号整数还是无符号整数
        """
        self.client = client
        self.key = key
        if signed:
            self.type = "i" + str(bit_length)
        else:
            self.type = "u" + str(bit_length)

    def increase(self, index, n=1):
        """
        对索引index上的计数器执行加法操作，然后返回计数器的当前值
        """
        bitmap_index = get_bitmap_index(index)
        result = self.client.execute_command("BITFIELD", self.key, "OVERFLOW",
        "SAT", "INCRBY", self.type, bitmap_index, n)
        return result[0]

    def decrease(self, index, n=1):
        """
        对索引index上的计数器执行减法操作，然后返回计数器的当前值
        """
        bitmap_index = get_bitmap_index(index)
        decrement = -n
        result = self.client.execute_command("BITFIELD", self.key, "OVERFLOW",
        "SAT", "INCRBY", self.type, bitmap_index, decrement)
        return result[0]

    def get(self, index):
        """
        获取索引index上的计数器的当前值
        """
        bitmap_index = get_bitmap_index(index)
        result = self.client.execute_command("BITFIELD", self.key, "GET", self.
        type, bitmap_index)
        return result[0]