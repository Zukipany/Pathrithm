# Source code is private. This file shows only its classes and function signatures.

"""API route handlers."""
from fastapi import APIRouter, HTTPException
from typing import Optional
import time
import math
from app.api.schemas import SnapRequest, SnapResponse, GraphLoadRequest, GraphLoadResponse, AlgorithmRequest, AlgorithmResponse, AlgorithmStepResponse, CompareRequest, CompareResponse, AlgorithmComparison, MultiPointRequest, MultiPointResponse, MultiPointSegment, BoundaryFilter, PointInput
from app.graph.builder import OverpassUnavailableError
from app.graph.models import AlgorithmResult, StreetGraph
from app.graph.store import AreaTooLargeError, area_for, get_graph
from app.utils.haversine import haversine as _haversine
from app.graph.snapping import snap_to_graph, SnappedPoint
from app.algorithms.dijkstra import DijkstraAlgorithm
from app.algorithms.astar import AStarAlgorithm
from app.algorithms.bfs import BFSAlgorithm
from app.algorithms.dfs import DFSAlgorithm
from app.algorithms.greedy import GreedyBFSAlgorithm
from app.algorithms.bidirectional import BidirectionalDijkstra
router = ...
SNAP_RADIUS_M = ...
MAX_FRAMES = ...
MAX_VISITED_COORDS = ...
ALGORITHMS = ...


def _point_in_polygon(lat: float, lon: float, polygon: list[list[float]]) -> bool:
    """Ray-casting point-in-polygon test."""
    ...


def _node_in_boundary(node, boundary: BoundaryFilter) -> bool:
    ...


def _boundary_extent(boundary: Optional[BoundaryFilter]) -> list[tuple[float, float]]:
    """Points spanning the boundary, so the downloaded area covers all of it."""
    ...


def _apply_boundary(graph: StreetGraph, boundary: BoundaryFilter, always_include: set[str]) -> StreetGraph:
    """Return a subgraph restricted to nodes within boundary (start/goal always kept)."""
    ...


async def _graph_for(points: list[PointInput], mode: str, boundary: Optional[BoundaryFilter]=None) -> StreetGraph:
    """Street graph covering the points (and boundary), turning data problems into clear HTTP errors."""
    ...


def _snap(graph: StreetGraph, point: PointInput, name: str) -> SnappedPoint:
    ...


def _frames(result: AlgorithmResult, graph: StreetGraph) -> list[AlgorithmStepResponse]:
    """Sample at most MAX_FRAMES steps evenly, attach coordinates, and add a final 'done' frame."""
    ...


@router.get('/health')
async def health_check():
    """Health check endpoint."""
    ...


@router.post('/graph/load', response_model=GraphLoadResponse)
async def load_graph(request: GraphLoadRequest):
    """Load street graph for a bounding box."""
    ...


@router.post('/route/snap', response_model=SnapResponse)
async def snap_points(request: SnapRequest):
    """Snap points to nearest road segments."""
    ...


@router.post('/algorithm/run', response_model=AlgorithmResponse)
async def run_algorithm(request: AlgorithmRequest):
    """Run a single pathfinding algorithm."""
    ...


@router.post('/algorithm/compare', response_model=CompareResponse)
async def compare_algorithms(request: CompareRequest):
    """Compare multiple algorithms on the same route."""
    ...


@router.post('/multipoint/route', response_model=MultiPointResponse)
async def multipoint_route(request: MultiPointRequest):
    """Calculate route through multiple points."""
    ...
