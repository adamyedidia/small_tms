import sys

def writeAssignsUpToX(x):
    if x >= 1:
        output = open("assign1.tfn", "w")
        output.write("input x\n\n")
        output.write("// Auto-generated code for function assign1\n")
        output.write("// Assigns x to the value 1\n")
        output.write("// Unary assumed\n\n")
        output.write("function clear x\n")
        output.write("function add1 x\n")
        output.write("return\n")
            
        for i in range(2, x+1):
            output = open("assign" + str(i) + ".tfn", "w")
            output.write("input x\n\n")
            output.write("// Auto-generated code for function assign" + str(i) + "\n")
            output.write("// Assigns x to the value " + str(i) + "\n")
            output.write("// Unary assumed\n")
            output.write("function assign" + str(i-1) + " x\n")
            output.write("function add1 x\n")
            output.write("return\n")
            
if __name__ == "__main__":
    writeAssignsUpToX(int(sys.argv[1]))