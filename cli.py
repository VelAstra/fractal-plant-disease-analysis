"""
CLI for Fractal-Based Plant Disease Analysis Suite.
"""

import argparse
import sys
import numpy as np
from PIL import Image

from core.classifier import FractalPlantClassifier
from core.evaluation import evaluate_classifier_performance


def cmd_diagnose(args):
    img = Image.open(args.input).convert("RGB")
    arr = np.array(img)
    print(f"[Diagnosis] Menganalisis citra daun: {args.input}")

    clf = FractalPlantClassifier()
    pred = clf.predict(arr)

    print("\n" + "=" * 50)
    print("HASIL DIAGNOSIS PATOLOGI DAUN FRAKTAL")
    print("=" * 50)
    print(f"Prediksi Penyakit    : {pred.predicted_class.upper()}")
    print(f"Tingkat Kepercayaan  : {pred.confidence * 100:.1f}%")
    print(f"Ringkasan Medis      : {pred.diagnosis_summary}")
    print("\nFitur Fraktal Terekstraksi:")
    print(f"- Dimensi Fraktal Batas Daun (DF) : {pred.features['df_boundary']:.3f}")
    print(f"- Dimensi Fraktal Lesi Penyakit   : {pred.features['df_lesions']:.3f}")
    print(f"- Rasio Luas Lesi Nekrotik        : {pred.features['lesion_ratio']*100:.2f}%")
    print(f"- Dimensi Fraktal Tekstur Permukaan: {pred.features['df_texture']:.3f}")
    print(f"- Lakunaritas Permukaan           : {pred.features['lacunarity']:.3f}")
    print("=" * 50 + "\n")


def cmd_gui(args):
    from gui.app import launch_gui
    launch_gui()


def main():
    p = argparse.ArgumentParser(description="Fractal Plant Leaf Disease Diagnosis")
    sub = p.add_subparsers(dest="command")

    p_diag = sub.add_parser("diagnose", help="Diagnose leaf pathology from image")
    p_diag.add_argument("input", help="Input leaf image file")

    sub.add_parser("gui", help="Launch interactive diagnosis GUI")

    args = p.parse_args()
    if args.command == "diagnose":
        cmd_diagnose(args)
    elif args.command == "gui":
        cmd_gui(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
