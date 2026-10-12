"""Exporta o best.pt para ONNX (formato exigido pelo yoloinferApp).

O yoloinferApp roda no navegador (ONNX Runtime Web) e espera entrada [1, 3, 192, 192].

Uso:
    python scripts/export_model.py
    python scripts/export_model.py --weights runs/detect/calcadas_v1/weights/best.pt
"""
import argparse
import shutil
from pathlib import Path

from ultralytics import YOLO


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", default="runs/detect/calcadas_v1/weights/best.pt")
    p.add_argument("--imgsz", type=int, default=192)
    args = p.parse_args()

    model = YOLO(args.weights)
    out = model.export(format="onnx", imgsz=args.imgsz, simplify=True)
    print("Exportado:", out)

    dest = Path("models")
    dest.mkdir(exist_ok=True)
    shutil.copy(out, dest / "calcadas.onnx")
    shutil.copy(args.weights, dest / "best.pt")
    print("Cópias salvas em models/calcadas.onnx e models/best.pt")


if __name__ == "__main__":
    main()
