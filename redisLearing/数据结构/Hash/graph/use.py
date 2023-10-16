from graph import Graph
from redis import Redis

client = Redis(decode_responses=True)
key = "test-graph"
graph = Graph(client, key)

print(graph.add_edge("a", "b", 30))
print(graph.add_multi_edges(("b", "c", 40), ("c", "a", 50)))
print(graph.get_edge_weight("a", "b"))
print(graph.has_edge("a", "b"))
print(graph.has_edge("b", "a"))
print(graph.get_all_edges())
print(graph.get_all_edges_weights())