"""
Interactive GUI Dashboard for Plant Leaf Disease Diagnosis.
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk

from core.classifier import FractalPlantClassifier


class PlantDiagnosisApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fractal Plant Leaf Pathology Diagnostic Studio")
        self.geometry("900x620")
        self.configure(bg="#F8FAFC")

        self.classifier = FractalPlantClassifier()
        self.current_img = None

        self._build_ui()
        sample = os.path.join(os.path.dirname(__file__), "..", "sample_data", "leaf_bacterial_spot.png")
        if os.path.exists(sample):
            self.load_image(os.path.abspath(sample))

    def _build_ui(self):
        header = tk.Frame(self, bg="#166534", height=60, padx=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="FRACTAL PLANT PATHOLOGY ANALYZER", font=("Segoe UI", 13, "bold"), fg="#FFFFFF", bg="#166534").pack(anchor="w", pady=(10, 0))
        tk.Label(header, text="Diagnosis Penyakit Daun Berbasis Dimensi Fraktal dan Lakunaritas", font=("Segoe UI", 9), fg="#DCFCE7", bg="#166534").pack(anchor="w")

        tools = tk.Frame(self, bg="#FFFFFF", padx=15, pady=8, relief="groove", bd=1)
        tools.pack(fill=tk.X, padx=15, pady=10)
        ttk.Button(tools, text="Pilih Citra Daun...", command=self.on_browse).pack(side=tk.LEFT, padx=5)
        ttk.Button(tools, text="Analisis Penyakit (Diagnosa)", command=self.on_diagnose).pack(side=tk.LEFT, padx=5)

        # Center Viewport & Results Card
        content = tk.Frame(self, bg="#F8FAFC", padx=15)
        content.pack(fill=tk.BOTH, expand=True)

        # Left Image
        f_left = tk.Frame(content, bg="#FFFFFF", relief="groove", bd=1, width=320)
        f_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        tk.Label(f_left, text="CITRA DAUN", font=("Segoe UI", 9, "bold"), bg="#FFFFFF", fg="#334155").pack(pady=4)
        self.lbl_img = tk.Label(f_left, bg="#F1F5F9")
        self.lbl_img.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        # Right Diagnostic Report
        f_right = tk.Frame(content, bg="#FFFFFF", relief="groove", bd=1)
        f_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))
        tk.Label(f_right, text="HASIL DIAGNOSIS FRAKTAL", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#166534").pack(pady=8)

        self.lbl_diag_class = tk.Label(f_right, text="-", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#0F172A")
        self.lbl_diag_class.pack(pady=4)

        self.lbl_diag_conf = tk.Label(f_right, text="Kepercayaan: -", font=("Segoe UI", 10), bg="#FFFFFF", fg="#16A34A")
        self.lbl_diag_conf.pack(pady=2)

        self.txt_summary = tk.Label(f_right, text="Silakan jalankan diagnosa untuk melihat hasil.", wraplength=340, font=("Segoe UI", 9), bg="#F1F5F9", fg="#334155", padx=10, pady=10)
        self.txt_summary.pack(fill=tk.X, padx=15, pady=12)

        self.lbl_feats = tk.Label(f_right, text="", justify=tk.LEFT, font=("Consolas", 9), bg="#FFFFFF", fg="#475569")
        self.lbl_feats.pack(anchor="w", padx=20, pady=5)

    def load_image(self, path):
        img = Image.open(path).convert("RGB")
        self.current_img = np.array(img)
        resized = img.resize((280, 280), Image.Resampling.BILINEAR)
        tk_img = ImageTk.PhotoImage(resized)
        self.lbl_img.image = tk_img
        self.lbl_img.config(image=tk_img)

    def on_browse(self):
        f = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if f:
            self.load_image(f)

    def on_diagnose(self):
        if self.current_img is None:
            return
        pred = self.classifier.predict(self.current_img)
        self.lbl_diag_class.config(text=pred.predicted_class.upper())
        self.lbl_diag_conf.config(text=f"Tingkat Kepercayaan: {pred.confidence * 100:.1f}%")
        self.txt_summary.config(text=pred.diagnosis_summary)

        f_txt = (
            f"Dimensi Batas Daun (DF) : {pred.features['df_boundary']:.3f}\n"
            f"Dimensi Lesi Nekrotik  : {pred.features['df_lesions']:.3f}\n"
            f"Rasio Luas Lesi         : {pred.features['lesion_ratio']*100:.2f}%\n"
            f"Dimensi Tekstur Urat   : {pred.features['df_texture']:.3f}\n"
            f"Lakunaritas Permukaan   : {pred.features['lacunarity']:.3f}"
        )
        self.lbl_feats.config(text=f_txt)


def launch_gui():
    app = PlantDiagnosisApp()
    app.mainloop()


if __name__ == "__main__":
    launch_gui()
