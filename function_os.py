import os
from pprint import pprint
chemin = "C:/programmation/python/"
dossier = os.path.join(chemin, "newdoss")
print(dossier)
if os.path.exists(dossier):
    os.removedirs(dossier)
else:
    os.makedirs(dossier, exist_ok=True)

pprint(dir(os.path))


