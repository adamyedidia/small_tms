import sys
import string
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

	writeHState = State("write_counter_H")
	
	listOfStates.append(inState)
	listOfStates.append(writeHState)

	for i in range(1, len(barCode)):
		newState = State("write_counter_" + str(i))
		listOfCounterWritingStates.append(newState)
		listOfStates.append(newState)

	outState = State("write_counter_out")
	
	listOfCounterWritingStates.append(writeHState)

	writeHState.set3("_", outState, "R", "H")
	
	for i, state in enumerate(listOfCounterWritingStates[:-1]):
		state.set3("_", listOfCounterWritingStates[i+1], "R", barCode[i])

	return outState

def writeEachVariableValue(listOfStates, inState, initValueString):

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
	outState = SimpleState("ACCEPT") #Change this!!

	listOfStates.extend([inState, write_State2, writeNameState, write_State3, write_State4, write_State5, write_State6, \
		findHState1, decrementCounterState, delete1State, findHState2, findHState3])

	listOfInitValueStates = []

	for i in range(len(initValueString)):
		listOfInitValueStates.append(State("write_var_value_initvalue_" + str(i)))
			
	inState.set3("_", write_State2, "R", "_")
	write_State2.set3("_", writeNameState, "R", "_")
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
	delete1State.set3("H", outState, "-", "_")

	findSymbol(findHState2, "H", "R", "R", findHState3)
	findSymbolW(findHState3, "H", "R", "R", "_", inState) 	

	return outState

def writeVariableValuesSkeleton(listOfStates, inState, numberOfVariables, initValueString):
	inState = writeCounter(listOfStates, inState, numberOfVariables)
	inState = writeEachVariableValue(listOfStates, inState, initValueString)
	return inState
	

def main():

################################################################

### Setting up the functionLabelDictionary

	functionLabelDictionary = {}
	functionDictionary = {}
	
	path = sys.argv[1]

	try:
		functions = open(path + "functions.tff", "r").readlines()
	except:  
		raise Exception("No functions.tff file found in directory " + path) 

	functionCounter = 0

	for function in functions:

		functionLabelDictionary[function] = {}		
		functionDictionary[function] = functionCounter
 
		functionLines = open(function[:-1] + ".tfn", "r")

		lineCounter = 0
		
		for line in functionLines:
			if ":" in line:
				label = string.split(line, ":")[0]
				functionLabelDictionary[function][label] = lineCounter

			lineCounter += 1

		functionCounter += 1

###################################################################

	try:
		initValueString = string.strip(open(path + "initvar", "r").read()) + "H"
	except:
		raise Exception("No initvar file found in directory " + path)

###################################################################

	inState = State("start")
	inState.makeStartState()

	listOfStates = []

	writeVariableValuesSkeleton(listOfStates, inState, 4, initValueString)	

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

