# Source code is private. This file shows only its classes and function signatures.

"""Point snapping to nearest road segment."""
import math
from dataclasses import dataclass
from typing import Optional
from app.graph.models import StreetGraph
from app.utils.haversine import haversine
from app.utils.geometry import project_point_on_segment, point_to_segment_distance


@dataclass
class SnappedPoint:
    """Result of snapping operation."""
    original_lat: float
    original_lon: float
    snapped_lat: float
    snapped_lon: float
    distance_m: float
    node_id: str
    street_name: Optional[str]
    success: bool
    error: Optional[str]


def snap_to_graph(graph: StreetGraph, lat: float, lon: float, max_distance_m: float=50.0) -> SnappedPoint:
    """
    Snap a coordinate to the nearest road segment in the graph.

    Args:
        graph: Street graph
        lat, lon: Point to snap
        max_distance_m: Maximum snapping distance

    Returns:
        SnappedPoint with snapping result
    """
    ...


def snap_multiple_points(graph: StreetGraph, points: list[tuple[float, float]], max_distance_m: float=50.0) -> list[SnappedPoint]:
    """Snap multiple points to the graph."""
    ...
