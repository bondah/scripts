# Script to bulk reformat videos to mp4
# This uses an Excel table of values to indicate which videos should be reformatted
# you will need ffmpeg: https://www.ffmpeg.org/
# https://github.com/bondah

import os, xlrd, shutil, ffmpeg, subprocess

# open Excel file
book = xlrd.open_workbook("E:\\Videos\\SewerVideoInventory_20180925.xlsx")
sheet = book.sheet_by_index(0)

# build dictionary of feature class updates
mapping = {}
for row in (sheet.row(r) for r in xrange(sheet.nrows)):
    name = row[9].value #file name
    skip = row[11].value #Yes values in this field for files to skip renaming
    archive = row[10].value #N values indicate file is not being archived (not reforatting archived files)

    mapping[name] = {'skip':skip, 'archive':archive}

print "mapping complete"

# go through all video files to reformat

rootdir = 'E:\\Videos\\'

app_path = os.path.join('C:\\', 'FOSS', 'ffmpeg', 'bin') #set PATH to ffmpeg files (if you have admin rights you can set this permanently outside the script)
os.environ["PATH"] += os.pathsep + app_path

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename, extension = os.path.splitext(file)
        if filename in mapping:
            if mapping[filename].get('skip') <> "Yes":
                if mapping[filename].get('archive') == "N":
                    outfile = filename + ".mp4"
                    try:
                        subprocess.call("ffmpeg -i "+file+" "+outfile)
                        print "reformatted: "+file
                        os.remove(file)
                        print "deleted: "+file
                    except:
                        print file+" could not be reformatted"

print "complete"
