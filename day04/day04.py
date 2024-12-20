#Day 4
import re

def getXMAS():
    # Open the file in read mode 
    with open('input.txt', 'r') as file: 
        # Read lines from the file 
        output = file.read().replace('\n', '')

#    print (output)
    XMAS46 = len(re.findall("XMAS",output))
    XMAS82 = len(re.findall("(?=(X[A-Z.]{139}M[A-Z.]{139}A[A-Z.]{139}S))",output))
    XMAS91 = len(re.findall("(?=(X[A-Z.]{138}M[A-Z.]{138}A[A-Z.]{138}S))",output))
    XMAS73 = len(re.findall("(?=(X[A-Z.]{140}M[A-Z.]{140}A[A-Z.]{140}S))",output))
    XMAS64 = len(re.findall("SAMX",output))
    XMAS28 = len(re.findall("(?=(S[A-Z.]{139}A[A-Z.]{139}M[A-Z.]{139}X))",output))
    XMAS19 = len(re.findall("(?=(S[A-Z.]{138}A[A-Z.]{138}M[A-Z.]{138}X))",output))
    XMAS37 = len(re.findall("(?=(S[A-Z.]{140}A[A-Z.]{140}M[A-Z.]{140}X))",output))
    XMAScount = XMAS46+XMAS82+XMAS91+XMAS73+XMAS64+XMAS28+XMAS19+XMAS37
    print (XMAS46) #output 202
    print (XMAS82) #output 206
    print (XMAS91) #output 369
    print (XMAS73) #output 408
    print (XMAS64) #output 211
    print (XMAS28) #output 195
    print (XMAS19) #output 417
    print (XMAS37) #output 413
    print (XMAScount) #output 2421? [x]
    
getXMAS()
