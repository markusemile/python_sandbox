
chemin = "test.txt"
with open(chemin, "r") as f:
    contenu_read = f.read()
    f.seek(0)
    contenu_repr_f_read = repr(f.read())
    f.seek(0)
    contenu_repr_f_readlines = repr(f.readlines())
    f.seek(0)
    contenu_splitlines = f.read().splitlines()
    print(contenu_read)
    print("\n")
    print(contenu_repr_f_read)
    print("\n")
    print(contenu_repr_f_readlines)
    print("\n")
    print(contenu_splitlines)

with open(chemin, "a+") as f:
    text_to_add = "\nnouveau texte"
    f.write(text_to_add)
    f.seek(0)
    t = f.read().splitlines()
