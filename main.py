from graph.map_loader import MapLoader
from graph.graph_info import GraphInfo
from graph.graph_manager import GraphManager

from algorithms.bfs import BFS


def main():

    # Carrega o mapa
    loader = MapLoader()

    graph = loader.load_city(
        "Copacabana, Rio de Janeiro, Brazil"
    )

    # Exibe informações do grafo
    info = GraphInfo(graph)

    info.summary()
    info.show_first_node()
    info.show_neighbors()
    info.show_edge_attributes()

    # Cria o GraphManager
    manager = GraphManager(graph)

    # Teste do GraphManager
    node = manager.get_nodes()[0]

    print("\n" + "=" * 50)
    print("TESTE DO GRAPH MANAGER")
    print("=" * 50)

    print(f"Nó: {node}")
    print(f"Coordenadas: {manager.get_coordinates(node)}")

    neighbors = manager.get_neighbors(node)

    print(f"Vizinhos: {neighbors}")

    if neighbors:
        print(
            f"Comprimento da aresta: "
            f"{manager.get_edge_length(node, neighbors[0]):.2f} m"
        )

    # ======================================================
    # Teste do BFS
    # ======================================================

    nodes = manager.get_nodes()

    start = nodes[0]
    goal = nodes[50]

    bfs = BFS(manager)

    result = bfs.search(start, goal)

    print("\n" + "=" * 50)
    print("RESULTADO DO BFS")
    print("=" * 50)

    print(f"Origem          : {start}")
    print(f"Destino         : {goal}")
    print(f"Nós visitados   : {result.visited_nodes}")
    print(f"Custo           : {result.path_cost}")
    print(f"Tempo           : {result.execution_time:.6f} s")

    print("\nCaminho encontrado:")

    if result.path:

        for i, node in enumerate(result.path, start=1):
            print(f"{i:02d} -> {node}")

    else:
        print("Nenhum caminho encontrado.")


if __name__ == "__main__":
    main()