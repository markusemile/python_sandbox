from pathlib import Path
import shutil

user_folder = Path.home()
print(f"\nDossier utilisateur: Path.home() => {user_folder}")
current_folder = Path.cwd()
print(f"Dossier courant: Path.cwd() => {current_folder}")
target_folder = Path("/Users/Papa/Documents")
print(f"Crée un dossier cible: target_folder = Path(\"Users/Papa/Documents\") => {target_folder}")
target_folder_parent = target_folder.parent
print(f"Paretn du dossier cible: target_folder_parent = target_folder.parent => {target_folder_parent}")

# concatenation path
print("\nconcatenation de chemin")

doc_path = user_folder / "Documents" / "exemple_file.py"
print(f"user_folder / 'Documents' / 'exemple_file.py' |or| user_folder.joinpath(\"Documents\", \"exemple_file.py\") => {doc_path}")

# display suffix of file
suffix = (user_folder / "Documents" / "exemple_file.py").suffix
print("\nDisplay suffix of file")
print(f"(user_folder / \"Documents\" / \"exemple_file.py\").suffix => {suffix}")

# some methode
print("\nSome methods")
p = Path("/users/Papa/Documents/test.txt")
print("p=Path(\"/users/Papa/Documents/test.txt\"")
print(f"p.name => {p.name}")
print(f"p.parent => {p.parent}")
print(f"p.parent.name => {p.parent.name}")
print(f"p.parent.parent => {p.parent.parent}")
print(f"p.stem => {p.stem}")
print(f"p.suffix => {p.suffix}")
print(f"p.suffixes => {p.suffixes}")
print(f"p.parts => {p.parts}")
print(f"p.exists() => {p.exists()}")
print(f"p.is_dir() => {p.is_dir()}")
print(f"p.is_file() => {p.is_file()}")

print("\ncreate and delete folder")
fld_test = user_folder / "Documents" / "tempoFolder"
print(f"Is file exist ? fld_test.exists()=> {fld_test.exists()}")
a = input("create the folder : fld_test.mkdir(exist_ok=True) [0]")
fld_test.mkdir(exist_ok=True)
print(f"Is file exist now ? fld_test.exists()=> {fld_test.exists()}")
a = input("delete the folder : fld_test.rmdir() [0]")
try:
    fld_test.rmdir()
except OSError:
    shutil.rmtree(fld_test)
    print(f"Removed the tree of '{fld_test}' folder. ")
else:
    print(f"Removed the '{fld_test}' folder. ")
print(f"Is fld_test exist ? => {fld_test.exists()}")
print(f"Is file exist now ? fld_test.exists()=> {fld_test.exists()}")
input("Create folder test : fld_test.mkdir() [0]")
fld_test.mkdir(exist_ok=True)

# create a tree of folders
input("Create folder tempoFolder/1/2/3 with parent if not exist [0]")
print("""\n
fld_test / 1 / 2 / 3
fld_test.mkdir(exist_ok=True, parents=True)\n
""")
fld_test_3 = fld_test / "1" / "2" / "3"
fld_test_3.mkdir(exist_ok=True, parents=True)
print(f"Is fld_test exist ? {fld_test_3.exists()}")

# create file
input(f"create a file 'info.txt' into {fld_test_3.parent} => new_file.touch() [0]")
new_file = fld_test_3.parent / "info.txt"
new_file.touch()
print(f"Is {new_file} exist? => new_file.exists()= {new_file.exists()}")
print(f"Is {new_file} is file ? => new_file.is_file()= {new_file.is_file()}")
input("Add new file lowres [0]")
new_lowres_file = fld_test_3.parent / (new_file.stem + "_lowres_" + new_file.suffix)
new_lowres_file.touch()
# read and write into file
input(f"Write 'Hello world' into {new_file} => new_file.write_text('Hello world') [0]")
new_file.write_text("Hello world")
print(f"Read {new_file} => print(\"new_file.read_text()\")")
print(new_file.read_text())
input(f"Remove {new_file} => new_file.unlink() [0]")
new_file.unlink()
print(f"Is {new_file} exist? => new_file.exists()= {new_file.exists()}")

# remove tree folders
input(f"Remove the tree of '{fld_test}' folder. => shutil.rmtree(fld_test) [0]")
shutil.rmtree(fld_test)
print(f"Is fld_test exist ? => {fld_test.exists()}")


