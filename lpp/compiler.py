from antlr4 import *
import sys
import os
from assignxgen import writeAssignsUpToX
from LPPLexer import LPPLexer
from LPPParser import LPPParser
from LPPListener import LPPListener
from codewriter import *
import time

def main(argv):
    input = FileStream(argv[1])
    lexer = LPPLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LPPParser(stream)
    tree = parser.prog()

    writer = CodeWriter()
    walker = ParseTreeWalker()
    walker.walk(writer, tree)

if __name__ == '__main__':
    main(sys.argv)
