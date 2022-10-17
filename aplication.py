import plotly
import plotly.graph_objs as graphObj
import plotly.express as PlotExpr
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

x1 = [[256, 23], [-23, 890]]
x2 = [[256, 23], [-23, 890]]
def returnX(list):
    Xes = []
    for el in list:
        Xes.append(el[0])
    return Xes
def returnY(list):
    Yes = []
    for el in list:
        Yes.append(el[1])
    return Yes
print(str(x1))
fig = make_subplots(rows=1, cols=2)
fig.update_yaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='Black')
fig.update_xaxes(range=[-0.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='White')
fig.add_trace(graphObj.Scatter(x = returnX(x1), y = returnY(x1), mode='markers',  name='Thargoid'), 1, 2)
fig.add_trace(graphObj.Scatter(x = returnX(x2), y = returnY(x2), mode='markers', name='Human'), 1, 1)
fig.show()