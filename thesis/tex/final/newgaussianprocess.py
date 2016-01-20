import numpy as np
import matplotlib.pyplot as p

n = 21

def getNextValue(prevValue, var):
    return np.random.normal(prevValue, var)
    
waveform = [0]    

for i in range(n):
    waveform.append(getNextValue(waveform[-1], 1))
    
p.plot(range(n), waveform)

p.show()