from pathlib import Path

import folium


class RouteVisualizer:

    def __init__(self, graph):
        self.graph = graph

    def draw_route(
        self,
        path: list[int],
        file_name: str = "route.html",
        color: str = "blue"
    ):

        if not path:
            print("Nenhuma rota encontrada.")
            return

        # Centro do mapa
        first = path[0]

        lat = self.graph.nodes[first]["y"]
        lon = self.graph.nodes[first]["x"]

        mapa = folium.Map(
            location=[lat, lon],
            zoom_start=16
        )

        coordinates = []

        for node in path:

            y = self.graph.nodes[node]["y"]
            x = self.graph.nodes[node]["x"]

            coordinates.append((y, x))

        # Desenha a rota
        folium.PolyLine(
            coordinates,
            color=color,
            weight=6,
            opacity=0.8
        ).add_to(mapa)

        # Origem
        folium.Marker(
            coordinates[0],
            popup="Origem",
            icon=folium.Icon(color="green")
        ).add_to(mapa)

        # Destino
        folium.Marker(
            coordinates[-1],
            popup="Destino",
            icon=folium.Icon(color="red")
        ).add_to(mapa)

        output_dir = Path("output")

        output_dir.mkdir(exist_ok=True)

        output_path = output_dir / file_name

        mapa.save(output_path)

        print(f"\nMapa salvo em {output_path.resolve()}")