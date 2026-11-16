"""
Fractal Feature Extraction Module for Plant Leaf Disease Analysis.
Computes Leaf Boundary Fractal Dimension, Lesion Irregularity Fractal Dimension,
and Surface Lacunarity to characterize plant pathology.
"""

from typing import Tuple, Dict, Any
import numpy as np


def compute_box_dimension(binary_mask: np.ndarray) -> float:
    h, w = binary_mask.shape
    p = min(h, w)
    if p < 8 or np.sum(binary_mask) == 0:
        return 1.0

    scales = [2, 4, 8, 16]
    counts = []

    for s in scales:
        ny = h // s
        nx = w // s
        if ny == 0 or nx == 0:
            continue
        trimmed = binary_mask[: ny * s, : nx * s]
        boxes = trimmed.reshape(ny, s, nx, s)
        counts.append(max(1, int(np.sum(np.any(boxes > 0, axis=(1, 3))))))

    if len(counts) < 2:
        return 1.0

    log_inv = np.log(1.0 / np.array(scales[:len(counts)], dtype=np.float64))
    log_c = np.log(counts)
    poly = np.polyfit(log_inv, log_c, 1)
    df = float(poly[0])
    return max(1.0, min(2.0, df))


def compute_lacunarity(image: np.ndarray, box_size: int = 4) -> float:
    h, w = image.shape
    ny = h // box_size
    nx = w // box_size
    if ny == 0 or nx == 0:
        return 1.0

    trimmed = image[: ny * box_size, : nx * box_size]
    boxes = trimmed.reshape(ny, box_size, nx, box_size)
    masses = np.sum(boxes, axis=(1, 3)).astype(np.float64)

    mean = np.mean(masses)
    if mean < 1e-5:
        return 1.0
    var = np.var(masses)
    return float((var / (mean ** 2)) + 1.0)


def extract_leaf_fractal_features(leaf_rgb: np.ndarray) -> Dict[str, float]:
    """
    Extracts a 4-dimensional fractal feature vector from a leaf image:
    1. df_boundary: Fractal dimension of leaf contour
    2. df_lesions: Fractal dimension of necrotic disease lesions
    3. df_texture: Box counting dimension of surface veins/edges
    4. lacunarity: Gappiness and distribution irregularity
    """
    r = leaf_rgb[:, :, 0].astype(np.float32)
    g = leaf_rgb[:, :, 1].astype(np.float32)
    b = leaf_rgb[:, :, 2].astype(np.float32)

    # 1. Leaf silhouette mask (excess green: 2*G - R - B > 10)
    leaf_mask = ((2 * g - r - b) > 10).astype(np.uint8)

    # Leaf boundary contour
    gy, gx = np.gradient(leaf_mask.astype(np.float32))
    boundary = (np.sqrt(gx**2 + gy**2) > 0.1).astype(np.uint8)
    df_boundary = compute_box_dimension(boundary)

    # 2. Lesions / necrotic spots (brown/yellow areas where R > G or dark spots)
    lesion_mask = (leaf_mask == 1) & ((r > g * 0.95) | (g < 60))
    df_lesions = compute_box_dimension(lesion_mask.astype(np.uint8))
    lesion_area_ratio = float(np.sum(lesion_mask) / max(1, np.sum(leaf_mask)))

    # 3. Surface texture edges
    gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
    t_gy, t_gx = np.gradient(gray.astype(np.float32))
    edges = (np.sqrt(t_gx**2 + t_gy**2) > 15.0).astype(np.uint8) & leaf_mask
    df_texture = compute_box_dimension(edges)

    # 4. Lacunarity
    lac = compute_lacunarity(gray * leaf_mask, box_size=8)

    return {
        "df_boundary": df_boundary,
        "df_lesions": df_lesions,
        "lesion_ratio": lesion_area_ratio,
        "df_texture": df_texture,
        "lacunarity": lac,
    }
