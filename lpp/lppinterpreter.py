from antlr4 import *
import sys
import os
from assignxgen import writeAssignsUpToX
from LPPLexer import LPPLexer
from LPPParser import LPPParser
from LPPListener import LPPListener
from codeexecutor import *
import time

def main(argv):
    inp = FileStream(argv[1])
    lexer = LPPLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = LPPParser(stream)
    tree = parser.prog()

    executor = CodeExecutor()
    walker = ParseTreeWalker()
    walker.walk(executor, tree)

if __name__ == '__main__':
    main(sys.argv)
