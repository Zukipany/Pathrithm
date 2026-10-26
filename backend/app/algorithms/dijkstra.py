# Source code is private. This file shows only its classes and function signatures.

"""Dijkstra's shortest path algorithm."""
import heapq
import time
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm


class DijkstraAlgorithm(BaseAlgorithm):
    """
    Dijkstra's Algorithm for finding shortest paths.

    Explores outward from start in order of increasing distance,
    guaranteeing the shortest path when all edge weights are non-negative.
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
