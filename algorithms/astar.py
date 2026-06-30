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
       

        y1, x1 = self.graph_manager.get_coordinates(node)
        y2, x2 = self.graph_manager.get_coordinates(goal)

        return math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

    def search(
        self,
        start: int,
        goal: int
    ) -> SearchResult:

        start_time = time.perf_counter()

        queue = []

        heapq.heappush(
            queue,
            (
                0,
                start
            )
        )

        g_score = {
            start: 0
        }

        parents = {}

        visited = set()

        visited_nodes = 0

        while queue:

            _, current = heapq.heappop(queue)

            if current in visited:
                continue

            visited.add(current)

            visited_nodes += 1

            if current == goal:
                break

            for neighbor in self.graph_manager.get_neighbors(current):

                edge = self.graph_manager.get_edge_length(
                    current,
                    neighbor
                )

                tentative = g_score[current] + edge

                if (
                    neighbor not in g_score
                    or
                    tentative < g_score[neighbor]
                ):

                    g_score[neighbor] = tentative

                    parents[neighbor] = current

                    priority = (
                        tentative +
                        self.heuristic(
                            neighbor,
                            goal
                        )
                    )

                    heapq.heappush(
                        queue,
                        (
                            priority,
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
            path_cost=g_score.get(goal, 0),
            execution_time=execution_time
        )