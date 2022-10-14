import json
import gzip

with gzip.open("../../Downloads/ALL/galaxy_1month.json.gz", 'r') as allSystemsFile:
    numOfLine = 0
    prevNumOfLine = 1
    maxNumOfStars = 0
    for byteLine in allSystemsFile:
        numOfLine += 1
        line = byteLine.decode("utf-8")
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
            for body in bodies:
                if body["type"] == 'Star':
                    numOfStars += 1

            if numOfStars == maxNumOfStars:
                with open("systems3.txt", 'a') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfStars) + '$\n')
            if numOfStars > maxNumOfStars:
                maxNumOfStars = numOfStars
                print(maxNumOfStars, numOfLine)
                with open("systems3.txt", 'w') as systemsFile:
                    systemsFile.write(name + ' $' + str(numOfStars) + '$\n')

        if numOfLine == prevNumOfLine * 2:
            prevNumOfLine *= 2
            print(numOfLine)