def make_todo_list_keys(user_id):
    return user_id + "::todo"
def make_done_list_keys(user_id):
    return user_id + "::done"

class TodoList:
    def __init__(self, client, user_id) -> None:
        self.client = client
        self.user_id = user_id
        self.todo_list = make_todo_list_keys(user_id)
        self.done_list = make_done_list_keys(user_id)
    
    def add(self, event):
        self.client.lpush(self.todo_list, event)
    
    def remove(self, event):
        self.client.lrem(self.todo_list, 0, event) # LREM list count elem
    
    def done(self, event):
        self.remove(event)
        self.client.lpush(self.done_list, event)

    def show_todo_list(self):
        return self.client.lrange(self.todo_list, 0, -1)

    def show_done_list(self):
        return self.client.lrange(self.done_list, 0, -1)