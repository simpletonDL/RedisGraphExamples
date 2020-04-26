from redis import Redis
from redisgraph import Graph

# print all graphs
# print(Redis().keys())

GRAPH = "pizza.txt"

NODE_COUNT = """
MATCH () RETURN COUNT(*)
"""

EDGE_STAT = """
match ()-[r]-() return type(r), count(*)
"""

RDF_QUERY_1 = """
PATH PATTERN s = ()-/ [<:SCO ~s :SCO] | [<:T ~s :T] | [<:SCO :SCO] | [<:T :T] /-()
MATCH (v)-/ ~s /->(to)
RETURN COUNT(*)
"""

WORSTCASE_QUERY = """
PATH PATTERN s = ()-/ [:A ~s :B] | [:A :B] /-()
MATCH (v)-/ ~s /->(to)
RETURN COUNT(*)
"""

FREE_SCALE_QUERY = """
path pattern S = ()-/ [:a ~S :d] | [:a ~X :d] /-()
path pattern X = ()-/ [:b ~X :c] | [:b :c] /-()
MATCH (v)-/ ~S /->(to)
RETURN COUNT(*)
"""

r = Redis()
graph = Graph(GRAPH, r)

res = graph.query(RDF_QUERY_1)
res.pretty_print()
