class DbIterator:
    def __init__(self, client, match=None, count=None) -> None:
        self.client = client
        self.match = match
        self.count = count
        self.current_cursor = 0
        self.iteration_is_over = False
    
    def next(self):
        if self.iteration_is_over:
            return None
        
        next_cursor, keys = self.client.scan(self.current_cursor, self.match, self.count)
        if next_cursor == 0:
            self.iteration_is_over = True
        self.current_cursor = next_cursor
        return keys