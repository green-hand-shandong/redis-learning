def make_record_key(origin):
    return "forward_to_record::{0}".format(origin)  # index 0

class Path:
    def __init__(self, client) -> None:
        self.client = client
    
    def forward_to(self, origin, destination):
        '''
        记录一次 origin 到 destination 的访问 
        origin : z
        destination : member
        计数 : score
        '''
        key = make_record_key(origin)
        self.client.zincrby(key, 1, destination)
        #           ZINCRBY sorted_set, increment, member
    
    def pagging_record(self, origin, number, count, with_time=False):
        key = make_record_key(origin)
        start_index = (number-1) * count
        end_index = number*count - 1
        return self.client.zrevrange(key, start_index, end_index, 
                                     withscores=with_time, score_cast_func=int)
