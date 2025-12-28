import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# to check our current directory
# print(ROOT_PATH)

# creating a new directory
os.mkdir(ROOT_PATH / '05-new_dir')

# creating and wrinting in a new file
file = open(ROOT_PATH/'05-new.txt', 'w')
file.write('omg hiii !!')
file.close()

# renaming the file
os.rename(ROOT_PATH/'05-new.txt', ROOT_PATH/'05-renamed.txt')

# deleting a file
rm_file = open(ROOT_PATH/'05-file.txt', 'w')
rm_file.close()
os.remove(ROOT_PATH/'05-file.txt')

# moving files
shutil.move(ROOT_PATH/'05-renamed.txt', ROOT_PATH/'05-new_dir'/'05-renamed.txt')