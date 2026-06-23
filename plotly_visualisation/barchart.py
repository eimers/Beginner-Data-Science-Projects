import plotly.express as px
import numpy as np

# Exemple de données simulées
categories = ["Python", "JavaScript", "C++", "Java", "R"]
values = np.random.randint(10, 100, size=len(categories))

# Création du bar chart futuriste
fig = px.bar(
    x=categories,
    y=values,
    title="🚀 Futuristic Bar Chart",
    color=values,
    color_continuous_scale="Viridis",  # palette moderne et futuriste
    template="plotly_dark",  # style sombre cyberpunk
)

# Options interactives
fig.update_layout(
    font=dict(size=16, color="cyan"),
    plot_bgcolor="black",
    paper_bgcolor="black",
    title_font=dict(size=22, color="magenta"),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
)

fig.show()
