# TJ Baesman
# CSCI 102 - Section E
# Week 12



def PrintOutput(inputString):
    print("OUTPUT", inputString)

def LoadFile(filename):
    file = open(filename)
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][0:len(lines[i])-1]
    return lines


