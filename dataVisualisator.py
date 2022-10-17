import plotly.graph_objs as graphObj
from plotly.subplots import make_subplots
import plotly.express as PlotExpr
import ast

def centerOfCoords(signalsSystemsCoords):
    numOfCoords = 0
    sumx = 0
    sumy = 0
    for coord in signalsSystemsCoords:
        sumx += coord[0]
        sumy += coord[2]
        numOfCoords += 1
    return [sumx/numOfCoords, sumy/numOfCoords]

def getNames(fileName, signalsSystemsNames):
    with open("allDataFiles/" + fileName, 'r') as File:
        index = 0
        for line in File:
            name = ""
            for x in line:
                if x == '(':
                    break
                name += x
            signalsSystemsNames.append(name)
            index += 1


def returnX(list):
    X = []
    for el in list:
        X.append(el[0])
    return X
def returnY(list):
    Y = []
    for el in list:
        Y.append(el[2])
    return Y

sagittarus = [25.21875,-20.90625,25899.96875]
sol = [0,0,0]
with open("allDataFiles/OtherSignalsSystemsCoords.txt", 'r') as OtherSignalsSystemsCoordsFile:
    OtherSignalsSystemsCoordsString = OtherSignalsSystemsCoordsFile.readline()
    OtherSignalsSystemsCoords = ast.literal_eval(OtherSignalsSystemsCoordsString)

with open("allDataFiles/HumanSignalsSystemsCoords.txt", 'r') as HumanSignalsSystemsCoordsFile:
    HumanSignalsSystemsCoordsString = HumanSignalsSystemsCoordsFile.readline()
    HumanSignalsSystemsCoords = ast.literal_eval(HumanSignalsSystemsCoordsString)

with open("allDataFiles/ThargoidSignalsSystemsCoords.txt", 'r') as ThargoidSignalsSystemsCoordsFile:
    ThargoidSignalsSystemsCoordsString = ThargoidSignalsSystemsCoordsFile.readline()
    ThargoidSignalsSystemsCoords = ast.literal_eval(ThargoidSignalsSystemsCoordsString)

with open("allDataFiles/GuardianSignalsSystemsCoords.txt", 'r') as GuardianSignalsSystemsCoordsFile:
    GuardianSignalsSystemsCoordsString = GuardianSignalsSystemsCoordsFile.readline()
    GuardianSignalsSystemsCoords = ast.literal_eval(GuardianSignalsSystemsCoordsString)


GuardianSignalsSystemsNames = []
getNames("GuardianSignals.txt", GuardianSignalsSystemsNames)
GuardianCenter = centerOfCoords(GuardianSignalsSystemsCoords)

ThargoidSignalsSystemsNames = []
getNames("ThargoidSignals.txt", ThargoidSignalsSystemsNames)
ThargoidCenter = centerOfCoords(ThargoidSignalsSystemsCoords)

HumanSignalsSystemsNames = []
getNames("HumanSignals.txt", HumanSignalsSystemsNames)
HumanCenter = centerOfCoords(HumanSignalsSystemsCoords)

OtherSignalsSystemsNames = []
getNames("OtherSignals.txt", OtherSignalsSystemsNames)
OtherCenter = centerOfCoords(OtherSignalsSystemsCoords)

fig = graphObj.Figure()
fig.update_yaxes(range=[-10, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_xaxes(range=[-10, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='Black')

fig.add_trace(graphObj.Scatter(x = returnX(ThargoidSignalsSystemsCoords), y = returnY(ThargoidSignalsSystemsCoords), mode = "markers", name = "Thargoids", customdata = ThargoidSignalsSystemsNames , hovertemplate="%{customdata}<br>(%{x}, %{y})"))
fig.add_trace(graphObj.Scatter(x = returnX(HumanSignalsSystemsCoords), y = returnY(HumanSignalsSystemsCoords), mode='markers', name='Human', customdata = HumanSignalsSystemsNames , hovertemplate="%{customdata}<br>(%{x}, %{y})"))
fig.add_trace(graphObj.Scatter(x = returnX(OtherSignalsSystemsCoords), y = returnY(OtherSignalsSystemsCoords), mode='markers',  name='Other', customdata = OtherSignalsSystemsNames , hovertemplate="%{customdata}<br>(%{x}, %{y})"))
fig.add_trace(graphObj.Scatter(x = returnX(GuardianSignalsSystemsCoords), y = returnY(GuardianSignalsSystemsCoords), mode='markers',  name='Guardians', customdata = GuardianSignalsSystemsNames , hovertemplate="%{customdata}<br>(%{x}, %{y})"))

fig.add_trace(graphObj.Scatter(x = [0], y = [0], mode = "markers", name = "Sol",  marker = dict(size = 10)))
fig.add_trace(graphObj.Scatter(x = [sagittarus[0]], y = [sagittarus[2]], mode = "markers", name = "Sagittarus A*",  marker = dict(size = 10)))
fig.add_trace(graphObj.Scatter(x = [GuardianCenter[0]], y = [GuardianCenter[1]], mode = "markers", name = "GuardianCenter",  marker = dict(size = 7)))
fig.add_trace(graphObj.Scatter(x = [ThargoidCenter[0]], y = [ThargoidCenter[1]], mode = "markers", name = "ThargoidCenter",  marker = dict(size = 7)))
fig.add_trace(graphObj.Scatter(x = [HumanCenter[0]], y = [HumanCenter[1]], mode = "markers", name = "HumanCenter",  marker = dict(size = 7)))
fig.add_trace(graphObj.Scatter(x = [OtherCenter[0]], y = [OtherCenter[1]], mode = "markers", name = "OtherCenter",  marker = dict(size = 7)))

fig.update_layout(template="plotly_white")
fig.show()




