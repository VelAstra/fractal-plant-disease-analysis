"""
Core Modules for Fractal-Based Plant Disease Analysis Suite.
"""

from .fractal_features import extract_leaf_fractal_features, compute_box_dimension, compute_lacunarity
from .classifier import FractalPlantClassifier, DiseasePrediction
from .evaluation import evaluate_classifier_performance

__all__ = [
    "extract_leaf_fractal_features",
    "compute_box_dimension",
    "compute_lacunarity",
    "FractalPlantClassifier",
    "DiseasePrediction",
    "evaluate_classifier_performance",
]
