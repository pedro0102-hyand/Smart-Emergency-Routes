import osmnx as ox
from hospitals.hospital import Hospital

class HospitalManager:

    def __init__(
        self,
        graph,
        place_name: str
    ):

        self.graph = graph
        self.place_name = place_name

        self.hospitals = []

    def load_hospitals(self):

        """
        Busca hospitais no OpenStreetMap.
        """

        tags = {
            "amenity": "hospital"
        }

        gdf = ox.features_from_place(
            self.place_name,
            tags
        )

        self.hospitals.clear()

        for _, row in gdf.iterrows():

            geometry = row.geometry

            if geometry.geom_type == "Point":

                latitude = geometry.y
                longitude = geometry.x

            else:

                centroid = geometry.centroid

                latitude = centroid.y
                longitude = centroid.x

            node = ox.distance.nearest_nodes(
                self.graph,
                longitude,
                latitude
            )

            name = row.get(
                "name",
                "Hospital sem nome"
            )

            hospital = Hospital(
                name=name,
                latitude=latitude,
                longitude=longitude,
                node_id=node
            )

            self.hospitals.append(hospital)

    def get_hospitals(self):

        return self.hospitals

    def show_hospitals(self):

        print("\n" + "=" * 50)
        print("HOSPITAIS ENCONTRADOS")
        print("=" * 50)

        print(
            f"Quantidade: {len(self.hospitals)}"
        )

        for i, hospital in enumerate(
            self.hospitals,
            start=1
        ):

            print("\n----------------------------")
            print(f"Hospital {i}")
            print("----------------------------")

            print(f"Nome      : {hospital.name}")
            print(f"Nó        : {hospital.node_id}")
            print(f"Latitude  : {hospital.latitude}")
            print(f"Longitude : {hospital.longitude}")