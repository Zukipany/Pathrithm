# Source code is private. This file shows only its classes and function signatures.

"""A* search algorithm."""
import heapq
import time
from itertools import islice
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm
from app.utils.haversine import haversine


class AStarAlgorithm(BaseAlgorithm):
    """
    A* (A-Star) search algorithm.

    Uses a heuristic (straight-line distance) to guide the search toward
    the goal, often exploring fewer nodes than Dijkstra while still
    guaranteeing the optimal path with an admissible heuristic.
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def _heuristic(self, node_id: str, goal_id: str) -> float:
        """Calculate straight-line distance heuristic (admissible)."""
        ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
