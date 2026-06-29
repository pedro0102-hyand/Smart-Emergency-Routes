import osmnx as ox
from pathlib import Path

class MapLoader:

    def __init__(self, cache_directory = "data/maps")-> None:

        self.cache_directory = Path(cache_directory)
        self.cache_directory.mkdir(parents=True, exist_ok=True)

    def load_city(self, city_name: str):

        file_name = city_name.lower().replace(", ", "")
        file_name = file_name.replace(" ", "_")
        file_path = self.cache_directory / f"{file_name}.graphml"

        if file_path.exists():

            graph = ox.load_graphml(file_path)

        else:

            graph = ox.graph_from_place(city_name, network_type='drive')
            ox.save_graphml(graph, file_path)

        return graph