import json
import gzip


def checkIfMaxAndWriteInFile(curNum, maxNum, fileName, numOfLine, curSystemName, fullLine):
    if fileName == "maxLengthOfTheNameOfLetters.txt" and curNum >= 6:
        with open("allDataFiles/maxLengthOfTheNameOfLettersWithMoreTHan6Characters.txt", 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
    if fileName == "maxNumOfStars.txt" and curNum >= 20:
        with open("allDataFiles/maxNumOfStarsWithMoreThan20Stars.txt", 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
    if curNum == maxNum:
        with open("allDataFiles/" + fileName, 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
        return 0
    if curNum > maxNum:
        print(fileName, "= ", curNum, numOfLine)
        with open("allDataFiles/" + fileName, 'w') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 1
    return 0


def checkIfMinAndWriteInFile(curNum, minNum, fileName, numOfLine, curSystemName, fullLine):
    if curNum != -1 and curNum == minNum:
        with open("allDataFiles/" + fileName, 'a') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
        return 0
    if curNum != -1 and (curNum < minNum or minNum == -1):
        print(fileName, "= ", curNum, numOfLine)
        with open("allDataFiles/" + fileName, 'w') as systemsFile:
            systemsFile.write(curSystemName + ' $' + str(curNum) + '$\n')
            systemsFile.write(fullLine + '\n')
        return 1
    return 0


with gzip.open("E:\Elite galaxy map\galaxy.json.gz", 'r') as allSystemsFile:
    numOfLine = 0
    prevNumOfLine = 1

    maxNumOfStars = 0
    maxNumOfStarsWithSameOrbitAsMainStar = 0

    maxNumOfBodies = 0
    maxNumOfGasGiants = 0
    maxNumOfPlanets = 0

    maxStarTemperature = 0
    minStarTemperature = -1
    maxGasGiantTemperature = 0
    minGasGiantTemperature = -1

    maxGasGiantGravity = 0
    minGasGiantGravity = -1
    maxPlanetGravity = 0
    minPlanetGravity = -1

    maxGasGiantMass = 0
    minGasGiantMass = -1
    maxPlanetMass = 0
    minPlanetMass = -1
    maxStarMass = 0
    minStarMass = -1

    maxGasGiantRadius = 0
    minGasGiantRadius = -1
    maxPlanetRadius = 0
    minPlanetRadius = -1
    minLandablePlanetRadius = -1
    minLandablePlanetRadiusNotEqualTo0 = -1
    maxStarRadius = 0
    minStarRadius = -1

    maxNumOfWaterBasedPlanets = 0
    maxNumOfLandablePlanets = 0
    maxNumOfDifferentResourcesOnPlanet = 0
    maxStackOfMoons = 0
    maxLengthOfTheNameOfLetters = 0
    #maxNumOfMoons = 0
    #maxExpectedValueOfMainTier4RawMaterials = 0
    differentTypesOfBodies = set()
    differentSignals = set()
    for byteLine in allSystemsFile:
        numOfLine += 1
        line = byteLine.decode("utf-8")

        if numOfLine > 1:
            try:
                jsonObj = json.loads('{ "info":' + line + '"empty":0}')
            except:
                try:
                    jsonObj = json.loads('{ "info":' + line + '}')
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
            curMinStarTemperature = -1
            curMaxGasGiantTemperature = 0
            curMinGasGiantTemperature = -1

            curMaxGasGiantGravity = 0
            curMinGasGiantGravity = -1
            curMaxPlanetGravity = 0
            curMinPlanetGravity = -1

            curMaxGasGiantMass = 0
            curMinGasGiantMass = -1
            curMaxPlanetMass = 0
            curMinPlanetMass = -1
            curMaxStarMass = 0
            curMinStarMass = -1

            curMaxGasGiantRadius = 0
            curMinGasGiantRadius = -1
            curMaxPlanetRadius = 0
            curMinPlanetRadius = -1
            curMaxStarRadius = 0
            curMinStarRadius = -1
            curMinLandablePlanetRadius = -1
            curMinLandablePlanetRadiusNotEqualTo0 = -1

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
                        if body["solarMasses"] < curMinStarMass or curMinStarMass == -1:
                            curMinStarMass = body["solarMasses"]
                    if "solarRadius" in body.keys():
                        if body["solarRadius"] > curMaxStarRadius:
                            curMaxStarRadius = body["solarRadius"]
                        if body["solarRadius"] < curMinStarRadius or curMinStarRadius == -1:
                            curMinStarRadius = body["solarRadius"]
                    if "surfaceTemperature" in body.keys():
                        if body["surfaceTemperature"] > curMaxStarTemperature:
                            curMaxStarTemperature = body["surfaceTemperature"]
                        if body["surfaceTemperature"] < curMinStarTemperature or curMinStarTemperature == -1:
                            curMinStarTemperature = body["surfaceTemperature"]

                elif body["type"] == 'Planet':
                    if "gas giant" in body["subType"]:
                        numOfGasGiants += 1

                        if "earthMasses" in body.keys():
                            if body["earthMasses"] > curMaxGasGiantMass:
                                curMaxGasGiantMass = body["earthMasses"]
                            if body["earthMasses"] < curMinGasGiantMass or curMinGasGiantMass == -1:
                                curMinGasGiantMass = body["earthMasses"]
                        if "radius" in body.keys():
                            if body["radius"] > curMaxGasGiantRadius:
                                curMaxGasGiantRadius = body["radius"]
                            if body["radius"] < curMinGasGiantRadius or curMinGasGiantRadius == -1:
                                curMinGasGiantRadius = body["radius"]
                        if "gravity" in body.keys():
                            if body["gravity"] > curMaxGasGiantGravity:
                                curMaxGasGiantGravity = body["gravity"]
                            if body["gravity"] < curMinGasGiantGravity or curMinGasGiantGravity == -1:
                                curMinGasGiantGravity = body["gravity"]
                        if "surfaceTemperature" in body.keys():
                            if body["surfaceTemperature"] > curMaxGasGiantTemperature:
                                curMaxGasGiantTemperature = body["surfaceTemperature"]
                            if body["surfaceTemperature"] < curMinGasGiantTemperature or curMinGasGiantTemperature == -1:
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
                                if len(planetName[0]) > curMaxLengthOfTheNameOfLetters and name in body["name"]:
                                    curMaxLengthOfTheNameOfLetters = len(planetName[0])
                        if "signals" in body.keys():
                            for signal in body["signals"]["signals"]:
                                differentSignals.add(signal)
                                if signal == "$SAA_SignalType_Human;":
                                    with open("allDataFiles/HumanSignals.txt", 'a') as HumanSignalsFile:
                                        HumanSignalsFile.write(name + '(' + body["name"] + ')\n')
                                if signal == "$SAA_SignalType_Guardian;":
                                    with open("allDataFiles/GuardianSignals.txt", 'a') as GuardianSignalsFile:
                                        GuardianSignalsFile.write(name + '(' + body["name"] + ')\n')
                                if signal == "$SAA_SignalType_PlanetAnomaly;":
                                    with open("allDataFiles/PlanetAnomalySignals.txt", 'a') as PlanetAnomalySignalsFile:
                                        PlanetAnomalySignalsFile.write(name + '(' + body["name"] + ')\n')
                                if signal == "$SAA_SignalType_Other;":
                                    with open("allDataFiles/OtherSignals.txt", 'a') as OtherSignalsFile:
                                        OtherSignalsFile.write(name + '(' + body["name"] + ')\n')
                                if signal == "$SAA_SignalType_Thargoid;":
                                    with open("allDataFiles/ThargoidSignals.txt", 'a') as ThargoidSignalsFile:
                                        ThargoidSignalsFile.write(name + '(' + body["name"] + ')\n')
                                if signal == "LowTemperatureDiamond":
                                    with open("allDataFiles/LowTemperatureDiamondSignals.txt", 'a') as LowTemperatureDiamondSignalsFile:
                                        LowTemperatureDiamondSignalsFile.write(name + '(' + body["name"] + ')\n')
                        if "parents" in body.keys():
                            for parent in body["parents"]:
                                if "Planet" in parent:
                                    curStackOfMoons += 1
                            if curStackOfMoons > curMaxStackOfMoons:
                                curMaxStackOfMoons = curStackOfMoons

                        if "materials" in body.keys():
                            if len(body["materials"]) > curMaxNumOfDifferentResourcesOnPlanet:
                                curMaxNumOfDifferentResourcesOnPlanet = len(body["materials"])
                            if body["subType"] == "High metal content world" and numOfLine == 87324391:
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
                            if body["earthMasses"] < curMinPlanetMass or curMinPlanetMass == -1:
                                curMinPlanetMass = body["earthMasses"]
                        if "radius" in body.keys():
                            if body["radius"] > curMaxPlanetRadius:
                                curMaxPlanetRadius = body["radius"]
                            if body["radius"] < curMinPlanetRadius or curMinPlanetRadius == -1:
                                curMinPlanetRadius = body["radius"]
                                if "isLandable" in body.keys() and body["isLandable"] and (body["radius"] < curMinLandablePlanetRadius or curMinLandablePlanetRadius == -1):
                                    curMinLandablePlanetRadius = body["radius"]
                                if "isLandable" in body.keys() and body["isLandable"] and body["radius"] != 0 and (body["radius"] < curMinLandablePlanetRadiusNotEqualTo0 or curMinLandablePlanetRadiusNotEqualTo0 == -1):
                                    curMinLandablePlanetRadiusNotEqualTo0 = body["radius"]

                        if "gravity" in body.keys():
                            if body["gravity"] > curMaxPlanetGravity:
                                curMaxPlanetGravity = body["gravity"]
                            if body["gravity"] < curMinPlanetGravity or curMinPlanetGravity == -1:
                                curMinPlanetGravity = body["gravity"]

                else:
                    if not(body["type"] in differentTypesOfBodies):
                        with open("allDataFiles/DifferentTypesOfBodies.txt", 'a') as systemsFile:
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

            if checkIfMinAndWriteInFile(curMinLandablePlanetRadius, minLandablePlanetRadius, "minLandablePlanetRadius.txt", numOfLine, name, line):
                minLandablePlanetRadius = curMinLandablePlanetRadius

            if checkIfMinAndWriteInFile(curMinLandablePlanetRadiusNotEqualTo0, minLandablePlanetRadiusNotEqualTo0, "minLandablePlanetRadiusNotEqualTo0.txt", numOfLine, name, line):
                minLandablePlanetRadiusNotEqualTo0 = curMinLandablePlanetRadiusNotEqualTo0

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
    print(differentSignals)