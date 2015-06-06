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
		

def main():
	startHState = State("startH")
	startEState = State("startE")
	start_State = State("start_")
	writeHState = State("writeH")
	findNextSymbolState = State("findNextSymbol")
	readSymbolState = State("readSymbol")
	swap1State = State("swap1")
	swapEState = State("swapE")
	moveRight1State = State("moveRight1")
	moveRightEState = State("moveRightE")
	remember1State = State("remember1")
	rememberEState = State("rememberE")
	writeH2State = State("writeH2")
	eraseHState = State("eraseH")
	findNextNumberState = State("findNextNumber")
	incrNumberState = State("incrNumber")
	getToStartNumberState = State("getToStartNumber")
	getToEndNumberState = State("getToEndNumber")

	listOfStates = [startHState, startEState, start_State, writeHState, findNextSymbolState, readSymbolState, \
			swap1State, swapEState, moveRight1State, moveRightEState, remember1State, rememberEState, writeH2State, eraseHState, \
			findNextNumberState, incrNumberState, getToStartNumberState, getToEndNumberState]

	startHState.makeStartState()

	startHState.setNextState("_", startEState)
	startHState.setHeadMove("_", "R")
	startHState.setWrite("_", "H")


	startEState.setNextState("_", start_State)
	startEState.setHeadMove("_", "R")
	startEState.setWrite("_", "E")


	start_State.setNextState("_", writeHState)
	start_State.setHeadMove("_", "R")

#	write_State.setNextState("H", writeHState)
#	write_State.setHeadMove("H", "R")
#	write_State.setWrite("H", "_")


	writeHState.setNextState("_", findNextSymbolState)
	writeHState.setHeadMove("_", "L")
	writeHState.setWrite("_", "H")	


	findSymbol(findNextSymbolState, "H", "L", "R", readSymbolState)


	readSymbolState.setNextState("1", swap1State)
	readSymbolState.setNextState("E", swapEState)
	readSymbolState.setNextState("_", eraseHState)

	readSymbolState.setAllHeadMoves("L")
	
	readSymbolState.setAllWrites("H")
	readSymbolState.setWrite("_", "_")


	swap1State.setNextState("H", moveRight1State)
	swap1State.setHeadMove("H", "R")
	swap1State.setWrite("H", "1")

	
	swapEState.setNextState("H", moveRightEState)
	swapEState.setHeadMove("H", "R")
	swapEState.setWrite("H", "E")


	moveRight1State.set3("H", remember1State, "R", "H")


	moveRightEState.set3("H", rememberEState, "R", "H")


	findSymbolW(remember1State, "H", "R", "R", "1", writeH2State)


	findSymbolW(rememberEState, "H", "R", "R", "E", writeH2State)


	writeH2State.set3("_", findNextSymbolState, "L", "H")


	eraseHState.set3("H", findNextNumberState, "R", "_")


	findSymbolW(findNextNumberState, "H", "R", "L", "_", incrNumberState)
	
	
	incrNumberState.set3("1", incrNumberState, "L", "E")
	incrNumberState.set3("E", getToStartNumberState, "-", "1")
	incrNumberState.set3("_", getToStartNumberState, "-", "E")

	findSymbolW(getToStartNumberState, "_", "L", "-", "H", getToEndNumberState)
	
	findSymbolW(getToEndNumberState, "_", "R", "R", "_", writeHState)

	convertStatesToString(listOfStates, open("test_tm.txt", "w"))
	
if __name__ == "__main__":
	main()

