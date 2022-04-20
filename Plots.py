import seaborn as sns
import pandas as pd
import os
from matplotlib import rc
import matplotlib.pyplot as plt

class plotting():
    #if not os.path.exists("images"):
    #    os.mkdir("images")

    #data
    df = pd.read_csv("Data.csv")
    #print control
    i = 1

    #Export settings
    sns.set_theme(style="darkgrid")
    sns.set(rc={"figure.figsize":(17, 10)}) #width, height
    plt.rcParams['axes.grid'] = True
    plt.rcParams['savefig.transparent'] = True



    # Plot the responses for different events and regions
    def linePlot(x, y, hue, style, data, i):
        plot = sns.lineplot(
            x=x,
            y=y,
            hue=hue,
            style=style,
            data=data)
        FigureID = 'images/' + str(i) + 'figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()
        plotting.i += 1



    def boxPlot(x, y, data, i):
        plot = sns.boxplot(
            x=x,
            y=y,
            data=data)
        FigureID = 'images/' + str(i) + 'figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()
        plotting.i += 1




#plotting.boxPlot("Country","DNT (Mean)", plotting.df, plotting.i)




