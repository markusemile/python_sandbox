from pathlib import Path


# sort a files into a folder by they extensions

folder_path = Path.home() / "Downloads"
all_elems = list(folder_path.glob("*"))
all_extension = set()
fld = [f for f in all_elems if f.is_dir()]
fld.sort()
files = [f for f in all_elems if f.is_file()]
files.sort()

for item in all_elems:
    if item.is_file():
        all_extension.add(item.suffix)

all_extension = [item for item in all_extension]
all_extension.sort()

extension_name ={
    ".png": "Image",
    ".jpg": "Image",
    ".gif": "Image",
    ".jpeg": "Image",
    ".mp4": "Movie",
    ".mkv": "Movie",
    ".mov": "Movie",
    ".zip": "Archive",
    ".rar": "Archive",
    ".pdf": "Document",
    ".json": "Document",
    ".mp3": "Music",
    ".wav": "Music",
    ".exe": "Executable",
    ".apk": "Executable",
    ".msi": "Executable",
    ".jar": "Java"
}

for folder in fld:
    print(f"[Folder]: {folder.name.capitalize()}")

for ext in all_extension:
    for file in files:
        if file.suffix == ext:
            print(f"[file]-[{extension_name.get(ext, 'Other')}]: {file.name.capitalize()}")




