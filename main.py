from graph.map_loader import MapLoader
from graph.graph_info import GraphInfo


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


if __name__ == "__main__":
    main()