import json
import gzip

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

            if numOfBodies == maxNumOfBodies:
                with open("bodies.txt", 'a') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfBodies) + '$\n')
            if numOfBodies > maxNumOfBodies:
                maxNumOfBodies = numOfBodies
                print("Max num of bodies = ", maxNumOfBodies, numOfLine)
                with open("bodies.txt", 'w') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfBodies) + '$\n')

            if numOfStars == maxNumOfStars:
                with open("systems3.txt", 'a') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfStars) + '$\n')
            if numOfStars > maxNumOfStars:
                maxNumOfStars = numOfStars
                print("Max num of stars = ",maxNumOfStars, numOfLine)
                with open("systems3.txt", 'w') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfStars) + '$\n')

        if numOfLine == prevNumOfLine * 2:
            prevNumOfLine *= 2
            print(numOfLine)