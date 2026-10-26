# Source code is private. This file shows only its classes and function signatures.

"""Bidirectional search algorithms."""
import heapq
import time
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm
from app.utils.haversine import haversine


class BidirectionalDijkstra(BaseAlgorithm):
    """
    Bidirectional Dijkstra's algorithm.

    Runs two simultaneous Dijkstra searches: one forward from start
    and one backward from goal. When they meet, we have the shortest path.
    Often explores ~50% less area than unidirectional Dijkstra.
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
