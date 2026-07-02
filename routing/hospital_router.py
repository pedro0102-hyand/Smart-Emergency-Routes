from algorithms.astar import AStar

class HospitalRouter:

    def __init__(self, graph_manager, hospital_manager):

        self.graph_manager = graph_manager
        self.hospital_manager = hospital_manager
        self.astar = AStar(graph_manager)

    def find_best_hospital(self, start_node):

        best_hospital = None
        best_result = None

        hospitals = self.hospital_manager.get_hospitals()

        for hospital in hospitals:

            result = self.astar.search(
                start_node,
                hospital.node_id
            )

            if not result.path:
                continue

            if best_result is None:

                best_result = result
                best_hospital = hospital

            elif result.path_cost < best_result.path_cost:

                best_result = result
                best_hospital = hospital

        return best_hospital, best_result