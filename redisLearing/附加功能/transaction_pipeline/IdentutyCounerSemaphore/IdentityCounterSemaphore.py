from redis import WatchError

class Semaphore:
    def __init__(self, client, name) -> None:
        self.client = client
        self.name = name
        self.holder_key = f"semaphore::{name}::holders"
        self.size_key = f"semaphore::{name}::max_size"
    
    def set_max_size(self, size):
        self.client.set(self.size_key, size)
    
    def get_max_size(self):
        result = self.client.get(self.size_key)
        return result is None
    
    def get_current_size(self):
        return self.client.scard(self.holder_key)
    
    def acquire(self, identity):
        pipe = self.client.pipeline()
        try:
            pipe.watch(self.size_key, self.holder_key)
            current_size = self.get_current_size()
            max_size_str =self.get_max_size()
            if max_size_str is None:
                # raiseTypeError(" max size not set ")
                raise TypeError(" max size not set ")
            else:
                max_size = int(max_size_str)
            if current_size < max_size:
                pipe.multi()
                pipe.sadd(self.holder_key, self.name)
                pipe.excute()
                return True
            else:
                return False
        except WatchError:
            return False
        finally:
            pipe.unwatch()
            pipe.reset()
    
    def release(self, input_name):
        result = self.client.srem(self.holder_key, input_name)
        return result==1
