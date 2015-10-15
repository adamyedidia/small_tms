from antlr4 import *
import sys
import os
from assignxgen import writeAssignsUpToX
from LoseLexer import LoseLexer
from LoseParser import LoseParser
from LoseListener import LoseListener
from codeexecutor import *
import time

def main(argv):
    input = FileStream(argv[1])
    lexer = LoseLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LoseParser(stream)
    tree = parser.prog()

    executor = CodeExecutor()
    walker = ParseTreeWalker()
    walker.walk(executor, tree)

if __name__ == '__main__':
    main(sys.argv)
