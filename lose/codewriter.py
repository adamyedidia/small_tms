from LoseListener import LoseListener

class Function():
    def __init__(self, name):
        self.name = name
        self.funcString = ""
        self.largestFilledReg = -1
    
    def add(self, s):
        self.funcString += s

class CodeWriter(LoseListener):

    def enterProg(self, ctx):
        self.variableDictionary = {}
        self.funcProcDictionary = {}
        self.filledRegs = []
        self.currentFunc = Function("main")
        self.currentFile = open("main.tfn", "w")
        self.ifCounter = 0
        self.whileCounter = 0

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

    def enterProcDef(self, ctx):
        procName = ctx.funcprocbody().funcproccallbody().VAR(0).getText()
        self.funcProcDictionary[procName] = "proc"

    def enterFuncproccall(self, ctx):
        funcProcName = ctx.funcproccallbody().VAR(0).getText()
        
        if funcProcDictionary[funcProcName] == "func":
            self.currentFunc.add("function " + funcprocName)

            counter = 1
            
            while not ctx.funcproccallbody().VAR(counter) == None:
                self.currentFunc.add(" " + ctx.funcproccallbody().VAR(counter).getText())

        if self.funcProcDictionary[funcProcName] == "proc":
            pass

    def enterExpr(self, ctx):
        print "current expr", ctx.getText()
        
        ctx.newAttribute = "hi!"
#        print ctx.newAttribute

    # release locks on the children and take hold of the lock on yourself
    def exitExpr(self, ctx):
        
        # if it's not just parens do stuff
        if not (ctx.expr(0) != None and ctx.expr(1) == None):
            # take lock
            ctx.associatedReg = self.findSmallestUnfilledReg()
            self.fillReg(ctx.associatedReg)        
        
            if ctx.expr(0) != None and ctx.expr(1) != None:                 
                self.currentFunc.add(self.dealWithExpr(ctx, stringify(ctx.associatedReg), \
                    stringify(ctx.expr(0).associatedReg), stringify(ctx.expr(1).associatedReg)))

                print ctx.getText(), ctx.associatedReg
                print ctx.expr(0).getText(), ctx.expr(0).associatedReg
                print ctx.expr(1).getText(), ctx.expr(1).associatedReg

                print self.dealWithExpr(ctx, stringify(ctx.associatedReg), \
                    stringify(ctx.expr(0).associatedReg), stringify(ctx.expr(1).associatedReg))
            
                # release lock
                self.emptyReg(ctx.expr(0).associatedReg) 
                self.emptyReg(ctx.expr(1).associatedReg)
        
            else:
                print self.dealWithExpr(ctx, stringify(ctx.associatedReg), None, None)
                self.currentFunc.add(self.dealWithExpr(ctx, stringify(ctx.associatedReg), None, None))   
        
        else:
            # if it's just parens don't do shit
            ctx.associatedReg = ctx.expr(0).associatedReg    
            
        print self.filledRegs    

    def exitWhileexpr(self, ctx):
        assert len(self.filledRegs) == 1
        self.currentFunc.add("WHILE_TEST_" + str(self.whileCounter) + ": [" + stringify(self.filledRegs[0]) + \
            "] E (WHILE_STATE_" + str(self.whileCounter) + "_FALSE); 1 ()\n")
        
        self.emptyReg(self.filledRegs[0])
        
    def exitWhilenondefprog(self, ctx):
        dummyReg = self.findSmallestUnfilledReg()
        
        self.currentFunc.add("[" + stringify(dummyReg) + "] E (WHILE_TEST_" + str(self.whileCounter) + ")\n")
        self.currentFunc.add("WHILE_STATE_" + str(self.whileCounter) + "_FALSE: ")

    # if the holder variable that holds the expression has a positive value, skip to the label at the end of the if statement
    def exitIfexpr(self, ctx):
        assert len(self.filledRegs) == 1
        self.currentFunc.add("[" + stringify(self.filledRegs[0]) + "] E (IF_STATE_" + str(self.ifCounter) + "_FALSE); 1 ()\n")
        
        self.emptyReg(self.filledRegs[0])
        
    # Place the label at the end of the concluded if statement. Note the intentional lack of \n
    def exitIfnondefprog(self, ctx):
        self.currentFunc.add("IF_STATE_" + str(self.ifCounter) + "_FALSE: ")
        self.ifCounter += 1

    def exitAssign(self, ctx):
        # should be just one reg full, since it's the root of the expression tree
        assert len(self.filledRegs) == 1
        self.currentFunc.add("function assign " + ctx.VAR().getText() + " " + stringify(self.filledRegs[0]) + "\n")

        self.emptyReg(self.filledRegs[0])

#        self.currentFile.write(self.dealWithExpr(ctx.expr(), ctx.VAR(), self.filledRegs[0], None))

    def exitReturnstate(self, ctx):
        self.currentFunc.add("return\n")

    def findSmallestUnfilledReg(self):
        x = 0
        while x in self.filledRegs:
            x += 1
            
        self.currentFunc.largestFilledReg = max(self.currentFunc.largestFilledReg, x)    
            
        return x
                
    def fillReg(self, reg):
        assert not (reg in self.filledRegs)
        self.filledRegs.append(reg)
    
    def emptyReg(self, reg):
        assert reg in self.filledRegs
        self.filledRegs.remove(reg)

    # Loads the result of the operation ctx on regs 2 and 3 into reg 1
    def dealWithExpr(self, ctx, reg1, reg2, reg3):
        comp = ctx.OPERATOR_COMPARE()
        
        if ctx.INT() != None:
            return "function assign" + ctx.INT().getText() + " " + reg1 + "\n"
        
        elif ctx.VAR() != None:    
            return "function assign " + reg1 + " " + ctx.VAR().getText() + "\n"
                
        elif ctx.expr(0) != None and ctx.expr(1) == None:
            # parens
            return ""        
                
        elif ctx.OPERATOR_MUL_DIV() != None:    
            if ctx.OPERATOR_MUL_DIV().getText() == "*":
                return "function multiply " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_MUL_DIV().getText() == "/":
                return "function divide " + reg1 + " " + reg2 + " " + reg3 + "\n"
        
        elif ctx.OPERATOR_ADD_SUB() != None:    
            if ctx.OPERATOR_ADD_SUB().getText() == "+":
                return "function add " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_ADD_SUB().getText() == "-":
                return "function subtract " + reg1 + " " + reg2 + " " + reg3 + "\n"
        
        elif comp != None:    
            if ctx.OPERATOR_COMPARE().getText() == ">":
                return "function greaterThan " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "<":
                # Note the inversion of reg2 and reg3
                return "function greaterThan " + reg1 + " " + reg3 + " " + reg2 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == ">=":
                return "function greaterOrEqual " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "<=":
                return "function greaterOrEqual " + reg1 + " " + reg3 + " " + reg2 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "==":
                return "function equal " + reg1 + " " + reg2 + " " + reg3 + "\n"
            
            elif ctx.OPERATOR_COMPARE().getText() == "!=":
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

def stringify(regNum):
    return "!" + str(regNum)
        
#def addSmallConst(label):
#    returnString = label + ": [" + 
