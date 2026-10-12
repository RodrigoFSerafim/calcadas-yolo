"""Treino do YOLOv8n para auditoria de calçadas.

Uso (na raiz do repositório):
    python scripts/train.py
    python scripts/train.py --epochs 150 --batch 32 --imgsz 192
"""
import argparse

from ultralytics import YOLO


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="dataset/data.yaml")
    p.add_argument("--model", default="yolov8n.pt")
    p.add_argument("--epochs", type=int, default=100)
    # 192 = resolução de entrada do yoloinferApp; treinar nela deixa as métricas
    # iguais ao que roda no celular. Teste 320/640 só para comparação.
    p.add_argument("--imgsz", type=int, default=192)
    p.add_argument("--batch", type=int, default=16)
    p.add_argument("--workers", type=int, default=0, help="0 evita erros no Windows")
    p.add_argument("--name", default="calcadas_v1")
    args = p.parse_args()

    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=0,
        workers=args.workers,
        patience=30,
        project="runs/detect",
        name=args.name,
        exist_ok=True,
        plots=True,
    )


if __name__ == "__main__":
    main()
