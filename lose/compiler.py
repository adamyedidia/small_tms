from antlr4 import *
import sys
import os
from assignxgen import writeAssignsUpToX
from LoseLexer import LoseLexer
from LoseParser import LoseParser
from LoseListener import LoseListener
from codewriter import *
import time

def main(argv):
    input = FileStream(argv[1])
    lexer = LoseLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LoseParser(stream)
    tree = parser.prog()

    writer = CodeWriter()
    walker = ParseTreeWalker()
    walker.walk(writer, tree)

if __name__ == '__main__':
    main(sys.argv)
