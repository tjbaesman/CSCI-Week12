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

def ScoreFinder(nameList, scoreList, name):
    for i in nameList:
        if i.lower() == name.lower():
            PrintOutput(name + " got a score of " + str(scoreList[nameList.index(i)]))
            return
    PrintOutput("player not found")

def Union(list1, list2):
    outList = []
    for i in list1:
        if not(i in list2):
            outList.append(i)
    for j in list2:
        if not(j in list1):
            outList.append(j)
    return outList



            
