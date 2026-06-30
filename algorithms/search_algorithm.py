from abc import ABC, abstractmethod
from graph.graph_manager import GraphManager


class SearchAlgorithm(ABC):

    def __init__(self, graph_manager: GraphManager):
        self.graph_manager = graph_manager

    @abstractmethod
    def search(self, start: int, goal: int):
        pass

    def _reconstruct_path(
        self,
        parents: dict[int, int],
        start: int,
        goal: int
    ) -> list[int]:

        if start == goal:
            return [start]

        if goal not in parents:
            return []

        path = [goal]

        while path[-1] != start:
            path.append(parents[path[-1]])

        path.reverse()

        return path