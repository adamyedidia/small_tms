import sys
import string
import math
from writer import *
from cpu import *

   
def main():
    path = sys.argv[1]

    try:
        functions = [string.strip(x) for x in open(path + "functions.tff", "r").readlines()]
    except:  
        raise Exception("No functions.tff file found in directory " + path) 

    functionLabelDictionary, functionDictionary, _, _ = getFunctionLabelDictionary(functions, path)
    functionVariableDictionary = getFunctionVariableDictionary(functions, path)

###################################################################

    try:
        initValueString = string.strip(open(path + "initvar", "r").read()) + "H"
    except:
        raise Exception("No initvar file found in directory " + path)

###################################################################

    inState = State("start")
    inState.makeStartState()

    listOfStates = []
    
    mainFunctionInputLine = open(path + functions[0] + ".tfn", "r").readlines()[0]
    
    numberOfVariables = len(string.split(mainFunctionInputLine)) - 1
    numberOfFunctions = len(functions)
    
    inState = write(listOfStates, inState, numberOfVariables, initValueString, numberOfFunctions, \
        functions, functionVariableDictionary, functionLabelDictionary, functionDictionary, path)
    inState = processCentrally(inState, listOfStates)
    
    convertStatesToString(listOfStates, open(sys.argv[2], "w"))
    
if __name__ == "__main__":    
    main()
 
