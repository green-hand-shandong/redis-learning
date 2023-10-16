VALUE_OF_LOCK = "lock"

class TimingLock:
    def __init__(self, client, key) -> None:
        self.client = client        
        self.key = key
    
    def acquire(self, timeout):
        # 获取lock， 但是ex=timeout， 并且只能新建不能操作已有的lock
        result = self.client.set(self.key, VALUE_OF_LOCK, ex=timeout, nx=True)
        return result is not None
    
    def release(self):
        return self.client.delete(self.key) == 1