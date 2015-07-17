import sys
import string
import math
from state import *
from stateTemplates import *

def prepTopFunction(inState, listOfStates, name):
    markFirstFunctionState = State(name + "_mark_first_fn")
    writeHState1 = State(name + "_write_H_1")
    getRidOfSeparatorState = State(name + "_no_separator")
    findTwoUnderscoresState = State(name + "_find_2_underscores")
    writeHState2 = State(name + "_write_H_2")
    outState = State(name + "_out")
	
    listOfStates.extend([inState, markFirstFunctionState, writeHState1, getRidOfSeparatorState, \
    	findTwoUnderscoresState, writeHState2])
	
    findPattern(inState, markFirstFunctionState, listOfStates, name + "_mark_first_fn", "HH", "L", "R", "H")
    
    moveBy(markFirstFunctionState, name + "_mark_first_fn", 2, "R", writeHState1, listOfStates)

    writeHState1.set3("_", getRidOfSeparatorState, "L", "H")
    
    getRidOfSeparatorState.set3("_", getRidOfSeparatorState, "L", "_")
    getRidOfSeparatorState.set3("1", findTwoUnderscoresState, "-", "1")
    getRidOfSeparatorState.set3("H", getRidOfSeparatorState, "-", "_")
    getRidOfSeparatorState.set3("E", findTwoUnderscoresState, "-", "E")
    
    findPattern(findTwoUnderscoresState, writeHState2, listOfStates, name + "____1", "__", "L", "R", "_")
    
    writeHState2.set3("_", outState, "R", "H")
	
    return outState
	
def prepLine(inState, listOfStates, name):
    # inState might have been called findLineNumber
    getToStartLineNumber = State(name + "_get_to_start_ln")
    markFirstLine = State(name + "_mark_first_line")
    getPastFunctionName = State(name + "_get_past_fn")
    writeH = State(name + "_write_H")
    getToLineNumber = State(name + "_get_to_ln")
    outState = State(name + "_out")
    
    listOfStates.extend([inState, getToStartLineNumber, markFirstLine, getPastFunctionName, 
        writeH, getToLineNumber])
    
    inState.set3("_", inState, "L", "_")
    inState.set3("1", getToStartLineNumber, "-", "1")
    inState.set3("E", getToStartLineNumber, "-", "E")
    
    findSymbolW(getToStartLineNumber, "_", "L", "R", "H", markFirstLine)
    
    findSymbolW(markFirstLine, "H", "R", "R", "_", getPastFunctionName)
    
    findSymbol(getPastFunctionName, "_", "R", "R", writeH)
        
    writeH.set3("_", getToLineNumber, "L", "H")
    
    findSymbol(getToLineNumber, "H", "L", "R", outState)

    return outState

def simpleTravelRight(inState, listOfStates, name, outState=None):
    
    if outState == None:
        outState = State(name + "_out")
    
    listOfStates.extend([inState])

    findSymbol(inState, "H", "R", "R", outState)
    
    return outState
    
def simpleTravelLeft(inState, listOfStates, name, lastMove="R", outState=None):
    
    foundHState = State(name + "_found_H")
    if outState == None:
        outState = State(name + "_out")    

    listOfStates.extend([inState])
        
    findSymbol(inState, "H", "L", lastMove, outState)
    
    return outState
    
# This function is very similar to the function markFunctionNames in writer.py,
# for obvious reasons.
def moveFunctionMarker(inState, listOfStates, name, outState=None):
    
    # inState might have been called getPastVariableNameState
    readSymbolReadState = State(name + "_read_symbol_read")
    checkForLineState = State(name + "_check_for_line")
    getPastLineNumberState = State(name + "_get_past_ln")
    checkForLineTypeState = State(name + "_check_for_line_type")
    checkForReactionState = State(name + "_check_for_reaction")
    getPastArgumentNameState = State(name + "_get_past_arg_name")
    checkForArgumentState = State(name + "_check_for_arg")
    returnToFailedFunctionState = State(name + "_return_failed_func")
    if outState == None:
        outState = State(name + "_out")

    listOfStates.extend([checkForReactionState, readSymbolReadState, checkForLineState, getPastLineNumberState, checkForLineTypeState, \
            inState, getPastArgumentNameState, checkForArgumentState, returnToFailedFunctionState])
    
    checkForReactionState.set3("_", checkForLineState, "R", "_")
    checkForReactionState.set3("1", readSymbolReadState, "R", "1")
    
    moveBy(readSymbolReadState, name + "_reading_basic_info", 3, "R", inState, listOfStates)
    # a goto looks like a variale name
    
    # This here's the whole point (the first one)! Getting that H in there.
    checkForLineState.set3("_", returnToFailedFunctionState, "L", "H")
    checkForLineState.set3("1", getPastLineNumberState, "R", "1")
    checkForLineState.set3("E", getPastLineNumberState, "R", "E")
	
    findSymbol(getPastLineNumberState, "_", "R", "R", checkForLineTypeState)
	
    checkForLineTypeState.set3("_", checkForReactionState, "R", "_")
    checkForLineTypeState.set3("1", inState, "-", "1")
    checkForLineTypeState.set3("E", getPastArgumentNameState, "-", "E")
	
    findSymbol(inState, "_", "R", "R", checkForReactionState)
	
    findSymbol(getPastArgumentNameState, "_", "R", "R", checkForArgumentState)
	
    checkForArgumentState.set3("_", checkForLineState, "R", "_")
    checkForArgumentState.set3("1", getPastArgumentNameState, "-", "1")
    checkForArgumentState.set3("E", getPastArgumentNameState, "-", "E")
    
    findSymbol(returnToFailedFunctionState, "H", "L", "-", outState)
    
    return outState
    
def moveLineMarker(inState, listOfStates, name, outState=None):
    # inState might have been called getPastLineNumberState
    
    checkForReactionState = State(name + "_check_for_reaction")
    readSymbolReadState = State(name + "_read_symbol_read")
    checkForLineTypeState = State(name + "_check_for_line_type")
    getPastVariableNameState = State(name + "_get_past_var_name")
    getPastArgumentNameState = State(name + "_get_past_arg_name")
    checkForArgumentState = State(name + "_check_for_arg")
    returnToFailedLineState = State(name + "_return_failed_line")
    if outState == None:
        outState = State(name + "_out")
    
    listOfStates.extend([inState, checkForReactionState, readSymbolReadState, checkForLineTypeState, 
        getPastVariableNameState, getPastArgumentNameState, checkForArgumentState, returnToFailedLineState])
    
    # This is the whole point!
    checkForReactionState.set3("_", returnToFailedLineState, "L", "H")
    checkForReactionState.set3("1", readSymbolReadState, "R", "1")
    
    moveBy(readSymbolReadState, name + "_reading_basic_info", 3, "R", getPastVariableNameState, 
        listOfStates)
    
    findSymbol(inState, "_", "R", "R", checkForLineTypeState)
    
    checkForLineTypeState.set3("_", checkForReactionState, "R", "_")
    checkForLineTypeState.set3("1", getPastVariableNameState, "-", "1")
    checkForLineTypeState.set3("E", getPastArgumentNameState, "-", "E")
    
    findSymbol(getPastVariableNameState, "_", "R", "R", checkForReactionState)
    
    findSymbol(getPastArgumentNameState, "_", "R", "R", checkForArgumentState)
    
    # This is the whole point!
    checkForArgumentState.set3("_", returnToFailedLineState, "L", "H")
    checkForArgumentState.set3("1", getPastArgumentNameState, "-", "1")
    checkForArgumentState.set3("E", getPastArgumentNameState, "-", "E")
    
    findSymbol(returnToFailedLineState, "H", "L", "-", outState)
    
    return outState
    
def rectifyNumber(inState, listOfStates, name, rectifySymbol, outState=None):
    # inState might have been called returnPrepState
    shiftSymbolState = State(name + "_shift_symbol")
    shift1State = State(name + "_shift_1")
    shiftEState = State(name + "_shift_E")
    if outState == None:
        outState = State(name + "_out")

    listOfStates.extend([inState, shiftSymbolState, shift1State, shiftEState])
	
    findSymbol(inState, "_", "L", "R", shiftSymbolState)	
	
    shiftSymbolState.set3("H", outState, "-", rectifySymbol)
    shiftSymbolState.set3("1", shift1State, "R", rectifySymbol)
    shiftSymbolState.set3("E", shiftEState, "R", rectifySymbol)
    
    shift1State.set3("H", outState, "-", "1")
    shift1State.set3("1", shift1State, "R", "1")
    shift1State.set3("E", shiftEState, "R", "1")
    
    shiftEState.set3("H", outState, "-", "E")
    shiftEState.set3("1", shift1State, "R", "E")
    shiftEState.set3("E", shiftEState, "R", "E")

    return outState

# for when you need to read this here symbol
def readHereSymbol(inState, listOfStates, name):
    # maps from symbol read to corresponding outState
    outStateDictionary = {"_": State(name + "_out__"), "1": State(name + "_out_1"),
        "E": State(name + "_out_E")}

    write1 = State(name + "_write_1")
    writeE = State(name + "_write_E")

    listOfStates.extend([inState, write1, writeE])
	
    # inState might have been called readSymbol
	
    inState.set3("1", write1, "L", "H")
    inState.set3("E", writeE, "L", "H")
    inState.set3("_", outStateDictionary["_"], "L", "_")
	
    write1.set3("H", outStateDictionary["1"], "R", "1")

    writeE.set3("H", outStateDictionary["E"], "R", "E")

    return outStateDictionary

def readThereSymbol(inState, listOfStates, name, symbol, outStateDictionary=None):
    
    if outStateDictionary == None:
        outStateDictionary = {"failure": State(name + "_out_fail"), "continue": State(name + "_out_continue"), 
            "success": State(name + "_out_success")}

    # inState might have been called readSymbol
    
    listOfStates.append(inState)

    if symbol == "_":
        inState.set3("_", outStateDictionary["success"], "L", "_")
        inState.set3("1", outStateDictionary["failure"], "-", "1")
        inState.set3("E", outStateDictionary["failure"], "-", "E")

    else:
        writeSymbolState = State(name + "_write_symbol")

        listOfStates.append(writeSymbolState)
        
        for symbolRead in ["_", "1", "E"]:
            if symbolRead == symbol:
                inState.set3(symbolRead, writeSymbolState, "L", "H")
            else:
                inState.set3(symbolRead, outStateDictionary["failure"], "-", symbolRead)
            
        writeSymbolState.set3("H", outStateDictionary["continue"], "-", symbol)
        
    return outStateDictionary
                
def findMatchingValue(inState, listOfStates, name, travelThere, travelBack, moveMarker):
    
    # Assumes we're already in position to read the next symbol                
    # inState might have been readFunctionSymbol
    
    readHereSymbolDict = readHereSymbol(inState, listOfStates, name + "_read_here")
    
    readUnderscore = rectifyNumber(readHereSymbolDict["_"], listOfStates, name + "_finished_here", "H")
    
    gotPastH1 = State(name + "_got_past_H_1")
    gotPastHE = State(name + "_got_past_H_E")

    listOfStates.extend([readHereSymbolDict["1"], readHereSymbolDict["E"]])

    readHereSymbolDict["1"].set3("H", gotPastH1, "R", "H")
    readHereSymbolDict["E"].set3("H", gotPastHE, "R", "H")

    checkForUnderscore = travelThere(readUnderscore, listOfStates, name + "_remember__")
    checkFor1 = travelThere(gotPastH1, listOfStates, name + "_remember_1")
    checkForE = travelThere(gotPastHE, listOfStates, name + "_remember_E")
    
    readThereSymbolDict = {"failure": State(name + "_out_fail"), "continue": State(name + "_out_continue"), 
        "success": State(name + "_out_success")}
    
    readThereSymbol(checkForUnderscore, listOfStates, name + "_check__", "_", readThereSymbolDict)
    readThereSymbol(checkFor1, listOfStates, name + "_check_1", "1", readThereSymbolDict)
    readThereSymbol(checkForE, listOfStates, name + "_check_E", "E", readThereSymbolDict)
    
    # if the symbol matches, and we haven't succeeded yet
    travelBack(readThereSymbolDict["continue"], listOfStates, name + "_continue", "R", inState)
    
    # if the symbol doesn't match, and we need to move onto the next possibility
    markerMoved = moveMarker(readThereSymbolDict["failure"], listOfStates, name + "_failure")
    
    doneFailing = rectifyNumber(markerMoved, listOfStates, name + "_remove_failed_H", "_")
    
    cameHomeInShame = travelBack(doneFailing, listOfStates, name + "_failed", "-")
    
    rectifyNumber(cameHomeInShame, listOfStates, name + "_reset_aux_on_failure", "H", inState)
    
    # if the symbol matches, and it was the last one, we have succeeded

    successRectified = rectifyNumber(readThereSymbolDict["success"], listOfStates, 
        name + "_goodnumber_rectify", "H")

    gotPastHSuccess = State(name + "_got_past_H_success")

    findSymbol(successRectified, "H", "L", "L", gotPastHSuccess)

    listOfStates.append(successRectified)

    cameHomeVictorious = travelBack(gotPastHSuccess, listOfStates, name + "_succeeded")
    
    outState = rectifyNumber(cameHomeVictorious, listOfStates, name + "_victorious_rectify", "_")
    
    return outState

def processCentrally(inState, listOfStates):
    inState = prepTopFunction(inState, listOfStates, "cpu_prep_top_func")
    inState = findMatchingValue(inState, listOfStates, "cpu_match_top_func", simpleTravelRight, \
        simpleTravelLeft, moveFunctionMarker)
    inState = prepLine(inState, listOfStates, "cpu_prep_line")
    inState = findMatchingValue(inState, listOfStates, "cpu_match_line", simpleTravelRight, \
        simpleTravelLeft, moveLineMarker)

    listOfStates.append(inState)
    inState.setAllNextStates(SimpleState("ACCEPT"))
    
    return inState
    


