import seaborn as sns
import pandas as pd
import os

if not os.path.exists("images"):
    os.mkdir("images")
#data
df = pd.read_csv("Data.csv")
#Export settings
sns.set_theme(style="darkgrid")
sns.set(rc={"figure.figsize":(19, 8)}) #width=8, height=4

# Plot the responses for different events and regions
plot = sns.lineplot(
    x="Dates",
    y="DNT (Mean)",
    hue="Country",
    style="Hospital",
    data=df
)

plot.figure.savefig('images/save_as_a_png.png')



