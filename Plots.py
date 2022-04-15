import plotly.express as px
import pandas as pd
import plotly.io as pio
import os

if not os.path.exists("images"):
    os.mkdir("images")

df = pd.read_csv("Data.csv")

#df = px.data.gapminder().query("continent=='Oceania'")


fig = px.line(df, x="Dates", y="DNT (Mean)", color='Hospital')

fig.update_layout(
    title_text="First plotly",
    paper_bgcolor = 'rgba(233,233,233, 0)',
    plot_bgcolor = 'rgba(233,233,233, 0)',
    template = "plotly_dark"
)
fig.write_image("images/fig1.png")
fig.show()