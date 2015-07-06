def getToTopFunction(inState, listOfStates):
	# inState might have been called findStackState
	
	name = "cpu_get_to_fn"
	
	findPattern(inState, markFirstFunctionState, listOfStates, name + "_mark_first_fn", "HH", "L", "L", "H")
	
	moveBy(markFirstFunctionState, name + "_mark_first_fn", 2, "R", writeHState)

	writeHState.set3("_", goLeftState, "L", "H")
	goLeftState, 
	
	findPattern(findTwoUnderScoresState, goRightState, listOfStates, name + "____1", "__", "L", "R", "_")
	
	moveBy(goRightState, "", 1, "R", )
	