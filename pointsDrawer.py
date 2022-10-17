import plotly.graph_objs as graphObj
from plotly.subplots import make_subplots
import ast

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
    OtherSignalsSystemsCoords = [[x[0] - sagittarus[0], x[1] - sagittarus[1], x[2] - sagittarus[2]] for x in
                                 OtherSignalsSystemsCoords]
with open("allDataFiles/HumanSignalsSystemsCoords.txt", 'r') as HumanSignalsSystemsCoordsFile:
    HumanSignalsSystemsCoordsString = HumanSignalsSystemsCoordsFile.readline()
    HumanSignalsSystemsCoords = ast.literal_eval(HumanSignalsSystemsCoordsString)
    HumanSignalsSystemsCoords = [[x[0] - sagittarus[0], x[1] - sagittarus[1], x[2] - sagittarus[2]] for x in HumanSignalsSystemsCoords]
with open("allDataFiles/ThargoidSignalsSystemsCoords.txt", 'r') as ThargoidSignalsSystemsCoordsFile:
    ThargoidSignalsSystemsCoordsString = ThargoidSignalsSystemsCoordsFile.readline()
    ThargoidSignalsSystemsCoords = ast.literal_eval(ThargoidSignalsSystemsCoordsString)
    ThargoidSignalsSystemsCoords = [[x[0] - sagittarus[0], x[1] - sagittarus[1], x[2] - sagittarus[2]] for x in
                                 ThargoidSignalsSystemsCoords]
with open("allDataFiles/GuardianSignalsSystemsCoords.txt", 'r') as GuardianSignalsSystemsCoordsFile:
    GuardianSignalsSystemsCoordsString = GuardianSignalsSystemsCoordsFile.readline()
    GuardianSignalsSystemsCoords = ast.literal_eval(GuardianSignalsSystemsCoordsString)
    GuardianSignalsSystemsCoords = [[x[0] - sagittarus[0], x[1] - sagittarus[1], x[2] - sagittarus[2]] for x in
                                 GuardianSignalsSystemsCoords]

fig = make_subplots(rows=2, cols=2)
fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='White')
#fig.add_trace(graphObj.Scatter(x = returnX(HumanSignalsSystemsCoords), y = returnY(HumanSignalsSystemsCoords), mode='markers', name='Human'), 1, 1)
fig.add_trace(graphObj.Scatter(x = returnX(ThargoidSignalsSystemsCoords), y = returnY(ThargoidSignalsSystemsCoords), mode='markers',  name='Thargoid'), 1, 2)
fig.add_layout_image(dict(source = "https://static.wikia.nocookie.net/elite-dangerous/images/a/aa/Elite-Dangerous-Codex-Galaxy-Regions.png/revision/latest?cb=20190505073219",
            xref="x",
            yref="y",
            x=0,
            y=0,
            sizex=4,
            sizey=4,
            sizing="stretch",
            opacity=0.75,
            layer="below"))
fig.update_layout(template="plotly_white")
#fig.add_trace(graphObj.Scatter(x = returnX(OtherSignalsSystemsCoords), y = returnY(OtherSignalsSystemsCoords), mode='markers',  name='Other'), 2, 1)
#fig.add_trace(graphObj.Scatter(x = returnX(GuardianSignalsSystemsCoords), y = returnY(GuardianSignalsSystemsCoords), mode='markers',  name='Guardians'), 2, 2)
fig.show()




