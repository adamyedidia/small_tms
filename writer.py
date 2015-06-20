import sys
import string
import math
from state import *
from stateTemplates import *

def convertStatesToString(listOfStates, output):

	numberOfStates = len(listOfStates)
	
	output.write("States: " + str(numberOfStates) + "\n")
	output.write("\n")
	
	statesIveAlreadyPrinted = {}

	for state in listOfStates:
#		print state.stateName
		
		try:
			assert (not state.stateName in statesIveAlreadyPrinted)
		except:
			print "duplicated state:", state.stateName
			raise		

		statesIveAlreadyPrinted[state.stateName] = None
		
		if state.isStartState:
			output.write("START ")
		
		output.write(state.stateName + ":\n")
		
		for symbol in ["_", "1", "H", "E"]:			
			output.write("\t" + symbol + " -> " + state.getNextStateName(symbol) + "; " + \
				state.getHeadMove(symbol) + "; " + state.getWrite(symbol) + "\n")
		
		output.write("\n")
        
def getFunctionLabelDictionary(functions, path):

	functionLabelDictionary = {}
	functionDictionary = {}

	functionCounter = 1

	for function in functions:

		functionLabelDictionary[function] = {}		
		functionDictionary[function] = functionCounter
 
		functionLines = open(path + string.strip(function) + ".tfn", "r")

		lineCounter = 1
		
		for line in functionLines:
			if ":" in line:
				label = string.split(line, ":")[0]
				functionLabelDictionary[function][label] = lineCounter

			lineCounter += 1

		functionCounter += 1
        
	return functionLabelDictionary, functionDictionary
    
def getFunctionVariableDictionary(functions, path):
    functionVariableDictionary = {}
    
    for function in functions:
        
        functionVariableDictionary[function] = {}
        
        functionLines = open(path + string.strip(function) + ".tfn", "r").readlines()
        
        firstLine = functionLines[0]
        
        for i, variableName in enumerate(string.split(firstLine)[1:]):
            functionVariableDictionary[function][variableName] = i+1
            
    return functionVariableDictionary

def convertNumberToBarCode(number, setOfSymbols = ["E", "1"]):

	barCode = ""	
	newBarCode = ""
	barCodeIndexCounter = -1

	overallCounter = 0
	
	incrementing = True

	while overallCounter < number:
		if incrementing:
			if barCodeIndexCounter == -1:
				newBarCode = setOfSymbols[0] + newBarCode
				barCodeIndexCounter = len(newBarCode) - 1
				overallCounter += 1
				barCode = newBarCode
				newBarCode = ""
				incrementing = True	

			else:
				indexOfSymbol = setOfSymbols.index(barCode[barCodeIndexCounter])

				if indexOfSymbol == len(setOfSymbols) - 1:
					newBarCode = setOfSymbols[0] + newBarCode
					barCodeIndexCounter -= 1

				else:
					newBarCode = setOfSymbols[indexOfSymbol + 1] + newBarCode
					barCodeIndexCounter -= 1
					incrementing = False

		else:
			if barCodeIndexCounter == -1:
				overallCounter += 1
				barCode = newBarCode
				barCodeIndexCounter = len(barCode) - 1
				newBarCode = ""
				incrementing = True

			else:
				newBarCode = barCode[barCodeIndexCounter] + newBarCode
				barCodeIndexCounter -= 1

	return barCode

def writeFunctionGuts(functionName, functionLines, labelDictionary):
	for line in functionLines:
		pass

# This writes a counter onto the tape, which will count down from x, where x is the number of variables.

def writeCounter(listOfStates, inState, x):
	assert x > 0

	barCode = convertNumberToBarCode(x)
	listOfCounterWritingStates = [inState]

	writeHState = State("write_var_counter_H")
	
	listOfStates.append(inState)
	listOfStates.append(writeHState)

	for i in range(1, len(barCode)):
		newState = State("write__var_counter_" + str(i))
		listOfCounterWritingStates.append(newState)
		listOfStates.append(newState)

	outState = State("write_var_counter_out")
	
	listOfCounterWritingStates.append(writeHState)

	writeHState.set3("_", outState, "R", "H")
	
	for i, state in enumerate(listOfCounterWritingStates[:-1]):
		state.set3("_", listOfCounterWritingStates[i+1], "R", barCode[i])

	return outState

def writeEachVariableValue(listOfStates, inState, initValueString, numberOfVariables):

	# inState might have been called write_State1
	write_State2 = State("write_var_value_underscore_2")
	writeNameState = State("write_var_value_name")
	write_State3 = State("write_var_value_underscore_3")
	write_State4 = State("write_var_value_underscore_4")
	write_State5 = State("write_var_value_underscore_5")
	write_State6 = State("write_var_value_underscore_6")
	findHState1 = State("write_var_value_find_H_1")
	decrementCounterState = State("write_var_value_decrement_counter")
	delete1State = State("write_var_value_delete_1")
	findHState2 = State("write_var_value_find_H_2")
	findHState3 = State("write_var_value_find_H_3")
	outState = State("write_var_value_out")

	listOfStates.extend([inState, write_State2, writeNameState, write_State3, write_State4, write_State5, write_State6, \
		findHState1, decrementCounterState, delete1State, findHState2, findHState3])

	listOfInitValueStates = []

	for i in range(len(initValueString)):
		listOfInitValueStates.append(State("write_var_value_initvalue_" + str(i)))
			
	inState.set3("_", write_State2, "R", "_")

	listOfNameSpaceStates = []
	for i in range(int(math.log(numberOfVariables, 2))):
		listOfNameSpaceStates.append(State("write_var_value_name_space_" + str(i)))
	listOfNameSpaceStates.append(writeNameState)

	write_State2.set3("_", listOfNameSpaceStates[0], "R", "_")

	for i, state in enumerate(listOfNameSpaceStates[:-1]):
		state.set3("_", listOfNameSpaceStates[i+1], "R", "_")
		listOfStates.append(state)

	writeNameState.set3("_", write_State3, "R", "E")
	write_State3.set3("_", write_State4, "R", "_")
	write_State4.set3("_", write_State5, "R", "_")
	write_State5.set3("_", write_State6, "R", "_")
	write_State6.set3("_", listOfInitValueStates[0], "R", "_")

	for i, state in enumerate(listOfInitValueStates[:-1]):
		state.set3("_", listOfInitValueStates[i+1], "R", initValueString[i])

	listOfStates.extend(listOfInitValueStates)

	listOfInitValueStates[-1].set3("_", findHState1, "L", "H")

	findSymbol(findHState1, "H", "L", "L", decrementCounterState)
	
	decrementCounterState.set3("E", decrementCounterState, "L", "1")
	decrementCounterState.set3("1", findHState2, "-", "E")
	decrementCounterState.set3("_", delete1State, "R", "_")
	
	delete1State.set3("1", findHState2, "-", "_")
	delete1State.set3("H", outState, "R", "H")

	findSymbol(findHState2, "H", "R", "R", findHState3)
	findSymbolW(findHState3, "H", "R", "R", "_", inState) 	

	return outState

def incrementEachIdentifier(listOfStates, inState):

	markState = State("write_var_incr_mark")
	findFinState = State("write_var_incr_find_fin")
	getPastValueLeftState = State("write_var_incr_get_past_value_left")
	findIdentifierState = State("write_var_incr_find_id")
	incrementIdentifierState = State("write_var_incr_id")
	find_State = State("write_var_incr_find_underscore")
	findValueLeftState = State("write_var_incr_find_value_left")
	findValueRightState = State("write_var_incr_find_value_right")
	getPastValueRightState = State("write_var_incr_get_past_value_right")
#	outState = SimpleState("ACCEPT")
	outState = State("write_var_incr_out")

	listOfStates.extend([inState, markState, findFinState, getPastValueLeftState, findIdentifierState, incrementIdentifierState, \
		find_State, findValueLeftState, findValueRightState, getPastValueRightState])

	# inState might have been called findNot_State
	inState.set3("_", inState, "R", "_")
	inState.set3("1", markState, "-", "1")
	inState.set3("E", markState, "-", "E")

	findSymbolW(markState, "_", "R", "R", "H", findFinState)
	
	findSymbol(findFinState, "H", "R", "L", getPastValueLeftState)
	
	findSymbol(getPastValueLeftState, "_", "L", "-", findIdentifierState)
	
	findIdentifierState.set3("_", findIdentifierState, "L", "_")
	findIdentifierState.set3("1", incrementIdentifierState, "-", "1")
	findIdentifierState.set3("E", incrementIdentifierState, "-", "E")
	findIdentifierState.set3("H", findValueRightState, "-", "_")

	incrementIdentifierState.set3("_", findValueLeftState, "L", "E")
	incrementIdentifierState.set3("1", incrementIdentifierState, "L", "E")
	incrementIdentifierState.set3("E", find_State, "-", "1")

	findSymbol(find_State, "_", "L", "-", findValueLeftState)

	findValueLeftState.set3("_", findValueLeftState, "L", "_")
	findValueLeftState.set3("1", getPastValueLeftState, "-", "1")
	findValueLeftState.set3("E", getPastValueLeftState, "-", "E")

	findValueRightState.set3("_", findValueRightState, "R", "_")
	findValueRightState.set3("1", getPastValueRightState, "-", "1")
	findValueRightState.set3("E", getPastValueRightState, "-", "E")
	
	getPastValueRightState.set3("_", inState, "-", "_")
	getPastValueRightState.set3("1", getPastValueRightState, "R", "1")
	getPastValueRightState.set3("E", getPastValueRightState, "R", "E")
	getPastValueRightState.set3("H", outState, "R", "_")

	return outState

# Puts heads in front of all the values, and puts the HH symbol to signal end of variable values
def putHeadsEverywhere(listOfStates, inState):

	# inState might have been called write_State
	writeHState = State("write_var_heads_write_H")
	findValueState = State("write_var_heads_find_value")
	getPastValueState = State("write_var_heads_get_past_value")
	findIdentifierState = State("write_var_heads_find_id")
	getPastIdentifierState = State("write_var_heads_get_past_id")
	getToFinState = State("write_var_heads_get_to_fin")
	outState = State("write_var_heads_out")
#	outState = SimpleState("ACCEPT")

	listOfStates.extend([inState, writeHState, findValueState, getPastValueState, findIdentifierState, getPastIdentifierState, getToFinState])

	inState.set3("_", writeHState, "R", "_")

	writeHState.set3("_", findValueState, "L", "H")
	
	findValueState.set3("_", findValueState, "L", "_")
	findValueState.set3("1", getPastValueState, "-", "1")
	findValueState.set3("E", getPastValueState, "-", "E")
	findValueState.set3("H", getToFinState, "R", "H")

	findSymbolW(getPastValueState, "_", "L", "L", "H", findIdentifierState)

	findIdentifierState.set3("_", findIdentifierState, "L", "_")
	findIdentifierState.set3("1", getPastIdentifierState, "-", "1")
	findIdentifierState.set3("E", getPastIdentifierState, "-", "E")
	
	findSymbol(getPastIdentifierState, "_", "L", "-", findValueState)

	findPattern(getToFinState, outState, listOfStates, "write_var_heads", "H_", "R", "R", "H")

	return outState

def writeVariableValuesSkeleton(listOfStates, inState, numberOfVariables, initValueString):
	inState = writeCounter(listOfStates, inState, numberOfVariables)
	inState = writeEachVariableValue(listOfStates, inState, initValueString, numberOfVariables)
	inState = incrementEachIdentifier(listOfStates, inState)
	inState = putHeadsEverywhere(listOfStates, inState)
	return inState
	
def writeAuxValues(listOfStates, inState, numberOfVariables, numberOfFunctions):
	# Write "Keep head in place, write _, line 1, function 1"

	# inState might have been called write_State1
	write_State2 = State("write_aux_underscore_2")
	write_State3 = State("write_aux_underscore_3")
	writeEState1 = State("write_aux_E_1")
	write_State4 = State("write_aux_underscore_4")
	writeEState2 = State("write_aux_E_2")
	outState = State("write_aux_out")
#	outState = SimpleState("ACCEPT")	

	listOfStates.extend([inState, write_State2, write_State3, writeEState1, write_State4, writeEState2])

	inState.set3("_", write_State2, "R", "_")
	write_State2.set3("_", write_State3, "R", "_")

	listOfLineNumberSpaceStates = []
	for i in range(int(math.log(numberOfVariables, 2))):
		listOfLineNumberSpaceStates.append(State("write_aux_line_number_space_" + str(i)))
	listOfLineNumberSpaceStates.append(writeEState1)

	write_State3.set3("_", listOfLineNumberSpaceStates[0], "R", "_")

	for i, state in enumerate(listOfLineNumberSpaceStates[:-1]):
		state.set3("_", listOfLineNumberSpaceStates[i+1], "R", "_")
		listOfStates.append(state)

	writeEState1.set3("_", write_State4, "R", "E")

	listOfFunctionNameSpaceStates = []
	for i in range(int(math.log(numberOfFunctions, 2))):
		listOfFunctionNameSpaceStates.append(State("write_aux_function_name_space_" + str(i)))
	listOfFunctionNameSpaceStates.append(writeEState2)
	
	write_State4.set3("_", listOfFunctionNameSpaceStates[0], "R", "_")

	for i, state in enumerate(listOfFunctionNameSpaceStates[:-1]):
		state.set3("_", listOfFunctionNameSpaceStates[i+1], "R", "_")
		listOfStates.append(state)
	
	writeEState2.set3("_", outState, "R", "E")

	return outState

def writeProgram(listOfStates, inState, functions, functionVariableDictionary, \
	functionLabelDictionary, functionDictionary, path):

    inState = writeProgramSkeleton(listOfStates, inState, functions, functionVariableDictionary, \
		functionLabelDictionary, functionDictionary, path)
    
    return inState
    
def writeProgramSkeleton(listOfStates, inState, functions, functionVariableDictionary, \
	functionLabelDictionary, functionDictionary, path):
    
	listOfFunctionGroups = []
	characteristicString = ""
	    		
	for i, function in enumerate(functions):
		functionName = function
		functionLines = open(path + functionName + ".tfn", "r").readlines()
		if i == 0:
			functionGroup = FunctionGroup(functionName, functionLines, functionVariableDictionary, \
				functionLabelDictionary, functionDictionary, convertNumberToBarCode, \
				listOfStates, inState)
		else:
			functionGroup = FunctionGroup(functionName, functionLines, functionVariableDictionary, \
				functionLabelDictionary, functionDictionary, convertNumberToBarCode, \
				listOfStates)			
		listOfFunctionGroups.append(functionGroup)
		characteristicString += functionGroup.charString
        
	for i, functionGroup in enumerate(listOfFunctionGroups[:-1]):
		functionGroup.attach(listOfFunctionGroups[i+1])
		
	outState = SimpleState("ACCEPT")
# Change this

	listOfFunctionGroups[-1].outState.setNextState("_", outState)
    
	return outState

def main():

################################################################

### Setting up the functionLabelDictionary

	
	path = sys.argv[1]

	try:
		functions = [string.strip(x) for x in open(path + "functions.tff", "r").readlines()]
	except:  
		raise Exception("No functions.tff file found in directory " + path) 

	functionLabelDictionary, functionDictionary = getFunctionLabelDictionary(functions, path)
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

	numberOfVariables = 4
	numberOfFunctions = 2

	inState = writeVariableValuesSkeleton(listOfStates, inState, numberOfVariables, initValueString)	
	inState = writeAuxValues(listOfStates, inState, numberOfVariables, numberOfFunctions)
	inState = writeProgram(listOfStates, inState, functions, functionVariableDictionary,
		functionLabelDictionary, functionDictionary, path)

	convertStatesToString(listOfStates, open("test_tm.txt", "w"))



################################################################

### Organizing the states that write the program code

#	writeVariableValuesSkeleton()


#	branchState = State("write_main_title_branch")

#	writeMainTitle1 = State("write_main_title_1")
#	writeMainTitle2 = State("write_main_title_2")
#	writeMainTitle3 = State("write_main_title_3")
#	writeMainTitle4 = State("write_main_title_4")

#	writeMainTitle1.makeStartState()
#	writeMainTitle1.set3("_", writeMainTitle2, "R", "H")
#	writeMainTitle2.set3("_", writeMainTitle3, "R", "H")
#	writeMainTitle3.set3("_", writeMainTitle4, "R", "_")
#	writeMainTitle4.set3("_", branchState, "R", "1")



#	for function in functions:
#		branchState.setNextState
		
		


if __name__ == "__main__":
	main()

