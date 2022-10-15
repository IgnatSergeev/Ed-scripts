import json
import gzip


def checkIfMaxAndWriteInFile(curNum, maxNum, fileName, numOfLine, curSystemName, fullLine):
    if curNum == maxNum:
        with open("allDataFiles/" + fileName, 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 0
    if curNum > maxNum:
        print(fileName, "= ", curNum, numOfLine)
        with open("allDataFiles/" + fileName, 'w') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 1


def checkIfMinAndWriteInFile(curNum, minNum, fileName, numOfLine, curSystemName, fullLine):
    if curNum == minNum:
        with open("allDataFiles/" + fileName, 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 0
    if curNum < minNum:
        print(fileName, "= ", curNum, numOfLine)
        with open("allDataFiles/" + fileName, 'w') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 1


with gzip.open("E:\Elite galaxy map\galaxy.json.gz", 'r') as allSystemsFile:
    numOfLine = 0
    prevNumOfLine = 1

    maxNumOfStars = 0
    maxNumOfStarsWithSameOrbitAsMainStar = 0

    maxNumOfBodies = 0
    maxNumOfGasGiants = 0
    maxNumOfPlanets = 0

    maxStarTemperature = 0
    minStarTemperature = 0
    maxGasGiantTemperature = 0
    minGasGiantTemperature = 0

    maxGasGiantGravity = 0
    minGasGiantGravity = 0
    maxPlanetGravity = 0
    minPlanetGravity = 0

    maxGasGiantMass = 0
    minGasGiantMass = 0
    maxPlanetMass = 0
    minPlanetMass = 0
    maxStarMass = 0
    minStarMass = 0

    maxGasGiantRadius = 0
    minGasGiantRadius = 0
    maxPlanetRadius = 0
    minPlanetRadius = 0
    maxStarRadius = 0
    minStarRadius = 0

    maxNumOfWaterBasedPlanets = 0
    maxNumOfLandablePlanets = 0
    maxNumOfDifferentResourcesOnPlanet = 0
    maxStackOfMoons = 0
    maxLengthOfTheNameOfLetters = 0
    #maxNumOfMoons = 0
    #maxExpectedValueOfMainTier4RawMaterials = 0
    differentTypesOfBodies = set()

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
            numOfStarsWithSameOrbitAsMainStar = 0
            mainStarOrbitalInclination = 0
            mainStarOrbitalEccentricity = 0

            numOfBodies = 0
            numOfGasGiants = 0
            numOfPlanets = 0

            curMaxStarTemperature = 0
            curMinStarTemperature = 0
            curMaxGasGiantTemperature = 0
            curMinGasGiantTemperature = 0

            curMaxGasGiantGravity = 0
            curMinGasGiantGravity = 0
            curMaxPlanetGravity = 0
            curMinPlanetGravity = 0

            curMaxGasGiantMass = 0
            curMinGasGiantMass = 0
            curMaxPlanetMass = 0
            curMinPlanetMass = 0
            curMaxStarMass = 0
            curMinStarMass = 0

            curMaxGasGiantRadius = 0
            curMinGasGiantRadius = 0
            curMaxPlanetRadius = 0
            curMinPlanetRadius = 0
            curMaxStarRadius = 0
            curMinStarRadius = 0

            numOfWaterBasedPlanets = 0
            numOfLandablePlanets = 0
            curMaxNumOfDifferentResourcesOnPlanet = 0
            curMaxStackOfMoons = 0
            #curMaxNumOfMoons = 0
            curMaxLengthOfTheNameOfLetters = 0
            isPlanetWithAllTier4Materials = False
            planetWithAllTier4MaterialsName = ""
            for body in bodies:
                if body["type"] == 'Star':
                    numOfStars += 1
                    if "orbitalInclination" in body.keys() and "orbitalEccentricity" in body.keys():
                        if body["distanceToArrival"] == 0:
                            mainStarOrbitalInclination = body["orbitalInclination"]
                            mainStarOrbitalEccentricity = body["orbitalEccentricity"]
                            numOfStarsWithSameOrbitAsMainStar += 1
                        else:
                            if body["orbitalInclination"] == mainStarOrbitalInclination \
                                    and body["orbitalEccentricity"] == mainStarOrbitalEccentricity:
                                numOfStarsWithSameOrbitAsMainStar += 1
                    if "solarMasses" in body.keys():
                        if body["solarMasses"] > curMaxStarMass:
                            curMaxStarMass = body["solarMasses"]
                        if body["solarMasses"] < curMinStarMass:
                            curMinStarMass = body["solarMasses"]
                    if "solarRadius" in body.keys():
                        if body["solarRadius"] > curMaxStarRadius:
                            curMaxStarRadius = body["solarRadius"]
                        if body["solarRadius"] < curMinStarRadius:
                            curMinStarRadius = body["solarRadius"]
                    if "surfaceTemperature" in body.keys():
                        if body["surfaceTemperature"] > curMaxStarTemperature:
                            curMaxStarTemperature = body["surfaceTemperature"]
                        if body["surfaceTemperature"] < curMinStarTemperature:
                            curMinStarTemperature = body["surfaceTemperature"]
                elif body["type"] == 'Planet':
                    if "gas giant" in body["subType"]:
                        numOfGasGiants += 1
                        if "earthMasses" in body.keys():
                            if body["earthMasses"] > curMaxGasGiantMass:
                                curMaxGasGiantMass = body["earthMasses"]
                            if body["earthMasses"] < curMinGasGiantMass:
                                curMinGasGiantMass = body["earthMasses"]
                        if "radius" in body.keys():
                            if body["radius"] > curMaxGasGiantRadius:
                                curMaxGasGiantRadius = body["radius"]
                            if body["radius"] < curMinGasGiantRadius:
                                curMinGasGiantRadius = body["radius"]
                        if "gravity" in body.keys():
                            if body["gravity"] > curMaxGasGiantGravity:
                                curMaxGasGiantGravity = body["gravity"]
                            if body["gravity"] < curMinGasGiantGravity:
                                curMinGasGiantGravity = body["gravity"]
                        if "surfaceTemperature" in body.keys():
                            if body["surfaceTemperature"] > curMaxGasGiantTemperature:
                                curMaxGasGiantTemperature = body["surfaceTemperature"]
                            if body["surfaceTemperature"] < curMinGasGiantTemperature:
                                curMinGasGiantTemperature = body["surfaceTemperature"]
                    else:
                        numOfPlanets += 1
                        curStackOfMoons = 0
                        planetName = "".join([body["name"][x] for x in range(len(body["name"])) if x > len(name)]).split()
                        if len(planetName) >= 1:
                            is0Has0digits = True
                            for i in range(1,10):
                                if str(i) in planetName[0]:
                                    is0Has0digits = False
                                    break
                            if is0Has0digits:
                                if len(planetName[0]) > curMaxLengthOfTheNameOfLetters:
                                    curMaxLengthOfTheNameOfLetters = len(planetName[0])
                        if "parents" in body.keys():
                            for parent in body["parents"]:
                                if "Planet" in parent:
                                    curStackOfMoons += 1
                            if curStackOfMoons > curMaxStackOfMoons:
                                curMaxStackOfMoons = curStackOfMoons
                        if "materials" in body.keys():
                            if len(body["materials"]) > curMaxNumOfDifferentResourcesOnPlanet:
                                curMaxNumOfDifferentResourcesOnPlanet = len(body["materials"])
                            if body["subType"] == "High metal content world":
                                if "Yttrium" in body["materials"] and "Polonium" in body["materials"] and \
                                        "Ruthenium" in body["materials"] and "Antimony" in body["materials"] and \
                                        "Tellurium" in body["materials"] and "Technetium" in body["materials"] and \
                                        "Selenium" in body["materials"]:
                                    isPlanetWithAllTier4Materials = True
                                    planetWithAllTier4MaterialsName = body["name"]
                        if body["subType"] == "Water world":
                            numOfWaterBasedPlanets += 1
                        if "isLandable" in body.keys() and body["isLandable"]:
                            numOfLandablePlanets += 1
                        if "earthMasses" in body.keys():
                            if body["earthMasses"] > curMaxPlanetMass:
                                curMaxPlanetMass = body["earthMasses"]
                            if body["earthMasses"] < curMinPlanetMass:
                                curMinPlanetMass = body["earthMasses"]
                        if "radius" in body.keys():
                            if body["radius"] > curMaxPlanetRadius:
                                curMaxPlanetRadius = body["radius"]
                            if body["radius"] < curMinPlanetRadius:
                                curMinPlanetRadius = body["radius"]
                        if "gravity" in body.keys():
                            if body["gravity"] > curMaxPlanetGravity:
                                curMaxPlanetGravity = body["gravity"]
                            if body["gravity"] < curMinPlanetGravity:
                                curMinPlanetGravity = body["gravity"]
                else:
                    if not(body["type"] in differentTypesOfBodies):
                        with open("DifferentTypesOfBodies.txt", 'a') as systemsFile:
                            systemsFile.write(name + ' $' + str(body["type"]) + '$\n')
                            systemsFile.write(line + '\n')
                        differentTypesOfBodies.add(body["type"])

                numOfBodies += 1

            if checkIfMaxAndWriteInFile(numOfBodies, maxNumOfBodies, "maxNumOfBodies.txt", numOfLine, name, line):
                maxNumOfBodies = numOfBodies

            if checkIfMaxAndWriteInFile(numOfStars, maxNumOfStars, "maxNumOfStars.txt", numOfLine, name, line):
                maxNumOfStars = numOfStars

            if checkIfMaxAndWriteInFile(numOfStarsWithSameOrbitAsMainStar, maxNumOfStarsWithSameOrbitAsMainStar, "maxNumOfStarsWithSameOrbitAsMainStar.txt", numOfLine, name, line):
                maxNumOfStarsWithSameOrbitAsMainStar = numOfStarsWithSameOrbitAsMainStar

            if checkIfMaxAndWriteInFile(numOfGasGiants, maxNumOfGasGiants, "maxNumOfGasGiants.txt", numOfLine, name, line):
                maxNumOfGasGiants = numOfGasGiants

            if checkIfMaxAndWriteInFile(numOfPlanets, maxNumOfPlanets, "maxNumOfPlanets.txt", numOfLine, name, line):
                maxNumOfPlanets = numOfPlanets

            if checkIfMaxAndWriteInFile(curMaxStarTemperature, maxStarTemperature, "maxStarTemperature.txt", numOfLine, name, line):
                maxStarTemperature = curMaxStarTemperature

            if checkIfMinAndWriteInFile(curMinStarTemperature, minStarTemperature, "minStarTemperature.txt", numOfLine, name, line):
                minStarTemperature = curMinStarTemperature

            if checkIfMaxAndWriteInFile(curMaxGasGiantTemperature, maxGasGiantTemperature, "maxGasGiantTemperature.txt", numOfLine, name, line):
                maxGasGiantTemperature = curMaxGasGiantTemperature

            if checkIfMinAndWriteInFile(curMinGasGiantTemperature, minGasGiantTemperature, "minGasGiantTemperature.txt", numOfLine, name, line):
                minGasGiantTemperature = curMinGasGiantTemperature

            if checkIfMaxAndWriteInFile(curMaxGasGiantGravity, maxGasGiantGravity, "maxGasGiantGravity.txt", numOfLine, name, line):
                maxGasGiantGravity = curMaxGasGiantGravity

            if checkIfMinAndWriteInFile(curMinGasGiantGravity, minGasGiantGravity, "minGasGiantGravity.txt", numOfLine, name, line):
                minGasGiantGravity = curMinGasGiantGravity

            if checkIfMaxAndWriteInFile(curMaxPlanetGravity, maxPlanetGravity, "maxPlanetGravity.txt", numOfLine, name, line):
                maxPlanetGravity = curMaxPlanetGravity

            if checkIfMinAndWriteInFile(curMinPlanetGravity, minPlanetGravity, "minPlanetGravity.txt", numOfLine, name, line):
                minPlanetGravity = curMinPlanetGravity

            if checkIfMaxAndWriteInFile(curMaxGasGiantMass, maxGasGiantMass, "maxGasGiantMass.txt", numOfLine, name, line):
                maxGasGiantMass = curMaxGasGiantMass

            if checkIfMinAndWriteInFile(curMinGasGiantMass, minGasGiantMass, "minGasGiantMass.txt", numOfLine, name, line):
                minGasGiantMass = curMinGasGiantMass

            if checkIfMaxAndWriteInFile(curMaxPlanetMass, maxPlanetMass, "maxPlanetMass.txt", numOfLine, name, line):
                maxPlanetMass = curMaxPlanetMass

            if checkIfMinAndWriteInFile(curMinPlanetMass, minPlanetMass, "minPlanetMass.txt", numOfLine, name, line):
                minPlanetMass = curMinPlanetMass

            if checkIfMaxAndWriteInFile(curMaxStarMass, maxStarMass, "maxStarMass.txt", numOfLine, name, line):
                maxStarMass = curMaxStarMass

            if checkIfMinAndWriteInFile(curMinStarMass, minStarMass, "minStarMass.txt", numOfLine, name, line):
                minStarMass = curMinStarMass

            if checkIfMaxAndWriteInFile(curMaxGasGiantRadius, maxGasGiantRadius, "maxGasGiantRadius.txt", numOfLine, name, line):
                maxGasGiantRadius = curMaxGasGiantRadius

            if checkIfMinAndWriteInFile(curMinGasGiantRadius, minGasGiantRadius, "minGasGiantRadius.txt", numOfLine, name, line):
                minGasGiantRadius = curMinGasGiantRadius

            if checkIfMaxAndWriteInFile(curMaxPlanetRadius, maxPlanetRadius, "maxPlanetRadius.txt", numOfLine, name, line):
                maxPlanetRadius = curMaxPlanetRadius

            if checkIfMinAndWriteInFile(curMinPlanetRadius, minPlanetRadius, "minPlanetRadius.txt", numOfLine, name, line):
                minPlanetRadius = curMinPlanetRadius

            if checkIfMaxAndWriteInFile(curMaxStarRadius, maxStarRadius, "maxStarRadius.txt", numOfLine, name, line):
                maxStarRadius = curMaxStarRadius

            if checkIfMinAndWriteInFile(curMinStarRadius, minStarRadius, "minStarRadius.txt", numOfLine, name, line):
                minStarRadius = curMinStarRadius

            if checkIfMaxAndWriteInFile(numOfWaterBasedPlanets, maxNumOfWaterBasedPlanets, "maxNumOfWaterBasedPlanets.txt", numOfLine, name, line):
                maxNumOfWaterBasedPlanets = numOfWaterBasedPlanets

            if checkIfMaxAndWriteInFile(numOfLandablePlanets, maxNumOfLandablePlanets, "maxNumOfLandablePlanets.txt", numOfLine, name, line):
                maxNumOfLandablePlanets = numOfLandablePlanets

            if checkIfMaxAndWriteInFile(curMaxNumOfDifferentResourcesOnPlanet, maxNumOfDifferentResourcesOnPlanet, "maxNumOfDifferentResourcesOnPlanet.txt", numOfLine, name, line):
                maxNumOfDifferentResourcesOnPlanet = curMaxNumOfDifferentResourcesOnPlanet

            if checkIfMaxAndWriteInFile(curMaxStackOfMoons, maxStackOfMoons, "maxStackOfMoons.txt", numOfLine, name, line):
                maxStackOfMoons = curMaxStackOfMoons

            if checkIfMaxAndWriteInFile(curMaxLengthOfTheNameOfLetters, maxLengthOfTheNameOfLetters, "maxLengthOfTheNameOfLetters.txt", numOfLine, name, line):
                maxLengthOfTheNameOfLetters = curMaxLengthOfTheNameOfLetters

            if isPlanetWithAllTier4Materials:
                with open("planetsWithAllTier4RawMaterials.txt", 'a') as systemsFile:
                    systemsFile.write(name + ' $' + str(planetWithAllTier4MaterialsName) + '$\n')
                    systemsFile.write(line + '\n')
            #different types of bodies

        if numOfLine == prevNumOfLine * 2:
            prevNumOfLine *= 2
            print(numOfLine)