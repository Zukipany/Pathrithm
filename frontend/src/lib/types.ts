// Source code is private. This file shows only its classes and function signatures.

export interface Point {
  lat: number;
  lon: number;
  label?: string;
}

export interface SnappedPoint extends Point {
  original: Point;
  snapped: Point;
  distance_m: number;
  node_id: string;
  street_name: string | null;
  success: boolean;
  error?: string;
}

export interface AlgorithmStep {
  step_number: number;
  current_node: string | null;
  current_coord: [number, number] | null;
  frontier: string[];
  frontier_coords: [number, number][];
  visited: string[];
  visited_count: number; // how many entries of AlgorithmResult.visited_coords are visited at this frame
  search_radius_m: number;
  explanation: string;
}

export interface AlgorithmResult {
  success: boolean;
  path: [number, number][];
  start_coord: [number, number] | null;
  goal_coord: [number, number] | null;
  visited_coords: [number, number][]; // every visited node, in visit order
  total_distance_m: number;
  estimated_time_min: number;
  visited_nodes_count: number;
  visited_edges_count: number;
  search_radius_m: number;
  explored_area_km2: number;
  execution_time_ms: number;
  steps: AlgorithmStep[];
  explanation: string;
  error?: string;
}

export interface AlgorithmComparison {
  algorithm: string;
  success: boolean;
  distance_m: number;
  time_min: number;
  nodes_explored: number;
  edges_explored: number;
  search_radius_m: number;
  explored_area_km2: number;
  execution_time_ms: number;
  optimal: boolean;
  explanation: string;
}

export interface CompareResult {
  comparisons: AlgorithmComparison[];
  best_algorithm: string;
  best_by_distance: string;
  best_by_efficiency: string;
  summary: string;
}

export interface MultiPointSegment {
  from_label: string;
  to_label: string;
  distance_m: number;
  time_min: number;
  path: [number, number][];
}

export interface MultiPointResult {
  segments: MultiPointSegment[];
  total_distance_m: number;
  total_time_min: number;
  original_order_distance: number | null;
  optimized: boolean;
  order_changed: boolean;
  explanation: string;
}

export interface CircleBoundary {
  type: 'circle';
  center_lat: number;
  center_lon: number;
  radius_m: number;
}

export interface RectangleBoundary {
  type: 'rectangle';
  north: number;
  south: number;
  east: number;
  west: number;
}

export interface PolygonBoundary {
  type: 'polygon';
  points: [number, number][];  // [lat, lon] pairs
}

export type BoundaryShape = CircleBoundary | RectangleBoundary | PolygonBoundary;

export type DrawingMode = 'none' | 'circle' | 'rectangle' | 'polygon';

export type TravelMode = 'walking' | 'cycling' | 'driving';

export type AlgorithmType =
  | 'dijkstra'
  | 'astar'
  | 'bfs'
  | 'dfs'
  | 'greedy'
  | 'bidirectional';

export interface AlgorithmInfo {
  id: AlgorithmType;
  name: string;
  description: string;
  color: string;
  optimal: boolean;
  usesHeuristic: boolean;
}

export const ALGORITHMS: AlgorithmInfo[] = [ /* private */ ];

export const TRAVEL_MODES: { id: TravelMode; name: string; icon: string }[] = [ /* private */ ];
