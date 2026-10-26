# Source code is private. This file shows only its classes and function signatures.

"""Distance calculations using the Haversine formula."""
import math
EARTH_RADIUS_M = ...


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on Earth.

    Args:
        lat1, lon1: Coordinates of point 1 (in degrees)
        lat2, lon2: Coordinates of point 2 (in degrees)

    Returns:
        Distance in meters
    """
    ...


def haversine_tuple(coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
    """Calculate distance between two (lat, lon) tuples."""
    ...
