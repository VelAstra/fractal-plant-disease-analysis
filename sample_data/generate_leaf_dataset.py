"""
Synthetic Plant Leaf Disease Dataset Generator.
Synthesizes realistic leaf shapes with distinct pathological lesion patterns.
"""

import os
from typing import List, Tuple
import numpy as np
from PIL import Image, ImageDraw


def draw_base_leaf(size: int = 160) -> Image.Image:
    img = Image.new("RGB", (size, size), color=(240, 240, 240))
    draw = ImageDraw.Draw(img)
    center = size // 2

    # Draw elliptical leaf silhouette
    draw.polygon([
        (center, 15),
        (center + 55, center - 20),
        (center + 45, center + 45),
        (center, size - 20),
        (center - 45, center + 45),
        (center - 55, center - 20),
    ], fill=(45, 140, 45), outline=(30, 95, 30))

    # Main vein
    draw.line([center, 25, center, size - 25], fill=(30, 110, 30), width=3)
    for y_v in range(40, size - 40, 20):
        draw.line([center, y_v, center + 35, y_v - 15], fill=(30, 110, 30), width=1)
        draw.line([center, y_v, center - 35, y_v - 15], fill=(30, 110, 30), width=1)

    return img


def generate_synthetic_samples(output_dir: str = "sample_data") -> List[Tuple[str, str]]:
    os.makedirs(output_dir, exist_ok=True)
    samples = []

    # 1. Healthy Leaf
    img_h = draw_base_leaf(160)
    p_h = os.path.join(output_dir, "leaf_healthy.png")
    img_h.save(p_h)
    samples.append((p_h, "healthy"))

    # 2. Bacterial Leaf Spot (Jagged small brown necrotic spots)
    img_b = draw_base_leaf(160)
    draw_b = ImageDraw.Draw(img_b)
    rng = np.random.default_rng(42)
    for _ in range(15):
        bx = rng.integers(60, 100)
        by = rng.integers(40, 120)
        r = rng.integers(3, 7)
        draw_b.ellipse([bx - r, by - r, bx + r, by + r], fill=(120, 60, 20), outline=(50, 20, 10))
    p_b = os.path.join(output_dir, "leaf_bacterial_spot.png")
    img_b.save(p_b)
    samples.append((p_b, "bacterial_spot"))

    # 3. Rust / Blight (Large diffuse chlorotic and orange-brown patches)
    img_r = draw_base_leaf(160)
    draw_r = ImageDraw.Draw(img_r)
    draw_r.ellipse([65, 50, 105, 95], fill=(185, 110, 30), outline=(130, 70, 10))
    draw_r.ellipse([50, 90, 90, 130], fill=(170, 95, 25), outline=(120, 60, 10))
    p_r = os.path.join(output_dir, "leaf_rust.png")
    img_r.save(p_r)
    samples.append((p_r, "rust_blight"))

    return samples


if __name__ == "__main__":
    s = generate_synthetic_samples()
    print(f"Generated {len(s)} leaf pathology samples.")
