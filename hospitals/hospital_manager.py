import osmnx as ox
from hospitals.hospital import Hospital
class HospitalManager:

    def __init__(
        self,
        graph,
        city
    ):

        self.graph = graph
        self.city = city
        self.hospitals = []

    # =====================================================
    # Carrega hospitais do OpenStreetMap
    # =====================================================

    def load_hospitals(self):

        tags = {
            "amenity": "hospital"
        }

        hospitals = ox.features_from_place(
            self.city,
            tags
        )

        self.hospitals.clear()

        for _, row in hospitals.iterrows():

            name = row.get(
                "name",
                "Hospital sem nome"
            )

            geometry = row.geometry

            if geometry.geom_type == "Point":

                latitude = geometry.y
                longitude = geometry.x

            else:

                point = geometry.centroid

                latitude = point.y
                longitude = point.x

            node = ox.distance.nearest_nodes(
                self.graph,
                longitude,
                latitude
            )

            self.hospitals.append(
                Hospital(
                    name=name,
                    node_id=node,
                    latitude=latitude,
                    longitude=longitude
                )
            )

        self._remove_duplicates()

    # =====================================================
    # Remove hospitais duplicados
    # =====================================================

    def _remove_duplicates(self):

        unique_nodes = set()
        unique_names = set()

        filtered = []

        for hospital in self.hospitals:

            normalized_name = (
                hospital.name
                .strip()
                .lower()
            )

            if hospital.node_id in unique_nodes:
                continue

            if normalized_name in unique_names:
                continue

            unique_nodes.add(
                hospital.node_id
            )

            unique_names.add(
                normalized_name
            )

            filtered.append(
                hospital
            )

        filtered.sort(
            key=lambda hospital: hospital.name
        )

        self.hospitals = filtered

    # =====================================================
    # Exibe hospitais
    # =====================================================

    def show_hospitals(self):

        print("\n" + "=" * 50)
        print("HOSPITAIS ENCONTRADOS")
        print("=" * 50)

        print(
            f"Quantidade: {len(self.hospitals)}"
        )

        for index, hospital in enumerate(
            self.hospitals,
            start=1
        ):

            print("\n----------------------------")
            print(f"Hospital {index}")
            print("----------------------------")

            print(f"Nome      : {hospital.name}")
            print(f"Nó        : {hospital.node_id}")
            print(f"Latitude  : {hospital.latitude}")
            print(f"Longitude : {hospital.longitude}")

    # =====================================================
    # Retorna todos os hospitais
    # =====================================================

    def get_hospitals(self):

        return self.hospitals

    # =====================================================
    # Retorna um hospital pelo índice
    # =====================================================

    def get_hospital(
        self,
        index
    ):

        return self.hospitals[index]