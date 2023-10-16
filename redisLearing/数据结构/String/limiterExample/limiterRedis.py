class Limiter:
    def __init__(self, cli, k) -> None:
        self.client = cli
        self.key = k
    
    def set_max_executabel_times(self, n):
        self.client.set(self.key, n) 
    
    def still_valid_to_execute(self):
        num = self.client.decr(self.key)
        return num >= 0
    
    def remaining_execute_times(self):
        num = int(self.client.get(self.key))
        return 0 if num < 0 else num
    