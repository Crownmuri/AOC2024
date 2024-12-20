#Day 4
import re

def getXMAS():
    # Open the file in read mode 
    with open('input.txt', 'r') as file: 
        # Read lines from the file 
        output = file.read()

#    print (output)
    XMAS46 = len(re.findall("XMAS",output))
    XMAS82 = len(re.findall("(?=(X[A-Z\n.]{140}M[A-Z\n.]{140}A[A-Z\n.]{140}S))",output))
    XMAS91 = len(re.findall("(?=(X[A-Z\n.]{139}M[A-Z\n.]{139}A[A-Z\n.]{139}S))",output))
    XMAS73 = len(re.findall("(?=(X[A-Z\n.]{141}M[A-Z\n.]{141}A[A-Z\n.]{141}S))",output))
    XMAS64 = len(re.findall("SAMX",output))
    XMAS28 = len(re.findall("(?=(S[A-Z\n.]{140}A[A-Z\n.]{140}M[A-Z\n.]{140}X))",output))
    XMAS19 = len(re.findall("(?=(S[A-Z\n.]{139}A[A-Z\n.]{139}M[A-Z\n.]{139}X))",output))
    XMAS37 = len(re.findall("(?=(S[A-Z\n.]{141}A[A-Z\n.]{141}M[A-Z\n.]{141}X))",output))
    XMAScount = XMAS46+XMAS82+XMAS91+XMAS73+XMAS64+XMAS28+XMAS19+XMAS37
    print (XMAScount) # Star Get
    MSAMS = len(re.findall("(?=(M[A-Z]{1}S[A-Z\n.]{139}A[A-Z\n.]{139}M[A-Z]{1}S))",output))
    MMASS = len(re.findall("(?=(M[A-Z]{1}M[A-Z\n.]{139}A[A-Z\n.]{139}S[A-Z]{1}S))",output))
    SSAMM = len(re.findall("(?=(S[A-Z]{1}S[A-Z\n.]{139}A[A-Z\n.]{139}M[A-Z]{1}M))",output))
    SMASM = len(re.findall("(?=(S[A-Z]{1}M[A-Z\n.]{139}A[A-Z\n.]{139}S[A-Z]{1}M))",output))
    MAScount = MSAMS + MMASS + SSAMM + SMASM
    print (MAScount) # Star Get
    
getXMAS()
