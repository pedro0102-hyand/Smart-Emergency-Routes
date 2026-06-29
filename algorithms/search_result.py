from dataclasses import dataclass

@dataclass

class SearchResult:


    path: list[int]
    visited_nodes: int
    path_cost: float
    execution_time: float