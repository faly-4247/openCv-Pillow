from pathlib import Path

import cv2
from PIL import Image


image_path = Path("images") / "photo.jpg"
output_path = Path("photo_reduite.png")
grayscale_output_path = Path("photo_gris.png")

if not image_path.is_file():
    raise SystemExit(
        f"Image introuvable : {image_path}\n"
        "Ajoute une image dans le dossier images et nomme-la photo.jpg."
    )

with Image.open(image_path) as image:
    print(image.format, image.size, image.mode)
    image.thumbnail((300, 300))
    image.save(output_path)

print(f"Image redimensionnee et enregistree : {output_path}")

opencv_image = cv2.imread(str(image_path))
if opencv_image is None:
    raise SystemExit(f"Impossible de lire l'image avec OpenCV : {image_path}")

grayscale_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
Image.fromarray(grayscale_image).save(grayscale_output_path)

print(f"Image en niveaux de gris enregistree : {grayscale_output_path}")
