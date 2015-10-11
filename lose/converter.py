import os
import sys

fileName = sys.argv[1]

try:
    assert fileName[-5:] == ".lose"
except:
    pront("Error: input file not a lose file")
    raise

dirName = fileName[:-5]

if not os.path.exists(dirName + "/"):
    os.system("mkdir " + dirName)

print "Compiling..."
os.system("python compiler.py " + fileName)
print "Importing dependencies..."
os.system("python importer.py " + dirName)
print "Done!"