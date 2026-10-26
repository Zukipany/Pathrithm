# Source code is private. This file shows only its classes and function signatures.

"""Pydantic schemas for API request/response models."""
from pydantic import BaseModel, Field
from typing import Optional


class BoundaryFilter(BaseModel):
    """Flat boundary shape — type selects which fields are used."""
    type: str
    center_lat: Optional[float]
    center_lon: Optional[float]
    radius_m: Optional[float]
    north: Optional[float]
    south: Optional[float]
    east: Optional[float]
    west: Optional[float]
    points: Optional[list[list[float]]]


class PointInput(BaseModel):
    """A route point with latitude and longitude."""
    lat: float
    lon: float
    label: Optional[str]


class SnapRequest(BaseModel):
    """Request to snap points to roads."""
    points: list[PointInput]
    mode: str
    max_distance_m: float
    boundary: Optional[BoundaryFilter]


class SnapResponse(BaseModel):
    """Response with snapped points."""
    snapped_points: list[dict]
    success: bool
    error: Optional[str]


class GraphLoadRequest(BaseModel):
    """Request to load graph for an area."""
    center_lat: float
    center_lon: float
    radius_m: float
    mode: str


class GraphLoadResponse(BaseModel):
    """Response with graph statistics."""
    node_count: int
    edge_count: int
    bbox: tuple[float, float, float, float]
    load_time_ms: float
    success: bool
    error: Optional[str]


class AlgorithmRequest(BaseModel):
    """Request to run a pathfinding algorithm."""
    start: PointInput
    goal: PointInput
    algorithm: str
    mode: str
    weights: Optional[dict]
    visualize: bool
    boundary: Optional[BoundaryFilter]


class MultiPointRequest(BaseModel):
    """Request for multi-point routing."""
    points: list[PointInput]
    algorithm: str
    mode: str
    optimize_order: bool
    weights: Optional[dict]


class AlgorithmStepResponse(BaseModel):
    """Single animation frame (a sampled algorithm step) for visualization."""
    step_number: int
    current_node: Optional[str]
    current_coord: Optional[tuple[float, float]]
    frontier: list[str]
    frontier_coords: list[tuple[float, float]]
    visited: list[str]
    visited_count: int
    search_radius_m: float
    explanation: str


class AlgorithmResponse(BaseModel):
    """Response with algorithm result."""
    success: bool
    path: list[tuple[float, float]]
    start_coord: Optional[tuple[float, float]]
    goal_coord: Optional[tuple[float, float]]
    visited_coords: list[tuple[float, float]]
    total_distance_m: float
    estimated_time_min: float
    visited_nodes_count: int
    visited_edges_count: int
    search_radius_m: float
    explored_area_km2: float
    execution_time_ms: float
    steps: list[AlgorithmStepResponse]
    explanation: str
    error: Optional[str]


class CompareRequest(BaseModel):
    """Request to compare multiple algorithms."""
    start: PointInput
    goal: PointInput
    algorithms: list[str]
    mode: str
    boundary: Optional[BoundaryFilter]


class AlgorithmComparison(BaseModel):
    """Comparison result for a single algorithm."""
    algorithm: str
    success: bool
    distance_m: float
    time_min: float
    nodes_explored: int
    edges_explored: int
    search_radius_m: float
    explored_area_km2: float
    execution_time_ms: float
    optimal: bool
    explanation: str


class CompareResponse(BaseModel):
    """Response with algorithm comparison."""
    comparisons: list[AlgorithmComparison]
    best_algorithm: str
    best_by_distance: str
    best_by_efficiency: str
    summary: str


class MultiPointSegment(BaseModel):
    """Result for a single segment of multi-point route."""
    from_label: str
    to_label: str
    distance_m: float
    time_min: float
    path: list[tuple[float, float]]


class MultiPointResponse(BaseModel):
    """Response for multi-point routing."""
    segments: list[MultiPointSegment]
    total_distance_m: float
    total_time_min: float
    original_order_distance: Optional[float]
    optimized: bool
    order_changed: bool
    explanation: str


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    service: str
