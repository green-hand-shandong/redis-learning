def type_sample_result(type_name, type_counter, db_size):
    return f"{type_name}: {type_counter},  {type_counter*100.0/db_size}% of the total"

class DbSampler:
    def __init__(self, client) -> None:
        self.client = client
    
    def sample(self):
        type_counter = {
            "string":0,
            "list":0,
            "hash":0,
            "set":0,
            "zset":0,
            "stream":0
        }
        for key in self.client.scan_iter():
            type = self.client.type(key)
            type_counter[type] += 1
        db_size = self.client.dbsize()

        print(f"Sample {db_size} keys.")
        print(type_sample_result("String", type_counter["string"], db_size))
        print(type_sample_result("List", type_counter["list"], db_size))
        print(type_sample_result("Hash", type_counter["hash"], db_size))
        print(type_sample_result("Set", type_counter["set"], db_size))
        print(type_sample_result("Zset", type_counter["zset"], db_size))
        print(type_sample_result("Stream", type_counter["stream"], db_size))



