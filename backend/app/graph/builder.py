# Source code is private. This file shows only its classes and function signatures.

"""Build street graph from OpenStreetMap data via Overpass API."""
import hashlib
import time
from typing import Optional
import httpx
from app.graph.models import Node, Edge, StreetGraph
from app.utils.haversine import haversine
HIGHWAY_TYPES = ...
WALKABLE_HIGHWAYS = ...
CYCLABLE_HIGHWAYS = ...
DRIVABLE_HIGHWAYS = ...
DEFAULT_SPEEDS = ...
WALKING_SPEED = ...
CYCLING_SPEED = ...
DRIVING_SPEED_FACTOR = ...


def _generate_node_id(lat: float, lon: float, osm_id: str) -> str:
    """Generate unique node ID from OSM data."""
    ...


def _parse_osm_tags(tags: dict) -> dict:
    """Extract relevant properties from OSM tags."""
    ...


def _is_allowed_for_mode(highway: str, mode: str, tags: dict) -> bool:
    """Check if a road segment is allowed for travel mode."""
    ...
OVERPASS_URLS = ...
_preferred_overpass = ...


class OverpassUnavailableError(RuntimeError):
    """Raised when no Overpass instance returned street data."""


async def fetch_osm_data(min_lat: float, min_lon: float, max_lat: float, max_lon: float, timeout: float=90.0) -> list[dict]:
    """
    Fetch OSM data from Overpass API.

    Public Overpass servers are frequently overloaded, so each configured
    instance is tried in turn before giving up.

    Args:
        min_lat, min_lon, max_lat, max_lon: Bounding box
        timeout: Request timeout in seconds (per instance)

    Returns:
        List of OSM elements (nodes and ways)
    """
    ...


async def build_graph_from_osm(min_lat: float, min_lon: float, max_lat: float, max_lon: float, mode: str='walking') -> StreetGraph:
    """
    Build street graph from OSM data.

    Args:
        min_lat, min_lon, max_lat, max_lon: Bounding box
        mode: Travel mode (walking, cycling, driving)

    Returns:
        StreetGraph instance
    """
    ...


def build_graph_from_elements(elements: list[dict], mode: str='walking') -> StreetGraph:
    """
    Build a street graph for one travel mode from raw Overpass elements.

    Only the largest connected part of the network is kept, so every point
    that snaps onto the graph can actually reach every other one (fragments
    cut off at the edge of the download area would otherwise strand routes).
    """
    ...


def _largest_component(graph: StreetGraph) -> set[str]:
    """Node IDs of the largest connected component, ignoring edge direction."""
    ...


async def extend_graph_for_points(graph: StreetGraph, points: list[tuple[float, float]], radius_m: float=500.0) -> StreetGraph:
    """
    Extend graph to ensure all points are covered.

    Args:
        graph: Existing graph
        points: List of (lat, lon) points
        radius_m: Additional radius around each point

    Returns:
        Extended graph (may modify original)
    """
    ...
