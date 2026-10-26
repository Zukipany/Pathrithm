# Source code is private. This file shows only its classes and function signatures.

"""Geometric operations for spatial calculations."""
import math


def project_point_on_segment(point: tuple[float, float], segment_start: tuple[float, float], segment_end: tuple[float, float]) -> tuple[float, float]:
    """
    Project a point onto a line segment.

    Args:
        point: (lat, lon) of point to project
        segment_start: (lat, lon) of segment start
        segment_end: (lat, lon) of segment end

    Returns:
        (lat, lon) of projected point on segment
    """
    ...


def point_to_segment_distance(point: tuple[float, float], segment_start: tuple[float, float], segment_end: tuple[float, float]) -> float:
    """
    Calculate distance from point to line segment.

    Returns:
        Distance in meters
    """
    ...


def bounding_box(center_lat: float, center_lon: float, radius_m: float) -> tuple[float, float, float, float]:
    """
    Calculate bounding box around a center point.

    Args:
        center_lat, center_lon: Center coordinates
        radius_m: Radius in meters

    Returns:
        (min_lat, min_lon, max_lat, max_lon)
    """
    ...
