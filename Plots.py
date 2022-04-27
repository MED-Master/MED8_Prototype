import seaborn as sns
import pandas as pd
import os
from matplotlib import rc
import matplotlib.pyplot as plt
import time
from datetime import datetime

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

    @staticmethod
    def linePlot(x, y, hue, style, data, folder):
        plot = sns.lineplot(
            x=x,
            y=y,
            hue=hue,
            style=style,
            data=data)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()



    def boxPlot(self, x, y, data, i):
        plot = sns.boxplot(
            x=x,
            y=y,
            data=data)
        FigureID = self.bassFolder + str(i) + 'figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()
        plotting.i += 1

    def dnt_barplot_bycountry(x, y, data, folder):
        barplot_dat = pd.DataFrame(data)
        barplot_dat = barplot_dat[barplot_dat["Dates"]=="2022 Q1"]
        barplot_dat.groupby("Country").mean()
        plot = sns.barplot(
            x=x,
            y=y,
            data=barplot_dat,
            color="b",
            ci=None
        )
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()



#plotting.boxPlot("Country","DNT (Mean)", plotting.df, plotting.i)




