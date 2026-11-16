"""
Unit and Integration Tests for Fractal Plant Disease Analysis Suite.
"""

import unittest
import numpy as np
from PIL import Image

from core.fractal_features import extract_leaf_fractal_features, compute_box_dimension
from core.classifier import FractalPlantClassifier
from core.evaluation import evaluate_classifier_performance
from sample_data.generate_leaf_dataset import draw_base_leaf


class TestPlantDisease(unittest.TestCase):

    def setUp(self):
        self.classifier = FractalPlantClassifier()
        img = draw_base_leaf(120)
        self.leaf_arr = np.array(img)

    def test_feature_extraction(self):
        feats = extract_leaf_fractal_features(self.leaf_arr)
        self.assertIn("df_boundary", feats)
        self.assertIn("df_lesions", feats)
        self.assertIn("lesion_ratio", feats)
        self.assertGreaterEqual(feats["df_boundary"], 1.0)
        self.assertLessEqual(feats["df_boundary"], 2.0)

    def test_healthy_prediction(self):
        pred = self.classifier.predict(self.leaf_arr)
        self.assertEqual(pred.predicted_class, "healthy")
        self.assertGreater(pred.confidence, 0.75)

    def test_evaluation_metrics(self):
        y_true = ["healthy", "bacterial_spot", "rust_blight"]
        y_pred = ["healthy", "bacterial_spot", "rust_blight"]
        res = evaluate_classifier_performance(y_true, y_pred)
        self.assertEqual(res["overall_accuracy"], 1.0)


if __name__ == "__main__":
    unittest.main()
