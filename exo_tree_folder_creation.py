import os
from pathlib import Path
import shutil

CURRENT_PATH = Path.cwd()

menu = {
    1: "Change current root ",
    2: "create new folder(s)",
    3: "delete folder",
    0: "exit"
}


# 1. Ask the root path
# 2. Display menu (change root/ new tree / del folder / del tree / exit)


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def change_current_path(data):
    global CURRENT_PATH
    CURRENT_PATH = data


def get_tree_folder():
    fld = list([f for f in CURRENT_PATH.glob("*") if f.is_dir()])
    return fld


def change_root():
    while True:
        clear_console()
        print("""
        ****************************
        * CHANGE CURRENT DIRECTORY *
        ****************************
        """)
        print(f"""
        Current path:
        *************
        {CURRENT_PATH}\n""")

        # initialisation
        index = 0
        map_list = {}

        # get the folder list

        # if parent of current path exist, and it's not the last parent

        print("[0]: [return menu]")
        map_list[index] = "cancel"
        index = index + 1

        if CURRENT_PATH.parent.exists() and CURRENT_PATH != CURRENT_PATH.parent:
            print(f"[{index}]: ../{CURRENT_PATH.parent.stem} [parent]")
            map_list[index] = CURRENT_PATH.parent
            index = index + 1

        folders = get_tree_folder()

        for folder in folders:
            print(f"[{index}]: {folder.name}")
            map_list[index] = folder
            index += 1

        choices = input("\nPlease choose a folder index: ")
        if not choices.isdigit() or int(choices) not in map_list:
            input("⚠️  Invalid choice. Press Enter to try again...")
            continue

        choices = int(choices)

        if choices == 0:
            break

        change_current_path(map_list[choices])


def create_folder():
    while True:
        clear_console()
        l1 = "*" * (len(str(CURRENT_PATH)) + 25)
        print(f"""
        {l1}
        Create a new folder into {CURRENT_PATH}
        {l1}
        """)
        cf_choice = input("""
        Please enter the path you want to create.
        Please separate each folder with a / 
        (ex: folder/child1/child2 or folderName)
        [ENTER to return menu]
        """)
        array_path = cf_choice.split("/")
        path = CURRENT_PATH / cf_choice
        if len(cf_choice) > 0:
            try:
                path.mkdir(exist_ok=True, parents=True)
                input(f"Folder {cf_choice} created with success !\n[enter]")
            except OSError as e:
                input(f"Error: {e}\n[enter]")
        break


def delete_folder():
    map_folder = {0: "cancel"}
    df_idx = 1
    while True:
        clear_console()
        l1 = "*" * (len(str(CURRENT_PATH)) + 25)
        print(f"""
        {l1}
        Delete a folder(s) into {CURRENT_PATH}
        {l1}
        """)
        df_folders = get_tree_folder()
        print("[0]: cancel")
        for i, v in enumerate(df_folders):
            print(f"[{i + df_idx}]: {v.stem}")
            map_folder[i + df_idx] = df_folders[i]

        df_choice = input("Enter the ID of the folder you want to delete :")
        if not df_choice.isdigit() or int(df_choice) not in map_folder:
            df_choice = input("Id out of range ! [enter]:")
            continue

        df_choice = int(df_choice)

        if df_choice == 0:
            break

        # check if folder empty
        empty_folder = list(map_folder.get(df_choice).glob("*"))
        confirm_delete = "n"

        if len(empty_folder) > 0:
            print("********************\nFolder not empty !!\n********************\n")

        confirm_delete = input("Are you sure, you want deleted it ? [Yes][No]: (default :n) ")

        if confirm_delete.lower() == "y":
            try:
                shutil.rmtree(CURRENT_PATH / map_folder[df_choice])
                input("Folder was deleted with success [enter]")
            except OSError as e:
                input(f"Error: {e}\n [enter]")

        break


while True:
    clear_console()
    print(f"\nCurrent folder: {CURRENT_PATH}\n")
    print("""
    *************
    * MAIN MENU *
    *************
    """)
    for idx, value in menu.items():
        print(f"[{idx}]: {value}")
    choice = input(f"Make your selection [0-{len(menu) - 1}]: ")

    if not choice.isdigit() or int(choice) not in menu:
        input(f"Please choice a number between 0 and {len(menu) - 1} [press enter]!")
        continue

    choice = int(choice)
    match choice:
        case 0:
            break
        case 1:
            change_root()
        case 2:
            create_folder()
        case 3:
            delete_folder()
