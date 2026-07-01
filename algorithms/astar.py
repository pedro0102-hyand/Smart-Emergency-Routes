import heapq
import math
import time
from algorithms.search_algorithm import SearchAlgorithm
from algorithms.search_result import SearchResult
class AStar(SearchAlgorithm):

    def heuristic(
        self,
        node: int,
        goal: int
    ) -> float:
        """
        Calcula a distância geográfica (Haversine)
        entre dois nós do grafo.

        Retorna a distância em metros.
        """

        lat1, lon1 = self.graph_manager.get_coordinates(node)
        lat2, lon2 = self.graph_manager.get_coordinates(goal)

        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)

        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1)
            * math.cos(lat2)
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        raio_terra = 6_371_000  # metros

        return raio_terra * c

    def search(
        self,
        start: int,
        goal: int
    ) -> SearchResult:

        start_time = time.perf_counter()

        priority_queue = []

        heapq.heappush(
            priority_queue,
            (
                0,
                start
            )
        )

        g_score = {
            start: 0.0
        }

        parents = {}

        visited = set()

        visited_nodes = 0

        while priority_queue:

            _, current = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)

            visited_nodes += 1

            if current == goal:
                break

            for neighbor in self.graph_manager.get_neighbors(current):

                edge_cost = self.graph_manager.get_edge_length(
                    current,
                    neighbor
                )

                tentative_g = (
                    g_score[current]
                    + edge_cost
                )

                if (
                    neighbor not in g_score
                    or tentative_g < g_score[neighbor]
                ):

                    g_score[neighbor] = tentative_g

                    parents[neighbor] = current

                    f_score = (
                        tentative_g
                        + self.heuristic(
                            neighbor,
                            goal
                        )
                    )

                    heapq.heappush(
                        priority_queue,
                        (
                            f_score,
                            neighbor
                        )
                    )

        execution_time = (
            time.perf_counter()
            - start_time
        )

        path = self._reconstruct_path(
            parents,
            start,
            goal
        )

        return SearchResult(
            path=path,
            visited_nodes=visited_nodes,
            path_cost=g_score.get(goal, 0.0),
            execution_time=execution_time
        )