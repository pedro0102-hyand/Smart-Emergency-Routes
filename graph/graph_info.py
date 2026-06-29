from typing import Any
import networkx as nx


class GraphInfo:
  
    def __init__(self, graph: nx.MultiDiGraph) -> None:

        self.graph = graph

    def summary(self) -> None:
   

        print("\n" + "=" * 50)
        print("INFORMAÇÕES DO GRAFO")
        print("=" * 50)

        print(f"Tipo do grafo : {type(self.graph).__name__}")
        print(f"Nós           : {self.graph.number_of_nodes()}")
        print(f"Arestas       : {self.graph.number_of_edges()}")

    def show_first_node(self) -> None:
     

        first_node = next(iter(self.graph.nodes))

        print("\nPrimeiro nó")
        print("-" * 30)
        print(f"ID: {first_node}")

        print("\nAtributos:")

        for key, value in self.graph.nodes[first_node].items():
            print(f"{key}: {value}")

    def show_neighbors(self) -> None:
      

        first_node = next(iter(self.graph.nodes))

        neighbors = list(self.graph.neighbors(first_node))

        print("\nVizinhos")
        print("-" * 30)

        print(f"Nó: {first_node}")
        print(f"Quantidade: {len(neighbors)}")

        for neighbor in neighbors:
            print(neighbor)

    def show_edge_attributes(self) -> None:
    

        edge = next(iter(self.graph.edges(keys=True, data=True)))

        origin, destination, key, attributes = edge

        print("\nPrimeira aresta")
        print("-" * 30)

        print(f"Origem : {origin}")
        print(f"Destino: {destination}")

        print("\nAtributos:")

        for name, value in attributes.items():
            print(f"{name}: {value}")