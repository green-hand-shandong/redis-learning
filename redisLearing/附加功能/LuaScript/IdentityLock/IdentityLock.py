class Identity:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def acquire(self, identity, timeout):
        result = self.client.set(self.key, identity, ex=timeout, nx=True)
        return result is None
    
    def release(self, input_identity):
        script = '''
        local key = KEYS[1]
        local input_identity = ARGV[1]
        local lock_identity = redis.call('GET', key)
        if lock_identity == false then
            return true
        elseif input_identity == lock_identity then
            redis.call('DEL', key)
            return true
        else
            return false
        end
        '''
        result = self.client.eval(script, 1, self.key, input_identity)
        return result == 1
