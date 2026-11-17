from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
source = root / "images" / "photo.jpg"
output = root / "output" / "photo_recadree.png"

if not source.is_file():
    raise SystemExit(f"Image introuvable : {source}")

with Image.open(source) as image:
    width, height = image.size
    crop = image.crop((0, 0, width // 2, height // 2))
    crop.save(output)

print(f"Image recadree : {output}")