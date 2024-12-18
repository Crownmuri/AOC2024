#Day 1
import numpy as np

def getLocationID():
    with open("input.txt", "r") as f:
        idlist = [line.rstrip('\n') for line in f]
        types = (line.split("   ") for line in idlist)
        xys = ((type[0], type[1]) for type in types)
        lstx = []
        lsty = []
        for x, y in xys:
           x = sorted(x.split())
           y = sorted(y.split())
           lstx.extend(x)
           lsty.extend(y)
        lstx.sort()
        lsty.sort()
        array1 = np.array(lstx).astype(int)
        array2 = np.array(lsty).astype(int)
        array3 = abs(array1 - array2)
        print(sum(array3)) # Star Get

                
        arraydiff1 = np.setdiff1d(array1,array2)
        arraydiff2 = np.setdiff1d(array2,array1)
        arraydup1 = array1[~np.isin(array1,arraydiff1)]
        arraydup2 = array2[~np.isin(array2,arraydiff2)]
        print(sum(arraydup2)) # Star Get
        
getLocationID()
