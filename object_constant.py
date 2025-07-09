import os
from pathlib import Path

print("\nWith os\n")
# with os
SOURCE_FILE = os.path.realpath(__file__)
print(SOURCE_FILE)
SOURCE_DIR = os.path.dirname(SOURCE_FILE)
print(SOURCE_DIR)
ROOT_DIR = os.path.dirname(SOURCE_DIR)
print(ROOT_DIR)
DATA_DIR = os.path.join(SOURCE_DIR, "DATA")
print(DATA_DIR)

print("\nWith pathlib\n")
# with pathlib
SOURCE_FILE = Path(__file__).resolve()
print(SOURCE_FILE)
SOURCE_DIR = SOURCE_FILE.parent
print(SOURCE_DIR)
ROOT_DIR = SOURCE_DIR.parent
print(ROOT_DIR)
DATA_DIR = SOURCE_DIR / "DATA"
print(DATA_DIR)



