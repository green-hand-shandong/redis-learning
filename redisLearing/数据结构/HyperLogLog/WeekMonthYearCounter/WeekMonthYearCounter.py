class UniqueCounterMerge:
    def __init__(self, client) -> None:
        self.client = client

    def merge(self, destination, *hyperloglog):
        self.client.pfmerge(destination, *hyperloglog)
