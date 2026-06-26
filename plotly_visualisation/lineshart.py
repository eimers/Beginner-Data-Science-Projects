import numpy as np
import plotly.express as px

days = ["Monday", "Tuesday", "wensday", "thurday", "friday", "saturday", "sanday"]
score = np.linspace(1, 10, 7)
fig = px.line(x=days, y=score, title="Evolution of score")
fig.show()
