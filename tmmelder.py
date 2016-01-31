# This program melds together two Turing machines;
# that is, if the first machine ends up in an "OUT" state, 
# this program outputs a TM where the out state of the first machine
# is the start state of the second

import sys
from tmreader import convertStatesToString
import tmsim

def alphabetMSToTS():
    return ["a", "b"]

if __name__ == "__main__":
	inMachineName = sys.argv[1][:-4]
	outMachineName = sys.argv[2][:-4]
		
	try:
		assert inMachineName != outMachineName
	except:
		print "Error: cannot meld two machines that have the same name."
		raise
	
	inMachine = tmsim.SingleTapeTuringMachine(sys.argv[1], alphabetMSToTS())
	outMachine = tmsim.SingleTapeTuringMachine(sys.argv[2], alphabetMSToTS())
	
	for state in inMachine.listOfRealStates:
#		state.stateName = inMachineName + "_" + state.stateName
		
		for symbol in alphabetMSToTS():
			nextState = state.getNextState(symbol)
			if nextState.stateName == "OUT":
				state.setNextState(symbol, outMachine.startState)
		
	for state in outMachine.listOfRealStates:
#		state.stateName = outMachineName + "_" + state.stateName
		
		state.isStartState = False
		
	convertStatesToString(inMachine.listOfRealStates + outMachine.listOfRealStates, \
		open(sys.argv[3], "w"))