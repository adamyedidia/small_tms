class SimpleState:
	def __init__(self, stateName, alphabet=["_", "1", "H", "E"]):
		self.stateName = stateName
		self.nextStateDict = {}
		self.headMoveDict = {}
		self.writeDict = {}

		if alphabet == None:
			self.alphabet = ["_", "1", "H", "E"]
		else:
			self.alphabet = alphabet

		for symbol in self.alphabet:
			self.nextStateDict[symbol] = self
			self.headMoveDict[symbol] = "-"
			self.writeDict[symbol] = symbol

		self.isStartState = False

	def isState(self):
		return True

class State:
	def __init__(self, stateName, description="", alphabet=["_", "1", "H", "E"]):
	
		self.stateName = stateName
		self.nextStateDict = {}
		self.headMoveDict = {}
		self.writeDict = {}
		self.description = description

		if alphabet == None:
			self.alphabet = ["_", "1", "H", "E"]
		else:
			self.alphabet = alphabet

		errorState = SimpleState("ERROR", self.alphabet)

		for symbol in self.alphabet:
			self.nextStateDict[symbol] = errorState
			self.headMoveDict[symbol] = "-"
			self.writeDict[symbol] = symbol

		self.isStartState = False
	
	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False
		
		for i, symbol in enumerate(self.alphabet):
			if other.alphabet[i] != symbol:
				return False

		for symbol in self.alphabet:
			if self.nextStateDict[symbol].stateName != other.nextStateDict[symbol].stateName:
				return False
			
			if self.headMoveDict[symbol] != other.headMoveDict[symbol]:
				return False

			if self.writeDict[symbol] != other.writeDict[symbol]:
				return False

		return True

	def __ne__(self, other):
		return not self.__eq__(other)

	def infoHash(self):
		returnString = ""
		
		for symbol in self.alphabet:
			returnString += symbol + ":" + self.nextStateDict[symbol].stateName + ";" + \
					self.headMoveDict[symbol] + self.writeDict[symbol]

		return returnString

	def setNextState(self, symbol, nextState):
		assert symbol in self.alphabet
		assert nextState.isState()
		self.nextStateDict[symbol] = nextState
			
	def setHeadMove(self, symbol, headMove):
		assert symbol in self.alphabet
		assert headMove in ["L", "R", "-"]
		self.headMoveDict[symbol] = headMove
			
	def setWrite(self, symbol, write):
		assert symbol in self.alphabet
		assert write in self.alphabet
		self.writeDict[symbol] = write

	def set3(self, symbol, nextState, headMove, write):
		self.setNextState(symbol, nextState)
		self.setHeadMove(symbol, headMove)
		self.setWrite(symbol, write)

	def setAllNextStates(self, nextState):
		assert nextState.isState()
		for symbol in self.alphabet:
			self.nextStateDict[symbol] = nextState

	def setAllHeadMoves(self, headMove):
		assert headMove in ["L", "R", "-"]
		for symbol in self.alphabet:
			self.headMoveDict[symbol] = headMove

	def setAllWrites(self, write):
		assert write in self.alphabet
		for symbol in self.alphabet:
			self.writeDict[symbol] = write

	def setAll3(self, nextState, headMove, write):
		self.setAllNextStates(nextState)
		self.setAllHeadMoves(headMove)
		self.setAllWrites(write)

	def getNextState(self, symbol):
		return self.nextStateDict[symbol]

	def getNextStateName(self, symbol):
		try:
#			print self.nextStateDict[symbol]
			return self.nextStateDict[symbol].stateName
		except KeyError:
			print "Error: I, state", self.stateName, "don't know about symbol", symbol
			raise

	def getHeadMove(self, symbol):
		return self.headMoveDict[symbol]

	def getWrite(self, symbol):
		try:
			return self.writeDict[symbol]		
		except KeyError:
			print "Error: I, state", self.stateName, "don't know about symbol", symbol
			print "My alphabet is", self.alphabet
			raise
	
	def isState(self):
		return True

	def makeStartState(self):
		self.isStartState = True
