#demander a l'utilisateur 2 nombres
def saisie():
    n1 = int(input("Entrez un premier nombre : "))
    n2 = int(input("Entrez un deuxieme nombre : "))
    return n1,n2
def addition(n1,n2):
    return n1+n2 if n1>0 and n2>0 else 0

def maine():
    n1,n2 = saisie()
    print(addition(n1,n2))
    return

maine()
