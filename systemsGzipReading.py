import json
import gzip

def checkIfMaxAndWriteInFile(curNum, maxNum, fileName, numOfLine, curSystemName):
    if curNum == maxNum:
        with open(fileName, 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
        return 0
    if curNum > maxNum:
        print(fileName, "= ", curNum, numOfLine)
        with open(fileName, 'w') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
        return 1

with gzip.open("E:\Elite galaxy map\galaxy.json.gz", 'r') as allSystemsFile:
    numOfLine = 0
    prevNumOfLine = 1
    maxNumOfStars = 0
    maxNumOfBodies = 0
    for byteLine in allSystemsFile:
        numOfLine += 1
        line = byteLine.decode("utf-8")
        if numOfLine < 10:
            print(line)
        if numOfLine > 1:
            try:
                jsonObj = json.loads('{ "info":' + line + '"empty":0}')
            except:
                print(numOfLine)
                print(line)
                continue
            name = jsonObj["info"]["name"]
            bodies = jsonObj["info"]["bodies"]
            numOfStars = 0
            numOfBodies = 0
            for body in bodies:
                if body["type"] == 'Star':
                    numOfStars += 1
                numOfBodies += 1

            if checkIfMaxAndWriteInFile(numOfBodies, maxNumOfBodies, "SystemsWithMaxNumOfBodies.txt", numOfLine, name):
                maxNumOfBodies = numOfBodies

            if checkIfMaxAndWriteInFile(numOfStars, maxNumOfStars, "SystemsWithMaxNumOfStars.txt", numOfLine, name):
                maxNumOfStars = numOfStars


        if numOfLine == prevNumOfLine * 2:
            prevNumOfLine *= 2
            print(numOfLine)