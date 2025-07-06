import json

chemin = "json_file_test.json"
found = False



# charger le json
try:
    with open(chemin, "r", encoding="utf8") as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print(f"Erreur: Fichier {chemin} non trouvé")
    exit()
except json.JSONDecodeError:
    print(f"Erreur : Le fichier {chemin} n'est pas un json valide")
    exit()

# on change le dict
id_to_change = input("Veuillez enter l'id a changer :")
if id_to_change.isdigit():
    id_to_change = int(id_to_change)
    for user in data["users"]:
        if user["id"] == id_to_change:
            new_name = input("Veuillez entrer le nouveau nom :")
            user["name"] = new_name
            found = True
            print("Nom de l'utilisateur changer avec succes !!")
            break
else:
    print(f"Erreur: Vous devez entrer un nombre")
    exit()

if not found:
    print(f"L'utilisateur avec l'ID {id_to_change} n'à pas été trouvé")

# on réécrit le json
try:
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
except json.JSONEncoder:
    print(f"Erreur: Probleme lors de l'encodage du fichier json.")



