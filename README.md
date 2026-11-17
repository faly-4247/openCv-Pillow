# Projet OpenCV et Pillow

Petit projet d'apprentissage du traitement d'images avec Pillow et OpenCV.

## Prerequis

- Python
- Une image placee dans `images/photo.jpg`

## Installation

Depuis la racine du projet, dans Git Bash :

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

## Lancer les exemples

Les commandes se lancent depuis la racine du projet :

```bash
python main.py
python pillow/recadrer.py
python opencv/contours.py
```

- `main.py` redimensionne l'image et cree une version en niveaux de gris.
- `pillow/recadrer.py` recadre le quart superieur gauche de l'image.
- `opencv/contours.py` detecte les contours de l'image.

Les deux premiers resultats de `main.py` sont crees a la racine. Les autres sont enregistres dans `output/`.

## Image d'entree

Le projet attend le fichier `images/photo.jpg`. Remplace-le par une image que tu peux utiliser et conserve ce nom, ou adapte le chemin dans les scripts. Evite d'ajouter une image personnelle au depot GitHub.