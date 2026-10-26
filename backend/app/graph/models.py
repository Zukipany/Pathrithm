# Source code is private. This file shows only its classes and function signatures.

"""Graph data structures for street network representation."""
from dataclasses import dataclass, field
from typing import Optional
import math


@dataclass
class Node:
    """Represents an intersection or point in the street network."""
    id: str
    lat: float
    lon: float
    street_name: Optional[str]

    @property
    def coord(self) -> tuple[float, float]:
        """Return (lat, lon) tuple."""
        ...


@dataclass
class Edge:
    """Represents a road segment between two nodes."""
    source: str
    target: str
    distance_m: float
    time_s: float
    road_type: str
    oneway: bool
    walking: bool
    cycling: bool
    driving: bool
    max_speed_kmh: Optional[int]
    surface: Optional[str]
    elevation_gain: float

    def cost(self, mode: str='walking', weights: Optional[dict]=None) -> float:
        """
        Calculate edge cost based on travel mode and weights.

        Args:
            mode: Travel mode (walking, cycling, driving)
            weights: Custom weights for cost calculation

        Returns:
            Edge cost (lower = better)
        """
        ...


@dataclass
class AlgorithmStep:
    """Records a single step in algorithm execution for visualization."""
    step_number: int
    current_node: Optional[str]
    frontier: list[str]
    visited: list[str]
    distance_updates: list[tuple[str, float]]
    g_scores: dict[str, float]
    h_scores: dict[str, float]
    f_scores: dict[str, float]
    explanation: str
    search_radius: float
    visited_count: int


@dataclass
class AlgorithmResult:
    """Complete result of algorithm execution."""
    success: bool
    path: list[str]
    path_coords: list[tuple[float, float]]
    total_distance_m: float
    estimated_time_min: float
    visited_nodes: list[str]
    visited_edges: list[tuple[str, str]]
    steps: list[AlgorithmStep]
    search_radius_m: float
    explored_area_km2: float
    execution_time_ms: float
    explanation: str
    error: Optional[str]


class StreetGraph:
    """
    Graph representation of street network.

    Uses adjacency list for efficient neighbor lookups.
    """

    def __init__(self):
        ...

    def add_node(self, node: Node) -> None:
        """Add a node to the graph."""
        ...

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph."""
        ...

    def get_neighbors(self, node_id: str) -> list[str]:
        """Get neighbor node IDs."""
        ...

    def get_edge(self, source: str, target: str) -> Optional[Edge]:
        """Get edge between two nodes."""
        ...

    def get_edge_cost(self, source: str, target: str, mode: str='walking', weights: Optional[dict]=None) -> float:
        """Get cost of edge between two nodes."""
        ...

    def node_count(self) -> int:
        ...

    def edge_count(self) -> int:
        ...

    def get_coords(self, node_id: str) -> Optional[tuple[float, float]]:
        """Get coordinates of a node."""
        ...

    def create_subgraph(self, node_ids: set[str]) -> 'StreetGraph':
        """Return a new StreetGraph containing only the given nodes and edges between them."""
        ...

    def calculate_search_radius(self, visited_ids: list[str], start_id: str) -> float:
        """Calculate maximum straight-line distance from start to any visited node."""
        ...

    def calculate_explored_area(self, visited_ids: list[str]) -> float:
        """
        Estimate explored area using convex hull approximation.

        Returns:
            Area in square kilometers (approximate)
        """
        ...
