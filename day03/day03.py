#Day 3
import re

def getMul():
    # Open the file in read mode 
    with open('input.txt', 'r') as file: 
        # Read lines from the file 
        output = file.read().replace('\n', '')
    regex1 = re.compile("(?<=mul\()([0-9]+),([0-9]+)(?=\))")
    readMul1 = re.findall(regex1,output)
#    print(readMul) # Get X and Y values from mul($1,$2) hits
    Mul1 = 0
    xys = ((type[0], type[1]) for type in readMul1)
    for x, y in xys:
        z = int(x) * int(y)
        Mul1 += z
    print (Mul1) # Star Get
    regex2 = re.compile("(do\(\))|(don't\(\))|(?<=mul\()([0-9]+),([0-9]+)(?=\))")
    readMul2 = re.findall(regex2,output)
#    print(readMul2) # Get DO, DONT, X and Y values from mul($1,$2) hits    
    abcd = ((type[0], type[1], type[2], type[3]) for type in readMul2)
    Mul2 = 0
    w = 1
    for a,b,c,d in abcd:
        if a == "do()":
            w = 1
        if b == "don't()":
            w = 0
        if c == '':
            c = 0
        if d == '':
            d = 0
        e = w * int(c) * int(d)
        Mul2 += e
    print (Mul2) # Star Get
getMul()
