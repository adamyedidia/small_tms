import string
import sys

sys.path.insert(0, '/home/adamyedidia/thesis/turdtotm')
from state import *
from tmsim import *

if __name__ == "__main__":
	sttm = SingleTapeTuringMachine(sys.argv[-1], ["a", "b"])
	args = sys.argv[1:-1]

	quiet = ("-q" in args)

	numSteps = float("Inf") # default value
	if ("-s" in args):
		numSteps = args[args.index("-s") + 1]

	output = None
	if ("-f" in args):
		output = open(args[args.index("-f") + 1], "w")

	sttm.run(quiet, numSteps, output)
