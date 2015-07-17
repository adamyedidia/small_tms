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
    
    moveBy(markFirstFunctionState, name + "_mark_first_fn", 2, "R", writeHState1)

    writeHState1.set3("_", goLeftState, "L", "H")
    
    getRidOfSeparatorState.set3("_", getRidOfSeparatorState, "L", "_")
    getRidOfSeparatorState.set3("1", findTwoUnderscoresState, "-", "1")
    getRidOfSeparatorState.set3("H", getRidOfSeparatorState, "-", "_")
    getRidOfSeparatorState.set3("E", findTwoUnderscoresState, "-", "E")
    
    findPattern(findTwoUnderScoresState, goRightState, listOfStates, name + "____1", "__", "L", "R", "_")
    
    moveBy(goRightState, "", 1, "R", writeHState2)
	
    writeHState2.set3("_", readFunctionSymbolState, "R", "H")
	
    return outState
	
def simpleTravelRight(inState, listOfStates, name, outState=None):
    
    if outState == None:
        outState = State(name + "_out")
    
    findSymbol(inState, "H", "R", "R", outState)
    
    return outState
    
def simpleTravelLeft(inState, listOfStates, name, outState=None):
    
    foundHState = State(name + "_found_H")
    if outState == None:
        outState = State(name + "_out")    
        
    findSymbol(inState, "H", "L", "L", foundHState)
    
    findSymbol(foundHState, "H", "L", "R", outState)
    
    return outState
    
# This function is very similar to the function markFunctionNames in writer.py,
# for obvious reasons.
def moveFunctionMarker(inState, listOfStates, name, outState=None):
    
    # inState might have been called checkForReactionState
    readSymbolReadState = State(name + "_read_symbol_read")
    checkForLineState = State(name + "_check_for_line")
    getPastLineNumberState = State(name + "_get_past_ln")
    checkForLineTypeState = State(name + "_check_for_line_type")
    getPastVariableNameState = State(name + "_get_past_var_name")
    getPastArgumentNameState = State(name + "_get_past_arg_name")
    checkForArgumentState = State(name + "_check_for_arg")
    returnToFailedFunctionState = State(name + "_return_failed_func")
    if outState == None:
        outState = State(name + "_out")
    
    inState.set3("_", checkForLineState, "R", "_")
    inState.set3("1", readSymbolReadState, "R", "1")
    
    moveBy(readSymbolReadState, name + "_reading_basic_info", 3, "R", getPastVariableNameState)
    # a goto looks like a variale name
    
    # This here's the whole point (the first one)! Getting that H in there.
    checkForLineState.set3("_", returnToFailedFunctionState, "L", "H")
    checkForLineState.set3("1", getPastLineNumberState, "R", "1")
    checkForLineState.set3("E", getPastLineNumberState, "R", "E")
	
    findSymbol(getPastLineNumberState, "_", "R", "R", checkForLineTypeState)
	
    checkForLineTypeState.set3("_", inState, "R", "_")
    checkForLineTypeState.set3("1", getPastVariableNameState, "-", "1")
    checkForLineTypeState.set3("E", getPastArgumentNameState, "-", "E")
	
    findSymbol(getPastVariableNameState, "_", "R", "R", inState)
	
    findSymbol(getPastArgumentNameState, "_", "R", "R", checkForArgumentState)
	
    checkForArgumentState.set3("_", checkForLineState, "R", "_")
    checkForArgumentState.set3("1", getPastArgumentNameState, "-", "1")
    checkForArgumentState.set3("E", getPastArgumentNameState, "-", "E")
    
    findSymbol(returnToFailedFunctionState, "H", "L", "-", outState)
    
    return outState
    
def rectifyNumber(inState, listOfStates, name, rectifySymbol, outState=None):
    # inState might have been called returnPrepState
    shiftSymbolState = State(name + "_shift_symbol")
    shift1State = State(name + "_shift_1")
    shiftEState = State(name + "_shift_E")
    if outState == None:
        outState = State(name + "_out")
	
    listOfStates.extend([inState, shiftSymbolState, shift1State, shiftEState])
	
    findSymbol(inState, "_", "L", "R", returnHState)	
	
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

def readHereSymbol(inState, listOfStates, name):
    # maps from symbol read to corresponding outState
    outStateDictionary = {"_": State(name + "_out__"), "1": State(name + "_out_1"),
        "E": State(name + "_out_E")}

    listOfStates.extend([instate, readSymbol, write1, writeE])
	
    # inState might have been called readSymbol
    write1 = State(name + "_write_1")
    writeE = State(name + "_write_E")
	
    inState.set3("1", write1, "L", "H")
    inState.set3("E", writeE, "L", "H")
    inState.set3("_", outStateDictionary["_"], "L", "_")
	
    write1.set3("H", outStateDictionary["1"], "-", "1")

    writeE.set3("H", outStateDictionary["E"], "-", "E")

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
    
    checkForUnderscore = travelThere(readUnderscore, listOfStates, name + "_remember__")
    checkFor1 = travelThere(readHereSymbolDict["1"], listOfStates, name + "_remember_1")
    checkForE = travelThere(readHereSymbolDict["E"], listOfStates, name + "_remember_E")
    
    readThereSymbolDict = {"failure": State(name + "_out_fail"), "continue": State(name + "_out_continue"), 
        "success": State(name + "_out_success")}
    
    readThereSymbol(checkForUnderscore, listOfStates, name + "_check__", "_", readThereSymbolDict)
    readThereSymbol(checkFor1, listOfStates, name + "_check_1", "1", readThereSymbolDict)
    readThereSymbol(checkForE, listOfStates, name + "_check_E", "E", readThereSymbolDict)
    
    # if the symbol matches, and we haven't succeeded yet
    travelBack(readThereSymbolDict["continue"], listOfStates, name + "_continue", inState)
    
    # if the symbol doesn't match, and we need to move onto the next possibility
    markerMoved = moveMarker(readThereSymbolDict["failure"], listOfStates, name + "_failure")
    
    doneFailing = rectifyNumber(markerMoved, listOfStates, name + "_remove_failed_H", "_")
    
    cameHomeInShame = travelBack(doneFailing, listOfStates, name + "_failed")
    
    rectifyNumber(cameHomeInShame, listOfStates, name + "_reset_aux_on_failure", "H", inState)
    
    # if the symbol matches, and it was the last one, we have succeeded
    cameHomeVictorious = travelBack(readThereSymbolDict["success"], listOfStates, name + "_succeeded")
    
    outState = rectifyNumber(cameHomeVictorious, listOfStates, name + "_victorious_rectify", "_")
    
    return outState

def processCentrally(inState, listOfStates):
    inState = prepTopFunction(inState, listOfStates, "cpu_prep_top_func")
    inState = findMatchingValue(inState, listOfStates, "cpu_match_top_func", simpleTravelRight, \
        simpleTravelLeft, moveFunctionMarker)
        
    inState.setAllNextStates(SimpleState("ACCEPT"))
    
    return inState
    

def getToTopFunction(inState, listOfStates):
    # inState might have been called findStackState
    
    name = "cpu_get_to_fn"
    
    markFirstFunctionState = State(name + "_mark_first_fn")
    writeHState1 = State(name + "_write_H_1")
    getRidOfSeparatorState = State(name + "_no_separator")
    findTwoUnderScoresState = State(name + "_find_2_underscores")
    writeHState2 = State(name + "_write_H_2")
    readFunctionSymbolState = State(name + "_read_fn_symbol")
    returnPrepState = State(name + "_return_prep")
    returnHState = State(name + "_return_H")
    shift1State = State(name + "_shift_1")
    shiftEState = State(name + "_shift_E")
    write1State1 = State(name + "_write_1_1")
    writeEState1 = State(name + "_write_E_1")
    remember1State1 = State(name + "_remember_1_1")
    rememberEState1 = State(name + "_remember_E_1")
    remember_State = State(name + "_remember__")
    remember1State2 = State(name + "_remember_1_2")
    rememberEState2 = State(name + "_remember_E_2")
    checkIf_State = State(name + "_check_if__")
    checkIf1State = State(name + "_check_if_1")
    checkIfEState = State(name + "_check_if_E")
    write1State2 = State(name + "_write_1_2")
    writeEState2 = State(name + "_write_E_2")
    continueState = State(name + "_continue")
    getPastFunctionNameState = State(name + "_get_past_fn_name")
    checkForLineState = State(name + "_check_for_line")
    getPastLineNumberState = State(name + "_get_past_ln")
    checkForLineTypeState = State(name + "_check_line_type")
    checkForReactionState = State(name + "_check_for_reaction")
    readSymbolReadState = State(name + "_read_read")
    readSymbolWrittenState = State(name + "_read_write")
    readHeadMoveState = State(name + "_read_head_move")
    getPastVariableNameState = State(name + "_get_past_var_name")
    getPastArgumentNameState = State(name + "_get_past_arg_name")
    checkForArgumentState = State(name + "_check_for_arg")
    getBackToFailedFunctionState = State(name + "_get_back_failed_fn")
    failurePrepState = State(name + "_failure_prep")
    failure_State = State(name + "_failure__")
    failure1State = State(name + "_failure_1")
    failureEState = State(name + "_failure_E")
    getBackToAuxState = State(name + "_get_back_aux")
    auxPrepState = State(name + "_aux_prep")
    auxHState = State(name + "_aux_H")
    aux1State = State(name + "_aux_1")
    auxEState = State(name + "_aux_E")
    getBackToHState = State(name + "_get_back_to_H")
    markFirstLineState = State(name + "_mark_first_line")
    getBackToGoodFunctionState = State(name + "_get_back_to_good_fn")
    getToStartGoodFunctionState = State(name + "_get_to_start_good_fn")
    goodFunc_State = State(name + "_good_func__")
    goodFunc1State = State(name + "_good_func_1")
    goodFuncEState = State(name + "_good_func_E")
    returnHomeVictoriousState = State(name + "_return_home_victorious")
    findLineNumberState = State(name + "_find_ln")
    getToStartLineNumberState = State(name + "_get_to_start_ln")
    outState = State(name + "_out")
    
    listOfStates.extend([inState, markFirstFunctionState, writeHState1, getRidOfSeparatorState, findTwoUnderScoresState,
            writeHState2, readFunctionSymbolState, returnPrepState, returnHState, shift1State, shiftEState,
            write1State1, writeEState1, remember1State1, rememberEState1, remember_State, remember1State2,
            rememberEState2, checkIf_State, checkIf1State, checkIfEState, write1State2, writeEState2, 
            continueState, getPastFunctionNameState, checkForLineState, getPastLineNumberState,
            checkForLineTypeState, checkForReactionState, readSymbolReadState, readSymbolWrittenState, 
            readHeadMoveState, getPastVariableNameState, getPastArgumentNameState, checkForArgumentState, 
            getBackToFailedFunctionState, failurePrepState, failure_State, failure1State, failureEState,
            getBackToAuxState, auxPrepState, auxHState, aux1State, auxEState, getBackToHState, markFirstLineState,
            getBackToGoodFunctionState, getToStartGoodFunctionState, goodFunc_State, goodFunc1State, 
            goodFuncEState, returnHomeVictoriousState, findLineNumberState, getToStartLineNumberState])
    
    
    findPattern(inState, markFirstFunctionState, listOfStates, name + "_mark_first_fn", "HH", "L", "R", "H")
    
    moveBy(markFirstFunctionState, name + "_mark_first_fn", 2, "R", writeHState)

    writeHState1.set3("_", goLeftState, "L", "H")
    
    getRidOfSeparatorState.set3("_", getRidOfSeparatorState, "L", "_")
    getRidOfSeparatorState.set3("1", findTwoUnderscoresState, "-", "1")
    getRidOfSeparatorState.set3("H", getRidOfSeparatorState, "-", "_")
    getRidOfSeparatorState.set3("E", findTwoUnderscoresState, "-", "E")
    
    findPattern(findTwoUnderScoresState, goRightState, listOfStates, name + "____1", "__", "L", "R", "_")
    
    writeHState2.set3("_", readFunctionSymbolState, "R", "H")
    
    readFunctionSymbolState.set3("_", returnPrepState, "L", "_")
    readFunctionSymbolState.set3("1", write1State1, "L", "H")
    readFunctionSymbolState.set3("E", writeEState1, "L", "H")
    
    findSymbol(returnPrepState, "_", "L", "R", returnHState)
    
    returnHState.set3("1", shift1State, "R", "H")
    returnHState.set3("E", shiftEState, "R", "H")
    
    shift1State.set3("_", remember_State, "-", "_")
    shift1State.set3("1", shift1State, "R", "1")
    shift1State.set3("E", shiftEState, "R", "1")
    
    shiftEState.set3("_", remember_State, "-", "_")
    shiftEState.set3("1", shift1State, "R", "E")
    shiftEState.set3("E", shiftEState, "R", "E")
    
    write1State1.set3("H", remember1State1, "R", "1")
    
    writeEState1.set3("H", rememberEState1, "R", "E")
    
    remember1State1.set3("H", remember1State2, "R", "H")

    rememberEState1.set3("H", rememberEState2, "R", "H")
    
    findSymbol(remember_State, "H", "R", "R", checkIf_State)
    
    findSymbol(remember1State2, "H", "R", "R", checkIf1State)
    
    findSymbol(rememberEState2, "H", "R", "R", checkIfEState)
    
    # On either success or failure, we have to move the H back to the beginning
    checkIf_State.set3("_", markFirstLineState, "R", "_")
    checkIf_State.set3("1", getPastFunctionNameState, "-", "1")
    checkIf_State.set3("E", getPastFunctionNameState, "-", "E")
    
    checkIf1State.set3("_", checkForLineState, "R", "_")
    checkIf1State.set3("1", write1State2, "L", "H")
    checkIf1State.set3("E", getPastFunctionNameState, "-", "E")
    
    checkIfEState.set3("_", checkForLineState, "R", "_")
    checkIfEState.set3("1", getPastFunctionNameState, "-", "1")
    checkIfEState.set3("E", writeEState2, "L", "H")
    
    write1State2.set3("H", continueState, "-", "1")
    
    writeEState2.set3("H", continueState, "-", "E")
    
    findSymbol(continueState, "H", "L", "R", readFunctionSymbolState)
    
    findSymbol(getPastFunctionNameState, "_", "R", "R", checkForLineState) 
    
    # This line's the point!
    checkForLineState.set3("_", getBackToFailedFunctionState, "L", "H")
    checkForLineState.set3("1", getPastLineNumberState, "-", "1")
    checkForLineState.set3("E", getPastLineNumberState, "-", "E")
    
    findSymbol(getPastLineNumberState, "_", "R", "R", checkForLineTypeState)
    
    checkForLineTypeState.set3("_", checkForReactionState, "R", "_")
    checkForLineTypeState.set3("1", getPastVariableNameState, "-", "1")
    checkForLineTypeState.set3("E", getPastArgumentNameState, "-", "E")
    
    checkForReactionState.set3("_", checkForLineState, "R", "_")
    checkForReactionState.set3("1", readSymbolReadState, "R", "1")
    
    moveBy(readSymbolReadState, "", 1, "R", readSymbolWrittenState)
    
    moveBy(readSymbolWrittenState, "", 1, "R", readHeadMoveState)
    
    moveBy(readHeadMoveState, "", 1, "R", getPastVariableNameState) # a goto looks like a variable name
            
    findSymbol(getPastVariableNameState, "_", "R", "R", checkForReactionState)
    
    findSymbol(getPastArgumentNameState, "_", "R", "R", checkForArgumentState)
    
    checkForArgumentState.set3("_", checkForLineState, "R", "_")
    checkForArgumentState.set3("1", getPastArgumentNameState, "-", "1")
    checkForArgumentState.set3("E", getPastArgumentNameState, "-", "E")
    
    findSymbol(getBackToFailedFunctionState, "H", "L", "-", failurePrepState)
    
    findSymbol(failurePrepState, "_", "L", "R", failureHState)
    
    # Okay, so we failed. We need to get rid of the head on the function we were
    # were looking at, and reset the head on the model of the function we're looking for.
    
    # another shifter
    failure_State.set3("1", failure1State, "R", "_")
    failure_State.set3("H", getBackToAuxState, "-", "_")
    failure_State.set3("E", failureEState, "R", "_")
    
    failure1State.set3("1", failure1State, "R", "1")
    failure1State.set3("H", getBackToAuxState, "-", "1")
    failure1State.set3("E", failureEState, "R", "1")
    
    failureEState.set3("1", failure1State, "R", "E")
    failureEState.set3("H", getBackToAuxState, "-", "E")
    failureEState.set3("E", failureEState, "R", "E")
    
    # Now we need to reset the Aux head
    findSymbol(getBackToAuxState, "H", "L", "-", auxPrepState)
    
    findSymbol(auxPrepState, "_", "L", "R", auxHState)
    
    # yet another shifter
    auxHState.set3("1", aux1State, "R", "H")
    auxHState.set3("H", readFunctionSymbolState, "R", "H")
    auxHState.set3("E", auxEState, "R", "H")
    
    aux1State.set3("1", aux1State, "R", "1")
    aux1State.set3("H", getBackToHState, "-", "1")
    aux1State.set3("E", auxEState, "R", "1")
    
    auxEState.set3("1", aux1State, "R", "E")
    auxEState.set3("H", getBackToHState, "-", "E")
    auxEState.set3("E", auxEState, "R", "E")
    
    findSymbol(getBackToHState, "H", "L", "R", readFunctionSymbolState)
    
    # Okay, we succeeded. Time to reset the function we like and mark the line that comes after it
    
    markFirstLineState.set3("_", getBackToGoodFunctionState, "L", "H")
    
    getBackToGoodFunctionState.set3("_", getToStartGoodFunctionState, "L", "_")
    
    findSymbol(getToStartGoodFunctionState, "_", "L", "R", goodFunc_State)
    
    # Yet ANOTHER shifter
    goodFunc_State.set3("1", goodFunc1State, "R", "_")
    goodFunc_State.set3("E", goodFuncEState, "R", "E")
    
    goodFunc1State.set3("1", goodFunc1State, "R", "1")
    goodFunc1State.set3("H", returnHomeVictoriousState, "L", "1")
    goodFunc1State.set3("E", goodFuncEState, "R", "1")
    
    goodFuncEState.set3("1", goodFunc1State, "R", "E")
    goodFuncEState.set3("H", returnHomeVictoriousState, "L", "E")
    goodFuncEState.set3("E", goodFuncEState, "R", "E")
    
    findSymbolW(returnHomeVictoriousState, "H", "L", "-", "_", findLineNumberState)
    
    findLineNumberState.set3("_", findLineNumberState, "L", "_")
    findLineNumberState.set3("1", getToStartLineNumberState, "-", "1")
    findLineNumberState.set3("E", getToStartLineNumberState, "-", "E")
    
    findSymbolW(getToStartLineNumberState, "_", "L", "R", "H", outState)
    
    return outState
