import json

json_path = "liste_de_courses.json"


# menu

def display_menu():
    choice_menu = -1
    while choice_menu not in range(6):
        a = input("""
        MENU
        ----
        [1] Add element
        [2] Delete element
        [3] Modify element
        [4] Display elements list
        [5] Rest list
        
        [0] Exit
        """)
        if a.isdigit() and int(a) in range(6):
            choice_menu = int(a)
    return choice_menu


def create_empty_list():
    with open(json_path, "x", encoding="utf-8") as f:
        print("create empty list")
        json.dump({"list": []}, f, indent=4, ensure_ascii=False)


def display_list():
    list_to_display = get_list()
    if "list" in list_to_display:
        if len(list_to_display["list"])>0:
            for idx, value in enumerate(list_to_display["list"]):
                print(f"[{idx}] - {value}")
        else:
            print("Nothing to display: list empty")
    else:
        print("list not find into file")


def get_list():
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            list_to_read = json.load(f)
            if "list" in list_to_read:
                return list_to_read
            else:
                print("Error json structure")
                exit()
    except FileNotFoundError:
        create_empty_list()
        display_list()
    except json.JSONDecodeError as e:
        print(f"Error: File {json_path} decoding error. Details: {e}")


def save_list(list_to_save):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(list_to_save, f, ensure_ascii=False, indent=4)


def add_element():
    elem = input("Enter a new element : ")
    if elem.strip() != "":
        current_list = get_list()
        current_list["list"].append(elem)
        save_list(current_list)
        print("Element saved with successfully !!")


def delete_elem():
    current_list = get_list()
    size_list = len(current_list["list"])

    if not current_list["list"] and size_list < 1:
        input("Nothing to delete ! List is empty. [enter]")
        return

    display_list()
    while True:
        a = input("Choose the id to delete : (or 'q' to cancel):")

        if a.lower() == 'q':
            input("cancelled ! [enter]")
            break

        if not a.isdigit():
            print("Enter a number, please !")
            continue

        id_to_delete = int(a)

        if id_to_delete not in range(size_list):
            input("Id out of range ! Please choose a correct index.")
            continue

        current_list['list'].pop(id_to_delete)
        save_list(current_list)
        print("Item delete with success !!")
        break


def modify_elem():
    current_list = get_list()
    elem_to_modify = -1
    elem_range = len(current_list["list"])

    while elem_to_modify not in range(len(current_list["list"])):
        display_list()
        a = input("Choice the element to modify")
        if a.isdigit():
            elem_to_modify = int(a)
            if elem_to_modify not in range(len(current_list["list"])):
                print("Choice out of range")

    element_modified = input("Please enter the modification of these element.")
    if len(element_modified) > 0 and element_modified.strip() != "":
        current_list["list"][elem_to_modify] = element_modified

    save_list(current_list)


def reset_list():
    confirm = input("Are you certain  ! You want to delete everything ? Default equal No => [Yes] or [Enter]")
    if confirm == "Yes":
        try:
            with open(json_path, "w") as f:
                json.dump({"list": []}, f)
                input(f"List has been reset !! [enter to continue]")

        except FileNotFoundError as e:
            print(f"File {json_path} was not found.")
    else:
        input(f"You choose {confirm} [enter to continue]")


running = True

while running:
    choice = display_menu()
    match choice:
        case 1: add_element()
        case 2:delete_elem()
        case 3:modify_elem()
        case 4:display_list()
        case 5:reset_list()
        case 0:
            print("Bye Bye")
            exit()
