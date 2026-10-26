# Source code is private. This file shows only its classes and function signatures.

"""Cache of street graphs keyed by area and travel mode.

Downloading OSM data from Overpass is by far the slowest part of a request
(often 20-40 s on the public servers), so raw Overpass responses are cached per
area — in memory and gzipped on disk under ``backend/.osm_cache`` — and a graph
is built per (area, travel mode) on top of them. Any cached area that fully
contains the requested one is reused, so switching travel mode or moving points
around inside an area never re-downloads.
"""
import asyncio
import gzip
import json
import math
from collections import OrderedDict
from pathlib import Path
from app.graph.builder import build_graph_from_elements, fetch_osm_data
from app.graph.models import StreetGraph
BBox = ...
CACHE_DIR = ...
GRID_DEG = ...
MARGIN_M = ...
MAX_AREA_KM2 = ...
MAX_AREAS_IN_MEMORY = ...
MAX_GRAPHS_IN_MEMORY = ...
_areas: OrderedDict[BBox, list[dict]]
_graphs: OrderedDict[tuple[BBox, str], StreetGraph]
_area_lock = ...


class AreaTooLargeError(ValueError):
    """Raised when the requested points span more street network than can be downloaded."""


def area_km2(bbox: BBox) -> float:
    ...


def area_for(points: list[tuple[float, float]]) -> BBox:
    """Bounding box (with margin, aligned to the grid) that covers all points."""
    ...


async def get_graph(points: list[tuple[float, float]], mode: str) -> StreetGraph:
    """Street graph for the travel mode that covers all points, downloading data only if needed."""
    ...


async def _get_area(bbox: BBox) -> tuple[BBox, list[dict]]:
    """Raw Overpass elements for an area containing bbox: memory, then disk, then download."""
    ...


def _remember_area(area: BBox, elements: list[dict]) -> None:
    ...


def _disk_areas() -> list[tuple[BBox, Path]]:
    """Cached areas on disk, smallest first so the cheapest matching graph is built."""
    ...


def _file_name(bbox: BBox) -> str:
    ...


def _to_grid(value: float, rounding) -> float:
    ...


def _contains(outer: BBox, inner: BBox) -> bool:
    ...
