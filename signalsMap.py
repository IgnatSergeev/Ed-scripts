import json
import gzip
import plotly.graph_objs as graphObj
from plotly.subplots import make_subplots


def returnX(list):
    X = []
    for el in list:
        X.append(el[0])
    return X
def returnY(list):
    Y = []
    for el in list:
        Y.append(el[1])
    return Y


HumanSignalsSystemsCoords = []
GuardianSignalsSystemsCoords = []
ThargoidSignalsSystemsCoords = []
OtherSignalsSystemsCoords = []
with gzip.open("E:\Elite galaxy map\galaxy.json.gz", 'r') as allSystemsFile:
    numOfLine = 0
    prevNumOfLine = 1
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
            for body in bodies:
                if body["type"] == 'Planet':
                    if not("gas giant" in body["subType"]):
                        if "signals" in body.keys():
                            for signal in body["signals"]["signals"]:
                                differentSignals.add(signal)
                                if signal == "$SAA_SignalType_Human;":
                                    coords = jsonObj["info"]["coords"]
                                    HumanSignalsSystemsCoords.append([int(coords["x"]),int(coords["y"]), int(coords["z"])])

                                if signal == "$SAA_SignalType_Guardian;":
                                    coords = jsonObj["info"]["coords"]
                                    GuardianSignalsSystemsCoords.append([int(coords["x"]),int(coords["y"]), int(coords["z"])])

                                if signal == "$SAA_SignalType_Other;":
                                    coords = jsonObj["info"]["coords"]
                                    OtherSignalsSystemsCoords.append([int(coords["x"]),int(coords["y"]), int(coords["z"])])

                                if signal == "$SAA_SignalType_Thargoid;":
                                    coords = jsonObj["info"]["coords"]
                                    ThargoidSignalsSystemsCoords.append([int(coords["x"]),int(coords["y"]), int(coords["z"])])


        if numOfLine == prevNumOfLine * 2:
            prevNumOfLine *= 2
            print(numOfLine)
    print(differentSignals)
with open("allDataFiles/HumanSignalsSystemsCoords.txt", 'w') as HumanSignalsSystemsCoordsFile:
    HumanSignalsSystemsCoordsFile.write(str(HumanSignalsSystemsCoords))
with open("allDataFiles/ThargoidSignalsSystemsCoords.txt", 'w') as ThargoidSignalsSystemsCoordsFile:
    ThargoidSignalsSystemsCoordsFile.write(str(ThargoidSignalsSystemsCoords))
with open("allDataFiles/OtherSignalsSystemsCoords.txt", 'w') as OtherSignalsSystemsCoordsFile:
    OtherSignalsSystemsCoordsFile.write(str(OtherSignalsSystemsCoords))
with open("allDataFiles/GuardianSignalsSystemsCoords.txt", 'w') as GuardianSignalsSystemsCoordsFile:
    GuardianSignalsSystemsCoordsFile.write(str(GuardianSignalsSystemsCoords))

fig = make_subplots(rows=2, cols=2)
fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='White')
fig.add_trace(graphObj.Scatter(x = returnX(HumanSignalsSystemsCoords), y = returnY(HumanSignalsSystemsCoords), mode='markers', name='Human'), 1, 1)
fig.add_trace(graphObj.Scatter(x = returnX(ThargoidSignalsSystemsCoords), y = returnY(ThargoidSignalsSystemsCoords), mode='markers',  name='Thargoid'), 1, 2)
fig.add_trace(graphObj.Scatter(x = returnX(OtherSignalsSystemsCoords), y = returnY(OtherSignalsSystemsCoords), mode='markers',  name='Other'), 2, 1)
fig.add_trace(graphObj.Scatter(x = returnX(GuardianSignalsSystemsCoords), y = returnY(GuardianSignalsSystemsCoords), mode='markers',  name='Guardians'), 2, 2)
fig.show()