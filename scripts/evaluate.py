"""Avalia o best.pt no conjunto de TESTE e imprime as métricas para o README.

Uso:
    python scripts/evaluate.py
    python scripts/evaluate.py --weights runs/detect/calcadas_v1/weights/best.pt
"""
import argparse

from ultralytics import YOLO


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", default="runs/detect/calcadas_v1/weights/best.pt")
    p.add_argument("--data", default="dataset/data.yaml")
    p.add_argument("--imgsz", type=int, default=192)
    args = p.parse_args()

    model = YOLO(args.weights)
    m = model.val(data=args.data, split="test", imgsz=args.imgsz, plots=True)

    print("\n=== MÉTRICAS (teste) ===")
    print(f"mAP@50     : {m.box.map50:.3f}")
    print(f"mAP@50-95  : {m.box.map:.3f}")
    print(f"Precision  : {m.box.mp:.3f}")
    print(f"Recall     : {m.box.mr:.3f}")
    print("\nmAP@50 por classe:")
    for i, name in model.names.items():
        if i < len(m.box.ap50):
            print(f"  {name:<18} {m.box.ap50[i]:.3f}")


if __name__ == "__main__":
    main()
