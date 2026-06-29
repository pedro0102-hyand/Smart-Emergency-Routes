from graph.map_loader import MapLoader


def main():

    loader = MapLoader()

    graph = loader.load_city(
        "Copacabana, Rio de Janeiro, Brazil"
    )

    print("\n===== Estatísticas =====")

    print(f"Nós: {len(graph.nodes)}")
    print(f"Arestas: {len(graph.edges)}")


if __name__ == "__main__":
    main()