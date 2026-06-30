import heapq
import time
from algorithms.search_algorithm import SearchAlgorithm
from algorithms.search_result import SearchResult


class Dijkstra(SearchAlgorithm):

    def search(self, start: int, goal: int) -> SearchResult:

        start_time = time.perf_counter()

        queue = [(0.0, start)]

        distances = {
            start: 0.0
        }

        parents = {}

        visited = set()

        visited_nodes = 0

        while queue:

            current_distance, current = heapq.heappop(queue)

            if current in visited:
                continue

            visited.add(current)
            visited_nodes += 1

            if current == goal:
                break

            for neighbor in self.graph_manager.get_neighbors(current):

                edge_length = self.graph_manager.get_edge_length(
                    current,
                    neighbor
                )

                new_distance = current_distance + edge_length

                if (
                    neighbor not in distances
                    or
                    new_distance < distances[neighbor]
                ):

                    distances[neighbor] = new_distance

                    parents[neighbor] = current

                    heapq.heappush(
                        queue,
                        (
                            new_distance,
                            neighbor
                        )
                    )

        execution_time = time.perf_counter() - start_time

        path = self._reconstruct_path(
            parents,
            start,
            goal
        )

        return SearchResult(

            path=path,

            visited_nodes=visited_nodes,

            path_cost=distances.get(goal, 0),

            execution_time=execution_time
        )