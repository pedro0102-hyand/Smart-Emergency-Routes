from dataclasses import dataclass


@dataclass
class Hospital:
    name: str
    latitude: float
    longitude: float
    node_id: int

    def __str__(self):
        return (
            f"Hospital: {self.name}\n"
            f"Latitude: {self.latitude}\n"
            f"Longitude: {self.longitude}\n"
            f"Node ID: {self.node_id}"
        )