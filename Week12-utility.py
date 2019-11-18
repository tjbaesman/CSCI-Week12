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

def UpdateString(string, substring, IDX):
    PrintOutput(string[0:IDX] + substring + string[IDX+len(substring):len(string)])

def FindWordCount(listOfLines, string):
    counter = 0
    for i in listOfLines:
        for j in range(len(i)-len(string)):
            if i[j:j+len(string)].lower() == string.lower():
                counter += 1
    return counter

