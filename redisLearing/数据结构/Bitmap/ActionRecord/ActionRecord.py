def make_action_key(action):
    return "action_recorder::" + action

class ActionRecorder:
    def __init__(self, client, action) -> None:
        self.client = client
        self.bitmap = make_action_key(action)
    
    def perform_by(self, user_id):
        self.client.setbit(self.bitmap, user_id, 1)
    
    def is_performed_by(self, user_id):
        return self.client.getbit(self.bitmap, user_id) == 1
    
    def count_performed(self):
        return self.client.bitcount(self.bitmap)


    