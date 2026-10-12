"""Conta imagens e instâncias por classe/split (cole o resultado no README)."""
from collections import Counter
from pathlib import Path

import yaml

root = Path("dataset")
cfg = yaml.safe_load((root / "data.yaml").read_text(encoding="utf-8"))
names = cfg["names"]
if isinstance(names, list):
    names = dict(enumerate(names))

print(f"{'split':<8}{'imagens':>9}  instâncias por classe")
total_imgs = 0
for split in ("train", "valid", "test"):
    img_dir = root / split / "images"
    lbl_dir = root / split / "labels"
    if not img_dir.exists():
        continue
    n_imgs = len([f for f in img_dir.iterdir() if f.suffix.lower() in {".jpg", ".jpeg", ".png"}])
    total_imgs += n_imgs
    c = Counter()
    for f in lbl_dir.glob("*.txt"):
        for line in f.read_text().splitlines():
            if line.strip():
                c[int(line.split()[0])] += 1
    detalhe = ", ".join(f"{names[k]}={c[k]}" for k in sorted(names))
    print(f"{split:<8}{n_imgs:>9}  {detalhe}")
print(f"TOTAL de imagens: {total_imgs}")
