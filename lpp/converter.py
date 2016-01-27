import os
import sys

def pront(x):
    print x

fileName = sys.argv[1]

try:
    assert fileName[-4:] == ".lpp"
except:
    pront("Error: input file not a lose++ file")
    raise

dirName = fileName[:-4]

if not os.path.exists(dirName + "/"):
    os.system("mkdir " + dirName)

print "Compiling..."
os.system("python compiler.py " + fileName)
print "Importing dependencies..."
os.system("python importer.py " + dirName)
print "Done!"