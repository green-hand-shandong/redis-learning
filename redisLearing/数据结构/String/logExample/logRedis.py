
LOG_SEPERATOR = "\n"

class Log:
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    
    def add(self, new_log):
        new_log += LOG_SEPERATOR
        self.client.append(self.key, new_log)
    
    def all(self):
        all_logs = self.client.get(self.key)
        if all_logs is not None:
            log_list = all_logs.split(LOG_SEPERATOR)
            log_list.remove("") # split会在结果中包含一个空串
            return log_list
        return []
    