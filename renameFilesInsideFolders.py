import os

rootdir="networks"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if file != "history.txt":
            print("")
            os.system("mv "+filepath+" "+subdir+os.sep+"ntw-cat1.txt")
            print(file+" renamed to ntw-cat1.txt")
            print("++++++++++++++++++++++++++++++++++++++")
            print("")
