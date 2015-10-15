import string
import re
from writer import *
from tmsim import *

class TuringMachineWithStack:
    def __init__(self, functions, path, functionLabelDictionary, functionLineDictionary, functionVariableDictionary, lineNumberToTextNumber, initVarString):
		
        mainFunctionName = string.strip(functions[0])
		
        self.stack = [(mainFunctionName, functionVariableDictionary[mainFunctionName], 1)]
        self.lineNumber = 1
		
        self.path = path
        self.functions = functions
        self.functionLabelDictionary = functionLabelDictionary
        self.functionLineDictionary = functionLineDictionary
        self.functionVariableDictionary = functionVariableDictionary
        self.lineNumberToTextNumber = lineNumberToTextNumber
		
        self.tapeDictionary = {}
        
        firstLineOfMainFunction = open(path + string.strip(functions[0]) + ".tfn", "r").readlines()[0]
        
        for i, varName in enumerate(string.split(firstLineOfMainFunction)[1:]):
            tape = Tape(varName, "_")
            
            self.tapeDictionary[i+1] = tape
            
            for j, symbol in enumerate(initVarString):
                self.tapeDictionary[i+1].tapeDict[j] = symbol
    
    # Returns 1 upon halting, 0 otherwise    
    def runOneStep(self):
                
        currentFunction = self.stack[-1][0]
        print currentFunction, self.lineNumber
        currentLine = self.functionLineDictionary[currentFunction][self.lineNumber]
        
        # get rid of labels
        currentLine = string.split(currentLine, ":")[-1]
        
        if "[" in currentLine:
            # direct command
            splitLine = re.split("[\[|\]]", currentLine)
			
            variableName = splitLine[1]
            reactions = string.split(splitLine[2], ";")
            
            foundAppropriateReaction = False
            
            tapeName = self.stack[-1][1][variableName]
            
            currentTape = self.tapeDictionary[tapeName]
            currentSymbol = currentTape.readSymbol()
                        
            for reaction in reactions:
                
                # ugly stuff at the end of next line is for removing whitespce
                splitReaction = re.split("[(|)|,]", string.strip(reaction).replace(" ", ""))
                if splitReaction[0] == currentSymbol:
                    foundAppropriateReaction = True
                
                    for command in splitReaction[1:]:
                        if command in ["1", "E", "_"]:
                            currentTape.writeSymbol(command)
                    
                    for command in splitReaction[1:]:
                        if command in ["L", "R", "-"]:
                            currentTape.moveHead(command)
                    
                    foundGoto = False
                    for command in splitReaction[1:]:
                        if not command in ["1", "E", "_", "L", "R", "-", ""]:
                            try:                                
                                self.lineNumber = self.functionLabelDictionary[currentFunction][command]
                                foundGoto = True
                            except:
                                print "Unrecognized label on line", self.lineNumberToTextNumber[self.lineNumber], "of function", currentFunction
                                raise
                    
                    if not foundGoto:
                        self.lineNumber += 1
                    
            if not foundAppropriateReaction:
                print "Turing machine threw error on line", self.lineNumberToTextNumber[self.lineNumber], "of function", currentFunction
                return 1
        
        elif string.split(currentLine)[0] == "function":
            
            oldMappingDict = self.stack[-1][1]
            
            calledFunction = string.split(currentLine)[1]
            firstLineOfCalledFunctionSplit = string.split(open(self.path + calledFunction + ".tfn", "r").readlines()[0])
            
            argList = string.split(currentLine)[2:]
            
            try:
                assert len(firstLineOfCalledFunctionSplit[1:]) == len(argList)
            except:
                print "Function call on line", self.lineNumberToTextNumber[self.lineNumber], "of function", currentFunction, "has", len(argList), \
                    "arguments, but the function being called has", len(firstLineOfCalledFunctionSplit[1:]), "inputs."
                raise
            
            newMappingDict = {}
            
            for i, variableName in enumerate(firstLineOfCalledFunctionSplit[1:]):
                newMappingDict[variableName] = oldMappingDict[argList[i]]
            
            self.stack.append((calledFunction, newMappingDict, self.lineNumber + 1))
            self.lineNumber = 1
            
        elif string.split(currentLine)[0] == "return":
            
            oldLineNumber = self.lineNumber
            
            self.lineNumber = self.stack[-1][2]
            self.stack.pop()
            
            if len(self.stack) == 0:
                print "Turing machine halted on line", self.lineNumberToTextNumber[oldLineNumber], "of function", currentFunction
                return 1
            
        else:
            print "Line", self.lineNumberToTextNumber[self.lineNumber], "of function", currentFunction, "is malformed."
            raise
            
        return 0
                        

    def run(self, quiet=False, numSteps=float("Inf"), outputFile=None):
        stepCounter = 0        
        
        while self.runOneStep() == 0:
            stepCounter += 1
            if stepCounter >= numSteps:
                print "Turing machine ran for", numSteps, "steps without halting."
                break
            
            if not quiet:                    
                self.printAllTapes(-2, 160, outputFile)
        
    def printAllTapes(self, start, end, output):
        
        outString = "Function: " + self.stack[-1][0] + "\n"
        outString += "Line number: " + str(self.lineNumberToTextNumber[self.lineNumber]) + "\n"
        outString += "\n"
        
        for tape in self.tapeDictionary.values():
            outString += tape.getTapeOutput(start, end)
            
        outString += "\n"
        outString += "Stack:\n"
        outString += "\n"
        
        for tupIndex in range(len(self.stack) - 1, -1, -1):
            outString += "Function " + self.stack[tupIndex][0] + " with return address " + \
                str(self.lineNumberToTextNumber[self.stack[tupIndex][2]]) + " and with mapping " + str(self.stack[tupIndex][1]) + "\n"
        
        outString += "\n"
        outString += "---------------------------------------"
        
        if output == None:
            print outString

        else:
            output.write(outString + "\n")
    
def main():    
    path = sys.argv[-1]

    try:
        functions = [string.strip(x) for x in open(path + "functions.tff", "r").readlines()]
    except:  
        raise Exception("No functions.tff file found in directory " + path) 

    functionLabelDictionary, functionDictionary, functionLineDictionary, lineNumberToTextNumber = getFunctionLabelDictionary(functions, path)
    functionVariableDictionary = getFunctionVariableDictionary(functions, path)

    try:
        initVarString = string.strip(open(path + "initvar", "r").read())
    except:
        raise Exception("No initvar file found in directory " + path)
    
    if "-q" in sys.argv:
        quiet = True
    else:
        quiet = False
            
    if "-s" in sys.argv:
        numSteps = int(sys.argv[sys.argv.index("-s") + 1])
    else:
        numSteps = float("inf")
    
    if "-f" in sys.argv:
        outputFile = open(path + sys.argv[sys.argv.index("-f") + 1], "w")
        outputFile.write("\n")
    else:
        outputFile = None
    
    TuringMachineWithStack(functions, path, functionLabelDictionary, functionLineDictionary, 
        functionVariableDictionary, lineNumberToTextNumber, initVarString).run(quiet, numSteps, outputFile)
    
    
if __name__ == "__main__":
    main()