from graph.graph_manager import GraphManager
from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):

    def __init__(self, graph_manager: GraphManager):
        self.graph_manager = graph_manager

    @abstractmethod
    def search(self, start: int, goal: int):
        pass