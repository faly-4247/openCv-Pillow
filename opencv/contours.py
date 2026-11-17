from pathlib import Path

import cv2
import numpy as np
from PIL import Image


root = Path(__file__).resolve().parent.parent
source = root / "images" / "photo.jpg"
output = root / "output" / "photo_contours.png"

if not source.is_file():
    raise SystemExit(f"Image introuvable : {source}")

with Image.open(source) as image:
    rgb = np.asarray(image.convert("RGB"))

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
contours = cv2.Canny(gray, 100, 200)
Image.fromarray(contours).save(output)

print(f"Contours detectes : {output}")
