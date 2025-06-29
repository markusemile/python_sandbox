import sys

running = True
option = -1
my_list = []


def display_list():
    for index, val in enumerate(my_list):
        print(f"{index} - {val}")


def display_menu():
    print("Menu\n-----\n1-Add an element to the list \n2-Remove an element of the list \n3- Display the list\n0-Exit")


display_menu()
while running:
    while option not in ["0", "1", "2", "3"]:
        option = input("Please choose an option between [0 - 1 - 2 or 3]")
    if option == "1":
        try:
            my_list.append(input("Please add a new ingredient into the list :"))
            print("new ingredient add successfully")
        except Exception as e:
            print(f"New ingredient was not add successfully\nError: {e}")
    elif option == "2":
        # display list
        if len(my_list) == 0:
            print("Empty list, nothing to delete !")
        else:
            display_list()
            ingredient_to_delete = -1
            while True:
                ingredient_to_delete = input("Choose the ingredient to delete :")
                if ingredient_to_delete.isdigit() and int(ingredient_to_delete) in range(len(my_list)):
                    ingredient_to_delete = int(ingredient_to_delete)
                    break
                print("Invalid index. try Again")

            try:
                my_list.pop(ingredient_to_delete)
                print("The ingredient was successfully deleted")
            except Exception as e:
                print(f"the ingredient was not successfully deleted\n Error: {e}")
    elif option == "3":
        if len(my_list) > 0:
            display_list()
        else:
            print("List is empty")
    else:
        print("Bye Bye")
        running = False
    option = -1
