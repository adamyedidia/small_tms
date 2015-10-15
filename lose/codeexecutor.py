from LoseListener import LoseListener
        
def pront(x):
    print x

class Function:
    def __init__(self, args, prog):
        self.args = args
        self.prog = prog

class CodeExecutor(LoseListener):
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
                
                if declare.natdecl() != None:
                    varName = declare.natdecl().VAR().getText()
                    
                    self.typeDictionary[varName] = "nat"
                    self.variableDictionary[varName] = 0
                    
                    identityMapping[varName] = varName
                    
                elif declare.signdecl() != None:
                    varName = declare.signdecl().VAR().getText()
                    
                    self.typeDictionary[varName] = "signed"
                    self.variableDictionary[varName] = 0
                    
                    identityMapping[varName] = varName
                    
                    # unimplemented
                    raise
                    
                elif declare.listdecl() != None:
                    varName = declare.listdecl().VAR().getText()
                    
                    self.typeDictionary[varName] = "list"
                    self.variableDictionary[varName] = 0   
                    
                    identityMapping[varName] = varName
                    # unimplemented
                    raise       
                
                elif declare.list2decl() != None:
                    varName = declare.list2decl().VAR().getText()
                    
                    self.typeDictionary[varName] = "list2"
                    self.variableDictionary[varName] = 0
                    
                    identityMapping[varName] = varName
                    # unimplemented
                    raise
                    
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
            while self.evaluate(whileLoop.whileexpr().expr(), mapping) > 0:
                # Note that this if statement does stuff as it's called
                if self.executeNonDefProg(whileLoop.whilenondefprog().nondefprog(), mapping):
                    # Then there was a return statement in the while loop
                    return True
                    
            return False
                
        elif command.ifstate() != None:
            ifState = command.ifstate()
            if self.evaluate(ifState.ifexpr().expr(), mapping) > 0:
                # This function doesn't just evaluate the truth of the if it also interprets the 
                # program
                if self.executeNonDefProg(ifState.ifnondefprog().nondefprog(), mapping):
                    # Then there was a return statement in the if statement
                    return True
                    
            return False
                
        elif command.ifelsestate() != None:
            ifElseState = command.ifelsestate()
            if self.evaluate(ifElseState.ifelseexpr().expr()) > 0:
                if self.executeNonDefProg(ifElseState.ifelsenondefprog().nondefprog(), mapping):
                    return True
            else:
                if self.executeNonDefProg(ifElseState.elsenondefprog().nondefprog(), mapping):
                    return True
            return False
        
        elif command.assign() != None:
            assign = command.assign()
            self.variableDictionary[mapping[assign.VAR().getText()]] = \
                self.evaluate(assign.expr(), mapping)
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
            
    # for finding the value of an expr (takes as input an expr)
    def evaluate(self, ctx, mapping):
        if ctx.INT() != None:
            return int(ctx.INT().getText())
        
        elif ctx.VAR() != None:
            return self.variableDictionary[mapping[ctx.VAR().getText()]]
        
        elif ctx.OPERATOR_NOT() != None:
            if ctx.OPERATOR_NOT().getText() == "!":
                booleanBelow = self.evaluate(ctx.expr())
                if booleanBelow == 0:
                    return 1
                elif booleanBelow > 0:
                    return 0
                else:
                    print "Error: negative boolean"
                    raise
            
        elif ctx.expr(0) != None and ctx.expr(1) == None:
            # this is the parens case
            return self.evaluate(ctx.expr(0), mapping)
            
        elif ctx.OPERATOR_MUL_DIV() != None:
            firstNum = self.evaluate(ctx.expr(0), mapping)
            secondNum = self.evaluate(ctx.expr(1), mapping)
            
            if ctx.OPERATOR_MUL_DIV().getText() == "*":
                return firstNum * secondNum
            
            elif ctx.OPERATOR_MUL_DIV().getText() == "/":
                try:
                    assert secondNum > 0
                except:
                    print "Error: division by zero or negative number"
                    raise
            
                return firstNum / secondNum
                
            elif ctx.OPERATOR_MUL_DIV().getText() == "%":
                try:
                    assert secondNum > 0
                except:
                    print "Error: division by zero or negative number"
                    raise
            
                return firstNum % secondNum                
                
            else:
                raise
            
        elif ctx.OPERATOR_ADD_SUB() != None:
            firstNum = self.evaluate(ctx.expr(0), mapping)
            secondNum = self.evaluate(ctx.expr(1), mapping)
            
            if ctx.OPERATOR_ADD_SUB().getText() == "+":
                return firstNum + secondNum
                
            elif ctx.OPERATOR_ADD_SUB().getText() == "-":
                result = firstNum - secondNum
                try:
                    assert result >= 0
                except:
                    print "Error: negative value obtained"
                    raise
                    
                return result
                
            else:
                raise
                
        elif ctx.OPERATOR_COMPARE() != None:
            firstNum = self.evaluate(ctx.expr(0), mapping)
            secondNum = self.evaluate(ctx.expr(1), mapping)
            
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
            firstNum = self.evaluate(ctx.expr(0), mapping)
            secondNum = self.evaluate(ctx.expr(1), mapping)
            
            if ctx.OPERATOR_BOOLEAN().getText() == "&":
                if firstNum > 0:
                    if secondNum > 0:
                        return 1
                    else:
                        return 0
                else:
                    return 0
                    
            elif ctx.OPERATOR_BOOLEAN().getText() == "|":
                if firstNum > 0:
                    return 1
                elif secondNum > 0:
                    return 1
                else:
                    return 0
                    
            else:
                raise
                
    