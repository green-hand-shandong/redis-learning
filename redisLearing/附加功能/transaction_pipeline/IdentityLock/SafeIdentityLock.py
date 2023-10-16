from redis import WatchError
    
class safeIdentityLock:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key    = key
    
    def acquire(self, identity, timeout):
        result = self.client.set(self.key, identity, ex=timeout, nx=True)
        return result is not None

    def release(self, input_identity):
        pipe = self.client.pipeline()
        try:
            pipe.watch(self.key)
        
            # lock_identity = self.client.get(self.key)
            lock_identity = pipe.get(self.key)
            if lock_identity is None:               # 已释放
                return True
            elif lock_identity == input_identity:   # 允许释放
                # self.client.delete(self.key)
                pipe.delete(self.key)
                pipe.excute()
                return True
            else:                                   # 拒绝释放
                return False
        except WatchError:
            return False
        finally:
            pipe.unwatch()
            pipe.reset()
        
