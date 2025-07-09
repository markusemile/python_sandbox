from pathlib import Path


# sort a files into a folder by they extensions

folder_path = Path.home() / "Downloads"
# get all elements in folder and put into list
all_elems = list(folder_path.glob("*"))
# initialisation of a set (no duplicate elem)
all_extension = set()
# get all folder and sorted
fld = [f for f in all_elems if f.is_dir()]
fld.sort()
# get all files and sorted
files = [f for f in all_elems if f.is_file()]
files.sort()

# get all suffix from files
for item in files:
    all_extension.add(item.suffix)

# convert to list and sort the extension
all_extension = list([item for item in all_extension])
all_extension.sort()

# dictionaries of extension with its full name
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
# display folders at first
for folder in fld:
    print(f"[Folder]: {folder.name.capitalize()}")
# next we display the files sorted by extension name and then by alpha
for ext in all_extension:
    for file in files:
        if file.suffix == ext:
            print(f"[file]-[{extension_name.get(ext, 'Other')}]: {file.name.capitalize()}")




