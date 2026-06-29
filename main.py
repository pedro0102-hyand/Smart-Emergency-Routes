from graph.map_loader import MapLoader
from graph.graph_info import GraphInfo
from graph.graph_manager import GraphManager


def main():

    loader = MapLoader()

    graph = loader.load_city(
        "Copacabana, Rio de Janeiro, Brazil"
    )

    info = GraphInfo(graph)
    info.summary()
    info.show_first_node()
    info.show_neighbors()
    info.show_edge_attributes()

    # Testando o GraphManager
    manager = GraphManager(graph)

    node = manager.get_nodes()[0]

    print("\n===== TESTE DO GRAPH MANAGER =====")
    print(f"Nó: {node}")
    print(f"Coordenadas: {manager.get_coordinates(node)}")

    neighbors = manager.get_neighbors(node)
    print(f"Vizinhos: {neighbors}")

    if neighbors:
        print(
            f"Comprimento da aresta: {manager.get_edge_length(node, neighbors[0])} m"
        )


if __name__ == "__main__":
    main()