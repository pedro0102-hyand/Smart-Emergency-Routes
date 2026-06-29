import networkx as nx

class GraphManager:

    def __init__(self, graph: nx.MultiDiGraph):

        self.graph = graph

    def get_nodes(self):
 
        return list(self.graph.nodes)

    def get_neighbors(self, node):

        return list(self.graph.neighbors(node))

    def get_coordinates(self, node):

        data = self.graph.nodes[node]

        return (
            data["y"],   # latitude
            data["x"]    # longitude
        )

    def get_edge_length(self, source, target): # comprimento da aresta entre dois nós
   
        edges = self.graph.get_edge_data(source, target)

        if edges is None:
            return None

        return min(
            edge["length"]
            for edge in edges.values()
        )