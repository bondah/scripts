# Script to bulk copy and rename files based on a table
# You will need an Excel table with the old values
# https://github.com/bondah

import os, xlrd, shutil

# open Excel file
book = xlrd.open_workbook("E:\Videos\SewerVideoInventory_20180925.xlsx")
sheet = book.sheet_by_index(0)

# build dictionary of feature class updates
mapping = {}
for row in (sheet.row(r) for r in xrange(sheet.nrows)):
    oldpath = row[4].value #old file path
    oldname = row[2].value #old file name
    oldtype = row[3].value #old file type
    newname = row[9].value #new file name
    skip = row[11].value #Yes values in this field for files to skip renaming

    mapping[oldpath] = {'oldname':oldname, 'oldtype':oldtype, 'newname':newname, 'skip':skip}

print "mapping complete"

# go through all video files to rename

rootdir = '\\SEWER\\VIDS\\' #root folder for your videos (can contain subfolders)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(subdir, file)
        print "filename: " + path
        if path in mapping:
            if mapping[path].get('skip') <> "Yes":
                shutil.copy(path, ''.join("E:/Videos/"+str(mapping[path].get('newname'))+str(mapping[path].get('oldtype'))))
                print "newname: " + str(mapping[path].get('newname'))+str(mapping[path].get('oldtype'))

print "complete"            
