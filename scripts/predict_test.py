"""Testa o modelo em imagens/vídeo/webcam antes de ir para o celular.

Uso:
    python scripts/predict_test.py --source dataset/test/images
    python scripts/predict_test.py --source 0          # webcam
"""
import argparse

from ultralytics import YOLO


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--weights", default="models/best.pt")
    p.add_argument("--source", default="dataset/test/images")
    p.add_argument("--conf", type=float, default=0.25)
    args = p.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    model = YOLO(args.weights)
    model.predict(source=source, conf=args.conf, save=True, show=args.source.isdigit(),
                  project="runs/predict", name="teste", exist_ok=True)
    print("Resultados em runs/predict/teste")


if __name__ == "__main__":
    main()
