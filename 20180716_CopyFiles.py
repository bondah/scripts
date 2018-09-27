# Copy files based on a text file list
# https://github.com/bondah

import os
import shutil

with open('tiles.txt', 'r') as f: #text file with list of files to extract
    myNames = {line.strip() for line in f}
    print myNames

dir_src = r"E:\Aerials\JPEG2000\4Inch" #source directory
dir_dst = r"H:\project\Transmittal\to_x\20180716 Data" #destination directory

# copy files
for dirpath, dirs, files in os.walk(dir_src):
    for file in files:
        bn,ext = os.path.splitext(file)
        if bn in myNames:
            shutil.copy( os.path.join(dirpath, file), dir_dst )

