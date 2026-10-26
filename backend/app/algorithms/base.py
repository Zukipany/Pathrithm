# Source code is private. This file shows only its classes and function signatures.

"""Base class for pathfinding algorithms."""
from abc import ABC, abstractmethod
from typing import Optional
import time
from app.graph.models import StreetGraph, AlgorithmStep, AlgorithmResult
from app.utils.haversine import haversine


class BaseAlgorithm(ABC):
    """Abstract base class for pathfinding algorithms."""
    name: str
    description: str
    guarantees_optimal: bool
    uses_heuristic: bool

    def __init__(self, graph: StreetGraph, mode: str='walking', weights: Optional[dict]=None):
        ...

    @abstractmethod
    def find_path(self, start: str, goal: str) -> AlgorithmResult:
        """
        Find path from start to goal.

        Args:
            start: Start node ID
            goal: Goal node ID

        Returns:
            AlgorithmResult with path and visualization data
        """
        ...

    def _reconstruct_path(self, came_from: dict[str, str], current: str) -> list[str]:
        """Reconstruct path from came_from map."""
        ...

    def _get_path_coords(self, path: list[str]) -> list[tuple[float, float]]:
        """Get coordinates for path nodes."""
        ...

    def _calculate_path_distance(self, path: list[str]) -> float:
        """Calculate total path distance in meters."""
        ...

    def _calculate_path_time(self, path: list[str]) -> float:
        """Calculate estimated travel time in minutes."""
        ...

    def _create_result(self, success: bool, path: list[str], visited: list[str], steps: list[AlgorithmStep], start: str, explanation: str, error: Optional[str]=None) -> AlgorithmResult:
        """Create AlgorithmResult with computed metrics."""
        ...

    def _distance_from(self, origin: str, node_id: str) -> float:
        """Straight-line distance in meters between two nodes (used to grow the search radius)."""
        ...

    def _get_explanation(self) -> str:
        """Get algorithm-specific explanation."""
        ...
