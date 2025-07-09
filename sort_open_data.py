import unicodedata
from pathlib import Path

file_path = Path.cwd() / "prenom.txt"
liste = ''

with open(file_path, "r+", encoding="utf-8") as f:
    firstname = unicodedata.normalize("NFD", repr(f.read())).split(",")
    stripped = [f.strip('\'  ') for f in firstname]
    stripped.sort()
    liste = ",".join(stripped)
    f.close()

with open("prenom_sorted.txt", "a+", encoding="utf-8") as f:
    f.write(liste)
    f.close()
