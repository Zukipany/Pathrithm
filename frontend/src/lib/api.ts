// Source code is private. This file shows only its classes and function signatures.

import type {
  Point,
  SnappedPoint,
  AlgorithmResult,
  CompareResult,
  MultiPointResult,
  TravelMode,
  AlgorithmType,
  BoundaryShape,
} from './types';

async function request<T>(endpoint: string, options?: RequestInit): Promise<T> { /* private */ }

export interface SnapPointsParams {
  points: Point[];
  mode: TravelMode;
  max_distance_m?: number;
  boundary?: BoundaryShape | null;
}

export async function snapPoints(params: SnapPointsParams): Promise<{ snapped_points: SnappedPoint[]; success: boolean; error?: string }> { /* private */ }

export interface RunAlgorithmParams {
  start: Point;
  goal: Point;
  algorithm: AlgorithmType;
  mode: TravelMode;
  weights?: Record<string, number>;
  visualize?: boolean;
  boundary?: BoundaryShape | null;
}

export async function runAlgorithm(params: RunAlgorithmParams): Promise<AlgorithmResult> { /* private */ }

export interface CompareAlgorithmsParams {
  start: Point;
  goal: Point;
  algorithms: AlgorithmType[];
  mode: TravelMode;
  boundary?: BoundaryShape | null;
}

export async function compareAlgorithms(params: CompareAlgorithmsParams): Promise<CompareResult> { /* private */ }

export interface MultiPointParams {
  points: Point[];
  algorithm: AlgorithmType;
  mode: TravelMode;
  optimize_order?: boolean;
  weights?: Record<string, number>;
}

export async function multiPointRoute(params: MultiPointParams): Promise<MultiPointResult> { /* private */ }

export async function healthCheck(): Promise<{ status: string; service: string }> { /* private */ }
