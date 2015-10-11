from LoseListener import LoseListener

def pront(x):
    print x

class Function():
    def __init__(self, name):
        self.name = name
        self.funcString = "\n// Auto-generated code for function " + name + "\n\n"
        self.largestFilledReg = -1
        self.filledRegs = []
        self.ifCounter = 0
        self.whileCounter = 0
        self.ifElseCounter = 0
    
    def add(self, s):
        self.funcString += s
        
    def findSmallestUnfilledReg(self):
        x = 0
        while x in self.filledRegs:
            x += 1
            
        self.largestFilledReg = max(self.largestFilledReg, x)    
            
        return x
                
    def fillReg(self, reg):
        assert not (reg in self.filledRegs)
        self.filledRegs.append(reg)
    
    def emptyReg(self, reg):
        assert reg in self.filledRegs
        self.filledRegs.remove(reg)

class CodeWriter(LoseListener):

    def enterProg(self, ctx):
        self.variableDictionary = {}
        self.funcProcDictionary = {}
        self.funcAuxCountDictionary = {}
        self.mainFunc = Function("main")
        self.funcSet = {}
        self.currentFunc = self.mainFunc
        self.currentFile = open("main.tfn", "w")

    def exitTrueprog(self, ctx):
        self.writeMainInputLine()
        self.currentFile.write(self.mainFunc.funcString)
        
    def exitCommand(self, ctx):
        pass
        
    def enterFuncdef(self, ctx):
        funcName = ctx.funcprocbody().funcproccallbody().VAR(0).getText()
        self.funcProcDictionary[funcName] = "func"
        self.currentFunc = Function(funcName)
        self.currentFile = open(funcName + ".tfn", "w")
        
    def exitFuncdef(self, ctx):
        inputLine = "input "
        
        listOfArguments = []
        argumentBody = ctx.funcprocbody().funcproccallbody()
        
        varCounter = 1
        while argumentBody.VAR(varCounter) != None:
            listOfArguments.append(argumentBody.VAR(varCounter).getText())
            varCounter += 1
            
        for argument in listOfArguments:
            inputLine += argument + " "
            
        for reg in range(self.currentFunc.largestFilledReg + 1):
            inputLine += stringify(reg) + " "

        self.currentFunc.funcString = inputLine + "\n" + self.currentFunc.funcString

        self.currentFile.write(self.currentFunc.funcString)
        
        self.funcAuxCountDictionary[self.currentFunc.name] = self.currentFunc.largestFilledReg + 1
        self.currentFunc = self.mainFunc
        self.currentFile = open("main.tfn", "w")

    def enterProcDef(self, ctx):
        procName = ctx.funcprocbody().funcproccallbody().VAR(0).getText()
        self.funcProcDictionary[procName] = "proc"
        self.procArgsDictionary[procName] = ctx.funcprocbody().funcproccallbody()
        self.procBodyDictionary[procName] = ctx.funcprocbody().nondefprog()

    def enterFuncproccall(self, ctx):
        funcProcName = ctx.funcproccallbody().VAR(0).getText()
        
        try:
            assert funcProcName in self.funcProcDictionary
        except:
            pront("Error: unrecognized function name", funcProcName)
            raise

        args = ctx.funcproccallbody()
        
        if self.funcProcDictionary[funcProcName] == "func":
            self.currentFunc.add("function " + funcProcName + " ")
            # add in the arguments
            argCounter = 1
            while args.VAR(argCounter) != None:
                self.currentFunc.add(args.VAR(argCounter).getText() + " ")
                argCounter += 1
                
                
            assert len(self.currentFunc.filledRegs) == 0    
            # add in the dummy registers
            regsUsingForCall = []
            for i in range(self.funcAuxCountDictionary[funcProcName]):
                
                reg = self.currentFunc.findSmallestUnfilledReg()
                self.currentFunc.add(stringify(reg) + " ")  
                self.currentFunc.fillReg(reg)
                regsUsingForCall.append(reg)
                
            [self.currentFunc.emptyReg(reg) for reg in regsUsingForCall]
                
            self.currentFunc.add("\n")
            
        if self.funcProcDictionary[funcProcName] == "proc":
            
            # figure out which variables in the function declaration map to which variables in the function call
            mapping = {}
            declArgs = self.procArgsDictionary[funcProcName]
            callArgs = args
            
            argCounter = 1
            
            while declArgs.VAR(argCounter) != None:
                mapping[declArgs.VAR(argCounter)] = callArgs.VAR(argCounter)
                
                try:
                    assert callArgs.VAR(argCounter) != None
                except:
                    pront("Function call", funcProcName, "has too few arguments.")
                    raise
                
                argCounter += 1
                
            try:
                assert callArgs.VAR(argCounter) == None
            except:
                pront("Function call", funcProcName, "has too many arguments.")
                raise
                
            # ok procs just don't work for the time being
            
            
            self.currentFunc.add("")

    def enterExpr(self, ctx):        
        ctx.newAttribute = "hi!"

    # release locks on the children and take hold of the lock on yourself
    def exitExpr(self, ctx):
        
        # if it's not just parens do stuff
        if not (ctx.expr(0) != None and ctx.expr(1) == None):
            # take lock
            ctx.associatedReg = self.currentFunc.findSmallestUnfilledReg()
            self.currentFunc.fillReg(ctx.associatedReg)        
        
            if ctx.expr(0) != None and ctx.expr(1) != None:                 
                self.currentFunc.add(self.dealWithExpr(ctx, stringify(ctx.associatedReg), \
                    stringify(ctx.expr(0).associatedReg), stringify(ctx.expr(1).associatedReg)))
            
                # release lock
                self.currentFunc.emptyReg(ctx.expr(0).associatedReg) 
                self.currentFunc.emptyReg(ctx.expr(1).associatedReg)
        
            else:
                self.currentFunc.add(self.dealWithExpr(ctx, stringify(ctx.associatedReg), None, None))   
        
        else:
            # if it's just parens don't do shit
            ctx.associatedReg = ctx.expr(0).associatedReg    
            
    def enterWhileexpr(self, ctx):
        self.currentFunc.add("WHILE_TEST_" + str(self.currentFunc.whileCounter) + ": ")

    def exitWhileexpr(self, ctx):
        assert len(self.currentFunc.filledRegs) == 1
        self.currentFunc.add("[" + stringify(self.currentFunc.filledRegs[0]) + \
            "] E (WHILE_STATE_" + str(self.currentFunc.whileCounter) + "_FALSE); 1 ()\n")
        
        self.currentFunc.emptyReg(self.currentFunc.filledRegs[0])
        
    def exitWhilenondefprog(self, ctx):
        dummyReg = self.currentFunc.findSmallestUnfilledReg()
        
        self.currentFunc.add("[" + stringify(dummyReg) + "] E (WHILE_TEST_" + str(self.currentFunc.whileCounter) + ")\n")
        self.currentFunc.add("WHILE_STATE_" + str(self.currentFunc.whileCounter) + "_FALSE: ")

    # if the holder variable that holds the expression has a positive value, skip to the label at the end of the if statement
    def exitIfexpr(self, ctx):
        assert len(self.currentFunc.filledRegs) == 1
        self.currentFunc.add("[" + stringify(self.currentFunc.filledRegs[0]) + "] E (IF_STATE_" + \
            str(self.currentFunc.ifCounter) + "_FALSE); 1 ()\n")
        
        self.currentFunc.emptyReg(self.currentFunc.filledRegs[0])    
        
    # Place the label at the end of the concluded if statement. Note the intentional lack of \n
    def exitIfnondefprog(self, ctx):
        self.currentFunc.add("IF_STATE_" + str(self.currentFunc.ifCounter) + "_FALSE: ")
        self.currentFunc.ifCounter += 1
        
    def exitIfelseexpr(self, ctx):
        assert len(self.currentFunc.filledRegs) == 1
        self.currentFunc.add("[" + stringify(self.currentFunc.filledRegs[0]) + "] E (IF_ELSE_STATE_" + \
            str(self.currentFunc.ifElseCounter) + "_FALSE); 1 ()\n")
        
        self.currentFunc.emptyReg(self.currentFunc.filledRegs[0])
    
    def exitIfelsenondefprog(self, ctx):
        dummyReg = self.currentFunc.findSmallestUnfilledReg()        
        
        self.currentFunc.add("[" + stringify(dummyReg) + "] E (IF_ELSE_STATE_" + str(self.currentFunc.ifElseCounter) + "_TRUE)\n")
        self.currentFunc.add("IF_ELSE_STATE_" + str(self.currentFunc.ifElseCounter) + "_FALSE: ")
        
    def editElsenondefprog(self, ctx):
        self.currentFunc.add("IF_ELSE_STATE_" + str(self.currentFunc.ifElseCounter) + "_TRUE: ")
        self.currentFunc.ifElseCounter += 1

    def exitAssign(self, ctx):
        # should be just one reg full, since it's the root of the expression tree
        assert len(self.currentFunc.filledRegs) == 1
        self.currentFunc.add("function assign " + ctx.VAR().getText() + " " + stringify(self.currentFunc.filledRegs[0]) + "\n")

        self.currentFunc.emptyReg(self.currentFunc.filledRegs[0])

#        self.currentFile.write(self.dealWithExpr(ctx.expr(), ctx.VAR(), self.filledRegs[0], None))

    def exitReturnstate(self, ctx):
        self.currentFunc.add("return\n")

    # Loads the result of the operation ctx on regs 2 and 3 into reg 1
    def dealWithExpr(self, ctx, reg1, reg2, reg3):
        comp = ctx.OPERATOR_COMPARE()
        
        if ctx.INT() != None:
            self.funcSet["assign" + ctx.INT().getText()] = True
            return "function assign" + ctx.INT().getText() + " " + reg1 + "\n"
        
        elif ctx.VAR() != None:    
            self.funcSet["assign"] = True
            return "function assign " + reg1 + " " + ctx.VAR().getText() + "\n"
                
        elif ctx.expr(0) != None and ctx.expr(1) == None:
            # parens
            return ""        
                
        elif ctx.OPERATOR_MUL_DIV() != None:    
            if ctx.OPERATOR_MUL_DIV().getText() == "*":
                self.funcSet["multiply"] = True
                return "function multiply " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_MUL_DIV().getText() == "/":
                self.funcSet["divide"] = True
                return "function divide " + reg1 + " " + reg2 + " " + reg3 + "\n"
        
        elif ctx.OPERATOR_ADD_SUB() != None:    
            if ctx.OPERATOR_ADD_SUB().getText() == "+":
                self.funcSet["add"] = True
                return "function add " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_ADD_SUB().getText() == "-":
                self.funcSet["subtract"] = True
                return "function subtract " + reg1 + " " + reg2 + " " + reg3 + "\n"
        
        elif comp != None:    
            if ctx.OPERATOR_COMPARE().getText() == ">":
                self.funcSet["greaterThan"] = True
                return "function greaterThan " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "<":
                # Note the inversion of reg2 and reg3
                self.funcSet["greaterThan"] = True
                return "function greaterThan " + reg1 + " " + reg3 + " " + reg2 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == ">=":
                self.funcSet["greaterOrEqual"] = True
                return "function greaterOrEqual " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "<=":
                self.funcSet["greaterOrEqual"] = True
                return "function greaterOrEqual " + reg1 + " " + reg3 + " " + reg2 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "==":
                self.funcSet["equal"] = True
                return "function equal " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "!=":
                self.funcSet["notEqual"] = True
                return "function notEqual " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
        raise
            
    def exitProg(self, ctx):
        pass

    def enterNatdecl(self, ctx):                
        self.variableDictionary[ctx.VAR().getText()] = "nat"

    def enterSigndecl(self, ctx):                
        self.variableDictionary[ctx.VAR().getText()] = "signed"
    
    def enterListdecl(self, ctx):                
        self.variableDictionary[ctx.VAR().getText()] = "list"

    def enterList2decl(self, ctx):              
        self.variableDictionary[ctx.VAR().getText()] = "list2"
        
    def writeMainInputLine(self):
        inputLine = "input "
        
        for varName in self.variableDictionary:
            inputLine += varName + " "
        
        for reg in range(self.currentFunc.largestFilledReg + 1):
            inputLine += stringify(reg) + " "    
            
        inputLine += "\n"
        
        self.mainFunc.funcString = inputLine + self.mainFunc.funcString

def stringify(regNum):
    return "!" + str(regNum)
        
        
#def addSmallConst(label):
#    returnString = label + ": [" + 
