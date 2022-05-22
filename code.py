import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")

AvgRating = df["Avg Rating"].tolist()

graph = pf.create_distplot( [AvgRating] , ["Data"] , show_hist=False)

graph.show()