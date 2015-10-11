import string
import os
import sys

def pront(x):
    print x

functionsTFF = ""
alreadyOpened = []

# automatically moves all the right functions to the target directory
def importFuncs(targetDir, func="main"):

    global alreadyOpened
    global functionsTFF

    print func

    functionsTFF += func + "\n"
    
    alreadyOpened.append(func)
    
    if os.path.exists(func + ".tfn"):
        currentFile = open(func + ".tfn", "r").readlines()
                                
        for line in currentFile:
            lineSplit = string.split(line, ":")
            command = lineSplit[-1]
            commandSplit = string.split(command)
            if commandSplit != [] and commandSplit[0] == "function":
                functionName = commandSplit[1]
                if not functionName in alreadyOpened:
                    importFuncs(targetDir, functionName)
                
        os.system("mv " + func + ".tfn " + targetDir)
            
    elif os.path.exists("builtin/" + func + ".tfn"):
        currentFile = open("builtin/" + func + ".tfn", "r").readlines()

        for line in currentFile:
            lineSplit = string.split(line, ":")
            command = lineSplit[-1]
            commandSplit = string.split(command)
            if commandSplit != [] and commandSplit[0] == "function":
                functionName = commandSplit[1]
                if not functionName in alreadyOpened:
                    importFuncs(targetDir, functionName)
                
        os.system("cp builtin/" + func + ".tfn " + targetDir)
        
    else:
        pront("Error: dependency file " + func + ".tfn does not exist.")
        raise
        
importFuncs(sys.argv[1])

open(sys.argv[1] + "/functions.tff", "w").write(functionsTFF)