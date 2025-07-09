from pathlib import Path

user_folder = Path.home() / "Documents"
input("""
*******************************
Show all element in folder [0]
*******************************

for item in user_folder.iterdir():
    print(item.name)
    
""")
for item in user_folder.iterdir():
    print(item.name)

input(f"""\n
*************************************
Show all folder in {user_folder} [0]
*************************************
folders = [item.name for item in user_folder.iterdir() if item.is_dir()]
for f in folders:
    print(f)

""")
folders = [item.name for item in user_folder.iterdir() if item.is_dir()]
for f in folders:
    print(f)

print("""
\n**************************************************
show all pdf file => a = user_folder.glob('*.pdf')
**************************************************
for item in user_folder.glob("*.pdf"):
    print(item.name)
    
""")
for item in user_folder.glob("*.pdf"):
    print(item.name)

print("""
\n**************************************************
show all pdf file in recursif folders => a = user_folder.rglob('*.pdf')
**************************************************
for item in user_folder.glob("*.pdf"):
    print(item.name)

""")
for item in user_folder.rglob("*.pdf"):
    print(item.name)
