# Source code is private. This file shows only its classes and function signatures.

"""Breadth-First Search algorithm."""
import time
from collections import deque
from itertools import islice
from typing import Optional
from app.graph.models import AlgorithmStep
from app.algorithms.base import BaseAlgorithm


class BFSAlgorithm(BaseAlgorithm):
    """
    Breadth-First Search (BFS) algorithm.

    Explores the graph layer by layer, visiting all nodes at distance N
    before any nodes at distance N+1. Without weights, finds the path
    with fewest edges (not necessarily shortest distance).
    """
    name = ...
    description = ...
    guarantees_optimal = ...
    uses_heuristic = ...

    def find_path(self, start: str, goal: str) -> 'AlgorithmResult':
        ...
