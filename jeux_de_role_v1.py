import random

mes_potions = 1
potion_add = 5
ma_force = random.randrange(5, 15)
nombre_de_mort = 0
option = -1
running = True


def display_status(ef):
    print(f"""

    -> ma force: {ma_force}
    -> force ennemi: {ef} 
    ->->

    """)


while running:

    menu_option = input(""" Choisissez une option :
    1: Attaquer un ennemi
    2: Voir mes stats
    3: Quitter""")

    if menu_option in ["1", "2", "3"]:
        if menu_option == "1":
            ennemi_force = random.randrange(5, 20)
            tour = 0
            display_status(ennemi_force)
            while not(ennemi_force <= 0 or ma_force <= 0):
                if tour == 0:
                    print("1 - Attaquer")
                    if mes_potions > 0:
                        print("2 - Prendre une potion ")
                    choix = input("Que voulez vous faire : [1-2]")
                    if choix == "1":
                        attack = random.randint(1,10)
                        ennemi_force -= attack
                        print(f"Vous attaquer avec une force de {attack}.")
                        display_status(ennemi_force)
                    elif choix == "2":
                        ma_force += potion_add
                        mes_potions -= 1
                    tour = 1
                elif tour == 1:
                    attack = random.randint(1,10)
                    ma_force -= attack
                    print(f"Vous êtes attaquer avec une force de {attack}.")
                    display_status(ennemi_force)
                    tour = 0
                input("Tour suivant...appuyer sur [enter]")

            if ennemi_force <= 0:
                print("Bravo, vous avez battu votre ennemi !")
                random_potion = random.randint(0, 3)
                print(f"Vous fouiller le cadavre de votre ennemi et trouver {random_potion} potions !")
                nombre_de_mort += 1
            else:
                print("Dommage, vous êtes mort !")
                replay = input("""
                Voulez-vous rejoué ?
                [0] Oui
                [1] Non
                """)
                if replay == "0":
                    ma_force = random.randrange(5, 15)
                    mes_potions = 1
                    continue
                else:
                    break

        if menu_option == "2":
            print("2")
            menu_option = 0

        if menu_option == "3":
            break
