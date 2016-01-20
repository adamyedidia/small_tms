from LPPListener import LPPListener
        
def pront(x):
    print x

class Function:
    def __init__(self, args, prog):
        self.args = args
        self.prog = prog

class CodeExecutor(LPPListener):
    def enterProg(self, ctx):
        self.typeDictionary = {}
        self.variableDictionary = {}
        self.funcDictionary = {}
        self.stack = []
                
        self.executeProg(ctx)
        
        pront("Program halted without errors.")    
            
    # for executing a sequence of commands (takes as input a prog)
    def executeProg(self, ctx):
        commandCounter = 0
        
        identityMapping = {}
            
        while ctx.trueprog().command(commandCounter) != None:
            
            command = ctx.trueprog().command(commandCounter)
                        
            if command.funcdef() != None:
                callBody = command.funcdef().funcprocbody().funcproccallbody()
                funcName = callBody.VAR(0).getText()
                prog = command.funcdef().funcprocbody().nondefprog()
        
                self.funcDictionary[funcName] = Function(callBody, prog)
                
            elif command.procdef() != None:
                raise
                # unimplemented
                
            elif command.declare() != None:
                declare = command.declare()
                
                if declare.intdecl() != None:
                    varName = declare.intdecl().VAR().getText()
                    
                    self.typeDictionary[varName] = "int"
                    self.variableDictionary[varName] = 0
                    
                    identityMapping[varName] = varName
                    
                elif declare.listdecl() != None:
                    varName = declare.listdecl().VAR().getText()
                    
                    self.typeDictionary[varName] = "list"
                    self.variableDictionary[varName] = 0   
                    
                    identityMapping[varName] = varName
                    # unimplemented
                
                elif declare.list2decl() != None:
                    varName = declare.list2decl().VAR().getText()
                    
                    self.typeDictionary[varName] = "list2"
                    self.variableDictionary[varName] = 0
                    
                    identityMapping[varName] = varName
                    # unimplemented
                    
                else:
                    raise
                    
            elif command.nondefcommand() != None:
                if self.executeNonDefCommand(command.nondefcommand(), identityMapping):
                    return
                
            else:
                raise
                
            commandCounter += 1
            
        pront("Error: main function terminated without return or halt statement")
        raise  
                    
    
    # for executing a sequence of nondefcommands IN A FUNCTION
    # (takes as input a nondefprog)
    def executeFunctionBody(self, ctx, mapping):
        commandCounter = 0
        
        while ctx.nondefcommand(commandCounter) != None:
            command = ctx.nondefcommand(commandCounter)
            
            if self.executeNonDefCommand(command, mapping):
                 # we got here via return statement; we're done!
                 return
            
            commandCounter += 1

        pront("Error: function terminated without return or halt statement")
        raise
            
        # 
    # for executing a sequence of nondefcommands (takes as input a nondefprog)
    # also takes as input a mapping of the variable names in the function call 
    # you're currently in to the original variable names
    def executeNonDefProg(self, ctx, mapping):
        commandCounter = 0
        
        while ctx.nondefcommand(commandCounter) != None:
            command = ctx.nondefcommand(commandCounter)
                         
            if self.executeNonDefCommand(command, mapping):
                # This means we got here via return satement
                return True
                
            commandCounter += 1
        
        #This means we got here via an if statement that just naturally ended
        return False
        
#        pront("Error: function terminated without return or halt statement")
#        raise
# I don't think this is right; there could be an ifstatement that ends.

    
    # For executing a single nondefcommand
    # returns a truth value that is True if there was a return statement that occurred
    # ( and that therefore the function that wraps the nondefprog should end)
    def executeNonDefCommand(self, command, mapping):
        if command.funcproccall() != None:    
            callBody = command.funcproccall().funcproccallbody()
            
            funcName = callBody.VAR(0).getText()
            
            newMapping = {}
            varCounter = 1
            
            functionBeingCalled = self.funcDictionary[funcName]
            
            while callBody.VAR(varCounter) != None:
                try:
                    assert functionBeingCalled.args.VAR(varCounter) != None
                except:
                    pront("Error: too many arguments in the function call of function " + \
                        funcName)
                    raise
                
                newMapping[functionBeingCalled.args.VAR(varCounter).getText()] = \
                    mapping[callBody.VAR(varCounter).getText()]
                    
                varCounter += 1
            
            try:
                assert functionBeingCalled.args.VAR(varCounter) == None
            except:
                pront("Error: too few arguments in the function call of function " + \
                    funcName)
            
            
            self.executeFunctionBody(functionBeingCalled.prog, newMapping)
            return False
            
        elif command.whileloop() != None:
            whileLoop = command.whileloop()
            while self.evaluateIntexpr(whileLoop.whileexpr().intexpr(), mapping) > 0:
                # Note that this if statement does stuff as it's called
                if self.executeNonDefProg(whileLoop.whilenondefprog().nondefprog(), mapping):
                    # Then there was a return statement in the while loop
                    return True
                    
            return False
                
        elif command.ifstate() != None:
            ifState = command.ifstate()
            if self.evaluateIntexpr(ifState.ifexpr().intexpr(), mapping) > 0:
                # This function doesn't just evaluate the truth of the if it also interprets the 
                # program
                if self.executeNonDefProg(ifState.ifnondefprog().nondefprog(), mapping):
                    # Then there was a return statement in the if statement
                    return True
                    
            return False
                
        elif command.ifelsestate() != None:
            ifElseState = command.ifelsestate()
            if self.evaluateIntexpr(ifElseState.ifelseexpr().intexpr()) > 0:
                if self.executeNonDefProg(ifElseState.ifelsenondefprog().nondefprog(), mapping):
                    return True
            else:
                if self.executeNonDefProg(ifElseState.elsenondefprog().nondefprog(), mapping):
                    return True
            return False
        
        elif command.assign() != None:
            assign = command.assign()
            self.variableDictionary[mapping[assign.VAR().getText()]] = \
                self.evaluateExpr(assign.expr(), mapping)
            return False
            
        elif command.returnstate() != None:
            return True
        
        elif command.printstate() != None:
            printState = command.printstate()
                        
            pront(mapping[printState.VAR().getText()] + ": " +  \
                str(self.variableDictionary[mapping[printState.VAR().getText()]]))    

#            pront(self.evaluate(printState.expr(), mapping))
                
            return False
            
        else:
            raise
            
    # for finding the value of an expr
    # takes as input an expr
    def evaluateExpr(self, ctx, mapping): 
        if ctx.intexpr() != None:
            return self.evaluateIntexpr(ctx.intexpr(), mapping)
            
        elif ctx.listexpr() != None:
            return self.evaluateListexpr(ctx.listexpr(), mapping)
            
        elif ctx.list2expr() != None:
            return self.evaluateList2expr(ctx.list2expr(), mapping)
            
    def evaluateIntexpr(self, ctx, mapping):
#        print ctx, ctx.getText()
        if ctx.INT() != None:
            return int(ctx.INT().getText())
        
        elif ctx.VAR() != None:
            return self.variableDictionary[mapping[ctx.VAR().getText()]]
        
        elif ctx.OPERATOR_NOT() != None:
            if ctx.OPERATOR_NOT().getText() == "!":
                booleanBelow = self.evaluateIntexpr(ctx.intexpr(0), mapping)
                if booleanBelow == 0:
                    return 1
                elif booleanBelow != 0:
                    return 0
                    
        elif ctx.OPERATOR_NEGATE() != None:
            return -1 * self.evaluateIntexpr(ctx.intexpr(0), mapping)            
            
        elif ctx.OPERATOR_LENGTH() != None:
            return len(self.evaluateListexpr(ctx.listexpr(), mapping))    
            
        elif ctx.OPERATOR_LENGTH2() != None:
            return len(self.evaluateList2expr(ctx.list2expr(), mapping))    
            
        elif ctx.listexpr() != None:
            # this is the listindex case
            l = self.evaluateListexpr(ctx.listexpr(), mapping)
            i = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            assert type(l) == type([])
            assert type(i) == type(0)
            result = l[i]
            assert type(result) == type(0)
            
            return result
            
        elif ctx.intexpr(0) != None and ctx.intexpr(1) == None:
            # this is the parens case; it had better be the only undone case
            # where there is only one intexpr (any others have to go before)
            # since the check is that there is exactly one intexpr
            return self.evaluateIntexpr(ctx.intexpr(0), mapping)
            
        elif ctx.OPERATOR_MUL_DIV() != None:
            firstNum = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            secondNum = self.evaluateIntexpr(ctx.intexpr(1), mapping)
            
            if ctx.OPERATOR_MUL_DIV().getText() == "*":
                return firstNum * secondNum
            
            elif ctx.OPERATOR_MUL_DIV().getText() == "/":
                try:
                    assert secondNum != 0
                except:
                    print "Error: division by zero"
                    raise
            
                return firstNum / secondNum
                
            elif ctx.OPERATOR_MUL_DIV().getText() == "%":
                try:
                    assert secondNum != 0
                except:
                    print "Error: division by zero"
                    raise
            
                return firstNum % secondNum                
                
            else:
                raise
            
        elif ctx.OPERATOR_ADD_SUB() != None:
            firstNum = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            secondNum = self.evaluateIntexpr(ctx.intexpr(1), mapping)
            
            if ctx.OPERATOR_ADD_SUB().getText() == "+":
                return firstNum + secondNum
                
            elif ctx.OPERATOR_ADD_SUB().getText() == "-":
                result = firstNum - secondNum
                return result
                
            else:
                raise
                
        elif ctx.OPERATOR_COMPARE() != None:
            firstNum = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            secondNum = self.evaluateIntexpr(ctx.intexpr(1), mapping)
            
            if ctx.OPERATOR_COMPARE().getText() == "==":
                if firstNum == secondNum:
                    return 1
                else:
                    return 0
                    
            elif ctx.OPERATOR_COMPARE().getText() == "!=":
                if firstNum != secondNum:
                    return 1
                else:
                    return 0
            
            elif ctx.OPERATOR_COMPARE().getText() == ">":
                if firstNum > secondNum:
                    return 1
                else:
                    return 0
            
            elif ctx.OPERATOR_COMPARE().getText() == "<":
                if firstNum < secondNum:
                    return 1
                else:
                    return 0
                    
            elif ctx.OPERATOR_COMPARE().getText() == ">=":
                if firstNum >= secondNum:
                    return 1
                else:
                    return 0
                    
            elif ctx.OPERATOR_COMPARE().getText() == "<=":
                if firstNum <= secondNum:
                    return 1
                else:
                    return 0
                    
            else:
                raise
                
        elif ctx.OPERATOR_BOOLEAN() != None:
            firstNum = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            secondNum = self.evaluateIntexpr(ctx.intexpr(1), mapping)
            
            if ctx.OPERATOR_BOOLEAN().getText() == "&":
                if firstNum != 0:
                    if secondNum != 0:
                        return 1
                    else:
                        return 0
                else:
                    return 0
                    
            elif ctx.OPERATOR_BOOLEAN().getText() == "|":
                if firstNum != 0:
                    return 1
                elif secondNum != 0:
                    return 1
                else:
                    return 0
                    
            else:
                raise
        
    def evaluateListexpr(self, ctx, mapping):
#        print ctx, ctx.getText()
        
        if ctx.OPERATOR_APPEND() != None:
            l = self.evaluateListexpr(ctx.listexpr(0), mapping)
            i = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            assert type(l) == type([])
            assert type(i) == type(0)
            return l + [i]
            
        elif ctx.OPERATOR_CONCAT() != None:
            firstList = self.evaluateListexpr(ctx.listexpr(0), mapping)
            secondList = self.evaluateListexpr(ctx.listexpr(1), mapping)
            assert type(firstList) == type([])
            assert type(secondList) == type([])
            return firstList + secondList
            
        elif ctx.list2expr() != None:
            l2 = self.evaluateList2expr(ctx.list2expr(), mapping)
            i = self.evaluateIntexpr(ctx.intexpr(0), mapping)
            assert type(l2) == type([])
            assert type(i) == type(0)
            result = l2[i]
            assert type(result) == type([])
            return result
            
        elif ctx.VAR() != None:
            return self.variableDictionary[mapping[ctx.VAR().getText()]]
            
        elif ctx.listexpr(0) != None:
#            print ctx.listexpr(0).getText()
            # This is the parens case
            # There better be no cases after this containing listexprs
            return self.evaluateListexpr(ctx.listexpr(0), mapping)
            
        elif ctx.intexpr(0) != None:
            # Build your own list!
            returnList = []
            exprCounter = 0
            
            while ctx.intexpr(exprCounter) != None:
                returnList.append(self.evaluateIntexpr(ctx.intexpr(exprCounter), mapping))
                exprCounter += 1
                
            return returnList
            
        else:
            # empty list case
            return []
            
    def evaluateList2expr(self, ctx, mapping):
        if ctx.OPERATOR_APPEND() != None:
            l2 = self.evaluateList2expr(ctx.list2expr(), mapping)
            l = self.evaluateListexpr(ctx.listexpr(), mapping)
            return l2 + [l]
        
        elif ctx.OPERATOR_CONCAT() != None:
            firstList2 = self.evaluateList2expr(ctx.list2expr(0), mapping)
            secondList2 = self.evaluateList2expr(ctx.list2expr(1), mapping)
            
            return firstList2 + secondList2
            
        elif ctx.list2expr() != None:
            # This is the parens case
            # There better not be any cases after this one containing list2exprs
            return self.evaluateList2expr(ctx.list2expr(), mapping)
            
        elif ctx.listexpr() != None:
            # Build your own list!
            returnList2 = []
            exprCounter = 0
            
            while ctx.listexpr(exprCounter) != None:
                returnList.append(self.evaluateListexpr(ctx.listexpr(exprCounter), mapping))
                exprCounter += 1
                
            return returnList2
            
        elif ctx.VAR() != None:
            return self.variableDictionary[mapping[ctx.VAR().getText()]]
            
        else:
            # empty list2 case
            return []