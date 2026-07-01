from graph.map_loader import MapLoader
from graph.graph_info import GraphInfo
from graph.graph_manager import GraphManager
from hospitals.hospital_manager import HospitalManager
from algorithms.bfs import BFS
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from visualization.route_visualizer import RouteVisualizer


def main():

    city = "Copacabana, Rio de Janeiro, Brazil"

    # ======================================================
    # Carrega o mapa
    # ======================================================

    loader = MapLoader()

    graph = loader.load_city(city)

    # ======================================================
    # Informações do grafo
    # ======================================================

    info = GraphInfo(graph)

    info.summary()
    info.show_first_node()
    info.show_neighbors()
    info.show_edge_attributes()

    # ======================================================
    # GraphManager
    # ======================================================

    manager = GraphManager(graph)

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
    # Hospitais
    # ======================================================

    hospital_manager = HospitalManager(
        graph,
        city
    )

    hospital_manager.load_hospitals()

    hospital_manager.show_hospitals()

    # ======================================================
    # Nós de origem e destino
    # ======================================================

    nodes = manager.get_nodes()

    start = nodes[0]
    goal = nodes[50]

    # ======================================================
    # BFS
    # ======================================================

    bfs = BFS(manager)

    bfs_result = bfs.search(start, goal)

    print("\n" + "=" * 50)
    print("RESULTADO DO BFS")
    print("=" * 50)

    print(f"Origem          : {start}")
    print(f"Destino         : {goal}")
    print(f"Nós visitados   : {bfs_result.visited_nodes}")
    print(f"Custo           : {bfs_result.path_cost}")
    print(f"Tempo           : {bfs_result.execution_time:.6f} s")

    print("\nCaminho encontrado:")

    if bfs_result.path:

        for i, node in enumerate(
            bfs_result.path,
            start=1
        ):
            print(f"{i:02d} -> {node}")

    else:
        print("Nenhum caminho encontrado.")

    # ======================================================
    # Dijkstra
    # ======================================================

    dijkstra = Dijkstra(manager)

    dijkstra_result = dijkstra.search(
        start,
        goal
    )

    print("\n" + "=" * 50)
    print("RESULTADO DO DIJKSTRA")
    print("=" * 50)

    print(f"Origem          : {start}")
    print(f"Destino         : {goal}")
    print(f"Nós visitados   : {dijkstra_result.visited_nodes}")
    print(f"Distância       : {dijkstra_result.path_cost:.2f} metros")
    print(f"Tempo           : {dijkstra_result.execution_time:.6f} s")

    print("\nCaminho encontrado:")

    if dijkstra_result.path:

        for i, node in enumerate(
            dijkstra_result.path,
            start=1
        ):
            print(f"{i:02d} -> {node}")

    else:
        print("Nenhum caminho encontrado.")

    # ======================================================
    # A*
    # ======================================================

    astar = AStar(manager)

    astar_result = astar.search(
        start,
        goal
    )

    print("\n" + "=" * 50)
    print("RESULTADO DO A*")
    print("=" * 50)

    print(f"Origem          : {start}")
    print(f"Destino         : {goal}")
    print(f"Nós visitados   : {astar_result.visited_nodes}")
    print(f"Distância       : {astar_result.path_cost:.2f} metros")
    print(f"Tempo           : {astar_result.execution_time:.6f} s")

    print("\nCaminho encontrado:")

    if astar_result.path:

        for i, node in enumerate(
            astar_result.path,
            start=1
        ):
            print(f"{i:02d} -> {node}")

    else:
        print("Nenhum caminho encontrado.")

    # ======================================================
    # Visualização das rotas
    # ======================================================

    visualizer = RouteVisualizer(graph)

    visualizer.draw_route(
        bfs_result.path,
        file_name="bfs_route.html",
        color="blue"
    )

    visualizer.draw_route(
        dijkstra_result.path,
        file_name="dijkstra_route.html",
        color="red"
    )

    visualizer.draw_route(
        astar_result.path,
        file_name="astar_route.html",
        color="green"
    )


if __name__ == "__main__":
    main()