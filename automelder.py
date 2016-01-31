import os
import sys

path = sys.argv[1]
target = sys.argv[2]

print "Generating the preliminary TM..."
os.system("python preliminary.py " + path + " prelim_tm_4s.txt")

print "Converting the preliminary TM to a 2-symbol TM..."
os.system("python tmreader.py prelim_tm_4s.txt prelim_tm_2s.txt")

print "Generating the code-writing TM..."
os.system("python codebarfer.py " + path + " code_write_tm_2s.txt")

print "Generating the code-running TM..."
os.system("python coderunner.py " + path + " code_run_tm_4s.txt")

print "Converting the code-running TM to a 2-symbol TM..."
os.system("python tmreader.py code_run_tm_4s.txt code_run.txt")

print "Melding the preliminary TM and the code-writing TM..."
os.system("python tmmelder.py prelim_tm_2s.txt code_write_tm_2s.txt code_gen.txt")

print "Melding the code-generating TMs with the code-running TM..."
os.system("python tmmelder.py code_gen.txt code_run.txt " + target)

print "Process complete!"