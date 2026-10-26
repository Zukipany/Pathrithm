# Source code is private. This file shows only its classes and function signatures.

"""Depth-First Search algorithm."""
import time
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm


class DFSAlgorithm(BaseAlgorithm):
    """
    Depth-First Search (DFS) algorithm.

    Explores as far as possible along each branch before backtracking.
    Does not guarantee shortest path - mainly useful for learning
    graph traversal and connectivity checking.
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
