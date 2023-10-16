def make_edge_name_from_vertexs(start, end):
    return str(start) + "->" + str(end)
def decompose_vrtexs_from_edge_name(name):
    return name.split("->")

class Graph:
    '''
    self.key   edge(start->end)   weight
    '''
    def __init__(self, client, key) -> None:
        self.client = client
        self.key = key
    def add_edge(self, start, end, weight):
        edge = make_edge_name_from_vertexs(start, end)
        self.client.hset(self.key, edge, weight)
    def remove_edge(self, start, end):
        edge = make_edge_name_from_vertexs(start, end)
        return self.client.hdel(self.key, edge)
    def get_edge_weight(self, start, end):
        edge = make_edge_name_from_vertexs(start, end)
        return self.client.hget(self.key, edge)
    def has_edge(self, start, end):
        edge = make_edge_name_from_vertexs(start, end)
        return self.client.hexists(self.key, edge)
    
    def add_multi_edges(self, *tuples):
        '''
        tuples : (start, end, weight) * n
        '''
        nodes_and_weights = {} #  dict{}    edge : weight
        for start, end, weight in tuples:
            edge = make_edge_name_from_vertexs(start, end)
            nodes_and_weights[edge] = weight
        self.client.hmset(self.key, nodes_and_weights)

    def get_multi_edge_weights(self, *tuples):
        edge_list = []          # list[]    edge
        for start, end in tuples:
            edge = make_edge_name_from_vertexs(start, end)
            edge_list.append(edge)
        return self.client.hmget(self.key, edge_list)

    def get_all_edges(self):
        edges = self.client.hkeys(self.key)
        result = set()
        for e in edges:
            start, end = decompose_vrtexs_from_edge_name(e)
            result.add((start, end))
        return result
    
    def get_all_edges_weights(self):
        edges_and_weight = self.client.hgetall(self.key)
        result = set()
        for edge, weight in edges_and_weight.items():
            start, end = decompose_vrtexs_from_edge_name(edge)
            result.add((start, end, weight))
        return result    
