# Source code is private. This file shows only its classes and function signatures.

"""Greedy Best-First Search algorithm."""
import heapq
import time
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm
from app.utils.haversine import haversine


class GreedyBFSAlgorithm(BaseAlgorithm):
    """
    Greedy Best-First Search algorithm.

    Always expands the node that appears closest to the goal based on
    heuristic alone (ignoring actual cost traveled). Fast but can produce
    suboptimal paths and may take wrong turns.
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def _heuristic(self, node_id: str, goal_id: str) -> float:
        """Calculate straight-line distance heuristic."""
        ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
