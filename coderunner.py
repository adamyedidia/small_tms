# This program outputs the TM that does everything after the code has been written down.
import sys
import string

from state import State

from writer import getFunctionLabelDictionary, getFunctionVariableDictionary, \
    incrementLineNumberIDs, markFunctionNames, incrementFunctionIDs, firstPrepTopFunction, \
    convertStatesToString

from cpu import processCentrally

def main():
    path = sys.argv[1]

    try:
        functions = [string.strip(x) for x in open(path + "functions.tff", "r").readlines()]
    except:  
        print "No functions.tff file found in directory " + path
        raise 

    functionLabelDictionary, functionDictionary, _, _ = getFunctionLabelDictionary(functions, path)
    functionVariableDictionary = getFunctionVariableDictionary(functions, path)

###################################################################

    try:
        initValueString = string.strip(open(path + "initvar", "r").read()) + "H"
    except:
        print "No initvar file found in directory " + path
        raise 

###################################################################

    inState = State("start_runner")
    inState.makeStartState()

    listOfStates = []

    mainFunctionInputLine = open(path + functions[0] + ".tfn", "r").readlines()[0]

    numberOfVariables = len(string.split(mainFunctionInputLine)) - 1
    numberOfFunctions = len(functions)
	
    inState = incrementLineNumberIDs(listOfStates, inState)
    inState = markFunctionNames(listOfStates, inState)
    inState = incrementFunctionIDs(listOfStates, inState)
    inState = firstPrepTopFunction(inState, listOfStates, "first_prep")
    inState = processCentrally(inState, listOfStates)
	
    convertStatesToString(listOfStates, open(sys.argv[2], "w"))
	

if __name__ == "__main__":
    main()