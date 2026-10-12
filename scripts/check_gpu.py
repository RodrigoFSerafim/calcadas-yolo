"""Confere se o PyTorch enxerga a GPU (RTX 4060)."""
import torch

print("PyTorch:", torch.__version__)
print("CUDA disponível:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("Sem CUDA: reinstale o torch com o índice cu121 (veja requirements.txt).")
