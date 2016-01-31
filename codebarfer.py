import sys
import string
import math


# Watch out! This uses the lower-level, a-b alphabet

from writer import getFunctionLabelDictionary, getFunctionVariableDictionary, \
    convertNumberToBarCode
from state import *
from tmreader import getSymbolMapping, alphabetMTToST, alphabetMSToTS, \
    convertStatesToString

def incrementWord(word):
    
    if word == "":
        return ""
    
    elif word[-1] == "a":
        return incrementWord(word[:-1]) + "b"
    
    else:
        return word[:-1] + "a"

# Converts a number to a string of wordSize a's and b's
def indexToWordMaker(wordSize, numWords):
    indexToWordDict = {}
    
    currentWord = "b"*wordSize
    
    for index in range(numWords):
        
        indexToWordDict[index] = currentWord
        
        currentWord = incrementWord(currentWord)
        
    return indexToWordDict

# This function does the naive thing of writing out the string one state at a time.
# It shouldn't be used in the final thing; this is for testing purposes.
def codeBarf(codeStringInAB):
    listOfStates = [State("write_code_symbol_" + str(i), \
        None, alphabetMSToTS()) for i in range(len(codeStringInAB))]
    listOfStates[0].isStartState = True
    
    for i, symbol in enumerate(codeStringInAB[:-1]):
        listOfStates[i].set3("a", listOfStates[i+1], "R", symbol)

    listOfStates[-1].set3("a", SimpleState("OUT"), "R", codeStringInAB[-1])

    convertStatesToString(listOfStates, open(sys.argv[2], "w"))

# The total length of the string we can represent with words of size wordSize
def computeNumCharsTotalFromWordSize(wordSize):
    return wordSize * 2**wordSize

def findAppropriateWordSize(numChars, wordSizeAttempt=2):
    if computeNumCharsTotalFromWordSize(wordSizeAttempt-1) < numChars \
        and computeNumCharsTotalFromWordSize(wordSizeAttempt) > numChars:
        
        return wordSizeAttempt
    
    else:
        return findAppropriateWordSize(numChars, wordSizeAttempt+1)

def createBlankWord(inState, wordSize, listOfStates):
    previousState = inState
    
    for i in range(1, wordSize):
        nextState = State("create_blank_word_" + str(i))
        
        previousState.set3()

def breakUpCodeString(wordSize, numWords, codeStringInAB):
    numCharsTotal = wordSize * numWords
    pad = (numCharsTotal - len(codeStringInAB))*"a"
    
    paddedCodeString = codeStringInAB + pad
    
#    print paddedCodeString
    
    brokenUpWords = []
    
    for i in range(numWords):
        brokenUpWords.append(paddedCodeString[i*wordSize:(i+1)*wordSize])
        
#        print paddedCodeString[i*wordSize:(i+1)*wordSize]
        
    return brokenUpWords

# This is the function where the introspective magic happens. 
# These states encode data via the way in which they point to each other.
def organizeDataStates(inState, wordSize, numWords, codeStringInAB, listOfStates):
    indexToWord = indexToWordMaker(wordSize, numWords)
        
    listOfStates.append(inState)
    
    wordToState = {"b"*wordSize: inState}
    indexToState = {0: inState}
    
    brokenUpWords = breakUpCodeString(wordSize, numWords, codeStringInAB)
        
    # start at 1 because inState is 0
    for i in range(1, numWords):
        
        word = indexToWord[i]
        
        state = State("data_" + str(i) + "_" + word, None, alphabetMSToTS())
        
        wordToState[word] = state
        indexToState[i] = state
        
        listOfStates.append(state)
        
    outState = State("data_out", None, alphabetMSToTS())    
                
    for i in range(numWords-1):
        state = indexToState[i]
        
        # This is it! This is the encoding!
        state.set3("a", indexToState[i+1], "R", "b")
        state.set3("b", wordToState[brokenUpWords[i]], "R", "a")
        
    lastDataState = indexToState[numWords-1]
    
    lastDataState.set3("a", outState, "R", "a")
    lastDataState.set3("b", wordToState[indexToWord[numWords-1]], "R", "a")
        
    return outState        

def createBlankCharacter(inStateA, inStateB, name, isFirstChar, listOfStates):
    # inStateA might have been called pushToFinStateA
    # inStateB might have been called pushToFinStateB
    findFirstAStateLeft = State(name + "_find_first_a_left", None, alphabetMSToTS())
    findSecondAState = State(name + "_find_second_a", None, alphabetMSToTS())
    writeBlankChar = State(name + "_write_blank_char", None, alphabetMSToTS())
    goRight = State(name + "_go_right", None, alphabetMSToTS())
    findFirstAStateRight = State(name + "_find_first_a_right", None, alphabetMSToTS())
    pushMiddleAState = State(name + "_push_middle_a", None, alphabetMSToTS())
    outStateA = State(name + "_out_a", None, alphabetMSToTS())
    outStateB = State(name + "_out_b", None, alphabetMSToTS())
                
    inStateA.set3("a", findFirstAStateLeft, "L", "a")
        
    if inStateB != None:    
        inStateB.set3("a", findFirstAStateLeft, "L", "b")
        inStateB.set3("b", inStateB, "R", "b")
        
        listOfStates.append(inStateB)

    listOfStates.extend([inStateA, findFirstAStateLeft, \
         findSecondAState, writeBlankChar, goRight, \
        findFirstAStateRight, pushMiddleAState])
        
    findFirstAStateLeft.set3("a", findSecondAState, "L", "a")
    findFirstAStateLeft.set3("b", findFirstAStateLeft, "L", "b")
    
    findSecondAState.set3("a", writeBlankChar, "R", "a")
    findSecondAState.set3("b", findSecondAState, "L", "b")
    
 #   goRight.set3("a", writeBlankChar, "R", "a")
    
    writeBlankChar.set3("a", pushMiddleAState, "R", "a")
    writeBlankChar.set3("b", findFirstAStateRight, "R", "a")
    
    findFirstAStateRight.set3("a", pushMiddleAState, "R", "b")
    findFirstAStateRight.set3("b", findFirstAStateRight, "R", "b")
    
    pushMiddleAState.set3("a", outStateA, "R", "a")
    pushMiddleAState.set3("b", outStateB, "R", "a")
    
    return outStateA, outStateB

def createBlankWord(inState, wordSize, listOfStates):
    inStateA, inStateB = inState, None
    
    for i in range(wordSize):
        isFirstChar = (i == 0)
        
        inStateA, inStateB = createBlankCharacter(inStateA, inStateB, \
            "create_blank_char_" + str(i), isFirstChar, listOfStates)
    
    
    outState = State("create_blank_word_out", None, alphabetMSToTS())
    
    goLeft = State("create_blank_go_left", None, alphabetMSToTS())
    
    inStateA.set3("a", goLeft, "R", "a")
    
    goLeft.set3("a", outState, "L", "a")

    # finish the last push-down    
    inStateB.set3("a", outState, "R", "b")
    inStateB.set3("b", inStateB, "R", "b")
        
    listOfStates.extend([inStateA, inStateB, goLeft])
    
    return outState
    
def testForFinalB(inState, listOfStates):
    theEnd = State("test_positive_end", None, alphabetMSToTS())
    keepGoing = State("test_negative_continue", None, alphabetMSToTS())
    
    listOfStates.extend([inState])
    
    inState.set3("a", keepGoing, "L", "a")
    inState.set3("b", theEnd, "L", "a")    
    
    return keepGoing, theEnd
    
def incrementBinaryCounter(inState, wordSize, name, listOfStates):
    # inState might have been called digit0Carry
    
    outState = State(name + "out", None, alphabetMSToTS())
    
    carryStates = {}
    noCarryStates = {}
    getOutStates = {}
    
    listOfStates.append(inState)
    
    for i in range(1, wordSize):
        carryStates[i] = State(name + "_carry_" + str(i), None, alphabetMSToTS())
        noCarryStates[i] = State(name + "_no_carry_" + str(i), None, alphabetMSToTS())  
        getOutStates[i] = State(name + "_get_out_" + str(i), None, alphabetMSToTS())  
        
        listOfStates.extend([carryStates[i], noCarryStates[i], getOutStates[i]])
    
    inState.set3("a", noCarryStates[1], "L", "b")
    inState.set3("b", carryStates[1], "L", "a")
    
    for i in range(1, wordSize-1):
        carryStates[i].set3("a", noCarryStates[i+1], "L", "b")
        carryStates[i].set3("b", carryStates[i+1], "L", "a")
        
        noCarryStates[i].set3("a", noCarryStates[i+1], "L", "a")
        noCarryStates[i].set3("b", noCarryStates[i+1], "L", "b")
        
        getOutStates[i].set3("a", getOutStates[i+1], "R", "a")
        getOutStates[i].set3("b", getOutStates[i+1], "R", "b")
        
    carryStates[wordSize-1].set3("a", getOutStates[1], "R", "b")
    
    noCarryStates[wordSize-1].set3("a", getOutStates[1], "R", "a")
    noCarryStates[wordSize-1].set3("b", getOutStates[1], "R", "b")
    
    getOutStates[wordSize-1].set3("a", outState, "R", "a")
    getOutStates[wordSize-1].set3("b", outState, "R", "b")
    
    return outState
    
    
def convertUnaryToBinary(inState, wordSize, firstDataState, name, listOfStates):
    # inState might have been called getToFin
    deleteLastB = State(name + "_delete_last_b", None, alphabetMSToTS())
    getToFirstALeft = State(name + "_get_to_first_a_left", None, alphabetMSToTS())
    getToSecondALeft = State(name + "_get_to_second_a_left", None, alphabetMSToTS())
    increment = State(name + "_increment", None, alphabetMSToTS())
    getToSecondARight = State(name + "_get_to_second_a_right", None, alphabetMSToTS())
    makeNewB = State(name + "_make_new_b", None, alphabetMSToTS())
    moveLeft = State(name + "_move_left", None, alphabetMSToTS())
    cleanUpMess = State(name + "_clean_up_mess", None, alphabetMSToTS())
    
    listOfStates.extend([inState, deleteLastB, getToFirstALeft, getToSecondALeft,
        getToSecondARight, makeNewB, moveLeft, cleanUpMess])
    
    inState.set3("a", deleteLastB, "L", "a")
    inState.set3("b", inState, "R", "b")
    
    deleteLastB.set3("a", makeNewB, "R", "a")
    deleteLastB.set3("b", getToFirstALeft, "L", "a")
    
    getToFirstALeft.set3("a", getToSecondALeft, "L", "a")
    getToFirstALeft.set3("b", getToFirstALeft, "L", "b")
    
    getToSecondALeft.set3("a", increment, "L", "a")
    getToSecondALeft.set3("b", getToSecondALeft, "L", "b")
    
    doneIncrementing = incrementBinaryCounter(increment, wordSize, name + "_incr", listOfStates)
    listOfStates.append(doneIncrementing)
    
    doneIncrementing.set3("a", getToSecondARight, "R", "a")
    
    getToSecondARight.set3("a", inState, "R", "a")
    getToSecondARight.set3("b", getToSecondARight, "R", "b")
        
    makeNewB.set3("a", moveLeft, "L", "b")
    
    moveLeft.set3("a", cleanUpMess, "L", "a")
    
    cleanUpMess.set3("a", firstDataState, "R", "a")
    cleanUpMess.set3("b", cleanUpMess, "L", "a")
    
def introspect(codeStringInAB):
    
    wordSize = findAppropriateWordSize(len(codeStringInAB))
    numWords = 2**wordSize
        
    markerA = State("preamble_write_marker_a", None, alphabetMSToTS())
    firstBSignal = State("preamble_first_b_signal", None, alphabetMSToTS())
    goLeft = State("preamble_go_left", None, alphabetMSToTS())
    lastCleanUp = State("epilogue_clean_up", None, alphabetMSToTS())
    findCodeHead = State("epilogue_find_code_head", None, alphabetMSToTS())
    foundCodeHead = State("epilogue_found_code_head", None, alphabetMSToTS())
    firstDataState = State("data_0_" + ("b"*wordSize), None, alphabetMSToTS())

    listOfStates = [markerA, firstBSignal, goLeft, lastCleanUp, findCodeHead, foundCodeHead]

    markerA.makeStartState()

    markerA.set3("a", firstBSignal, "R", "a")
    firstBSignal.set3("a", goLeft, "L", "b")
    goLeft.set3("a", firstDataState, "R", "a")
    
    inState = organizeDataStates(firstDataState, wordSize, numWords, codeStringInAB, listOfStates)
    inState, endState = testForFinalB(inState, listOfStates)    
    inState = createBlankWord(inState, wordSize, listOfStates)
    convertUnaryToBinary(inState, wordSize, firstDataState, "convert", listOfStates)
    
    endState.set3("a", lastCleanUp, "L", "a")

    lastCleanUp.set3("a", findCodeHead, "L", "a")
    lastCleanUp.set3("b", lastCleanUp, "L", "a")
    
    findCodeHead.set3("a", findCodeHead, "L", "a")
    findCodeHead.set3("b", foundCodeHead, "R", "b")
    
    listOfStates.append(endState)
    
    foundCodeHead.set3("a", SimpleState("OUT"), "R", "a")
    
    convertStatesToString(listOfStates, open(sys.argv[2], "w"))
    
def alphabetMSToTS():
    return ["a", "b"]
    
def convertToAB(s):
    returnString = ""
    
    symbolMapping = getSymbolMapping()[0]
    
#    print symbolMapping
	
    for symbol in s:
        returnString += symbolMapping[symbol]
        
    return returnString

def findProgramSkeleton(listOfStates, inState, functions, functionVariableDictionary, \
    functionLabelDictionary, functionDictionary, path):
    
    listOfFunctionGroups = []
    characteristicString = ""
                
    for i, function in enumerate(functions):
        functionName = function
        functionLines = open(path + functionName + ".tfn", "r").readlines()
        if i == 0:
            functionGroup = FunctionGroup(functionName, functionLines, functionVariableDictionary, \
                functionLabelDictionary, functionDictionary, convertNumberToBarCode, \
                listOfStates, inState, True)
        else:
            functionGroup = FunctionGroup(functionName, functionLines, functionVariableDictionary, \
                functionLabelDictionary, functionDictionary, convertNumberToBarCode, \
                listOfStates)           
        listOfFunctionGroups.append(functionGroup)
        characteristicString += functionGroup.charString
        
    for i, functionGroup in enumerate(listOfFunctionGroups[:-1]):
        functionGroup.attach(listOfFunctionGroups[i+1])
        
    outState = State("write_code_skeleton_out")

    listOfFunctionGroups[-1].outState.setNextState("_", outState)
        
    return characteristicString

if __name__ == "__main__":
    
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
        raise Exception("No initvar file found in directory " + path)

###################################################################
    
    # An antiquated thing from back when writeProgramSkeleton used to make the states
    # itself, instead of just telling us what the string should be.
    throwawayList = []
    throwawayState = State("foo")
    
    codeString = findProgramSkeleton(throwawayList, throwawayState, functions, 
        functionVariableDictionary, functionLabelDictionary, functionDictionary, path)
            
    codeStringInAB = convertToAB(codeString)
    
#    codeStringInAB = "bbbbb" + codeStringInAB[5:]
        
#    codeBarf(codeStringInAB)

    introspect(codeStringInAB)