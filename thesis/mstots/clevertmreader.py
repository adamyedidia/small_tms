def getListOfAllABCombosOld(comboSize):
	if comboSize == 0:
		return [""]

	else:
		returnList = []
		for item in getListOfAllABCombos(comboSize - 1):
			for symbol in alphabetMSToTS():
				returnList.append(item + symbol)

		return returnList


def alphabetMTToST():
    return ["_", "1", "H", "E"]

def alphabetMSToTS():
    return ["a", "b"]

def alphabetMSToTS():
    return ["a", "b"]
	
def getSymbolMapping():
	symbolMapping = {}
	reverseSymbolMapping = {}
	
	alphabetSize = len(alphabetMTToST())

	listOfAllABCombos = getListOfAllABCombos(alphabetSize)

	for i, symbol in enumerate(alphabetMTToST()):	
		symbolMapping[symbol] = listOfAllABCombos[i]
		reverseSymbolMapping[listOfAllABCombos[i]] = symbol

	return symbolMapping, reverseSymbolMapping

# Takes as input a dictionary such as {0: "a"} to indicate that the 0th symbol must be "a"
def mapFromMiniSymbolsSeenToLargerSymbols(seenSymbolDict):
	returnList = symbolMapping.keys()
	
	for abString in reverseSymbolMapping:
		for index in seenSymbolDict:
			if abString[index] != seenSymbolDict[index]:
				# remove the contradictory symbol
				returnList.remove(reverseSymbolMapping[abString])

	return returnList

def drawConclusions(seenSymbolDict):
	for listOfSymbols
	

if __name__ == "__main__":
	sttm = SingleTapeTuringMachine(sys.argv[1])

	listOfStates = []

	coreStateDictionary = {}

	outerStartState = sttm.startState

	symbolMapping, reverseSymbolMapping = getSymbolMapping()
	
	print symbolMapping
	wordLength = len(symbolMapping["_"])

	for outerState in sttm.listOfRealStates:
		coreStateDictionary[outerState.stateName] = State(outerState.stateName + "_read_", None, alphabetMSToTS())
		
		if outerState.isStartState:
			coreStateDictionary[outerState.stateName].makeStartState()
			
		for outerState in sttm.listOfRealStates:
			