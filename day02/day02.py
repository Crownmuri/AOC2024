#Day 2
from collections import Counter
import numpy as np

def getSafeReports():
    # Open the file in read mode 
    with open('input.txt', 'r') as file: 
        # Read lines from the file 
        lines = file.readlines() 
 
    # Convert the lines to numbers 
    numbers = [line.strip() for line in lines] 
    numberslol = np.asarray([s.split(' ') for s in numbers])
    safereport = 0
    unsafereport = []
    for row in numberslol:
        row = list(map(int,row))
        rowd = np.diff(row)
        if np.all(rowd != 0) and np.all(rowd <= -1) and np.all(rowd >= -3) or np.all(rowd >= 1) and np.all(rowd <= 3):
            safereport+=1
#        if np.all(rowd == 0) or np.any(rowd <= -4) or np.any(rowd >= 4): # Dunno how to solve this yet for star #2
#            unsafereport.append(rowd)
#            print (rowd)
    print (safereport) # Star Get        
#    print (unsafereport)            
    
getSafeReports()
