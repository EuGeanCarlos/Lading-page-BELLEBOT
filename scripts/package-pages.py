"""Empacota apenas os recursos públicos versionados do projeto original."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.'
FILES = ['a.animated-button.thar-four {.css', 'img/BALLERINI.svg', 'img/Vector.svg', 'img/balle-bot.svg', 'index.html', 'style.css']
DEST = ROOT / "_site"
DEST.mkdir(exist_ok=True)
for name in FILES:
    target = DEST / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / name, target)
assert (DEST / "index.html").is_file(), "Entrada index.html ausente"
(DEST / ".nojekyll").touch()
