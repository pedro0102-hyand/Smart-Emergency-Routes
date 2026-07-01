class Hospital:

    def __init__(self, name: str, latitude: float, longitude: float, node_id: int):

        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.node_id = node_id
    
    def __str__(self):
        return (
            f"Hospital: {self.name}\n"
            f"Latitude: {self.latitude}\n"
            f"Longitude: {self.longitude}\n"
            f"Node ID: {self.node_id}"
        )