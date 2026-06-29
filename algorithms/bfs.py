from collections import deque
import time
from algorithms.search_algorithm import SearchAlgorithm
from algorithms.search_result import SearchResult


class BFS(SearchAlgorithm):


    def search(self, start: int, goal: int) -> SearchResult:
   

        start_time = time.perf_counter()

        queue = deque([start])
        visited = {start}
        parents = {}

        visited_nodes = 0

        while queue:

            current = queue.popleft()
            visited_nodes += 1

            if current == goal:
                break

            for neighbor in self.graph_manager.get_neighbors(current):

                if neighbor not in visited:

                    visited.add(neighbor)
                    parents[neighbor] = current
                    queue.append(neighbor)

        execution_time = time.perf_counter() - start_time

        # Não encontrou caminho
        if start != goal and goal not in parents:
            return SearchResult(
                path=[],
                visited_nodes=visited_nodes,
                path_cost=0,
                execution_time=execution_time
            )

        # Reconstrução do caminho
        path = [goal]

        while path[-1] != start:
            path.append(parents[path[-1]])

        path.reverse()

        return SearchResult(
            path=path,
            visited_nodes=visited_nodes,
            path_cost=len(path) - 1,
            execution_time=execution_time
        )