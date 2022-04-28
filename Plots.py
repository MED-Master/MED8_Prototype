import seaborn as sns
import pandas as pd
import os
from matplotlib import rc
import matplotlib.pyplot as plt
import time
from datetime import datetime
import numpy as np

class plotting():
    #if not os.path.exists("images"):
    #    os.mkdir("images")

    #data
    df = pd.read_csv("Data.csv")
    #print control
    i = 1

    #Export settings
    sns.set_theme(style="whitegrid")
    sns.set(rc={"figure.figsize":(17, 10)}) #width, height
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.color'] = "#000000"
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

    @staticmethod
    def dnt_barplot_bycountry(x, y, data, folder):
        barplot_dat = pd.DataFrame(data)
        barplot_dat = barplot_dat[barplot_dat["Dates"] == "2022 Q1"]
        barplot_dat.groupby("Country").mean()
        plot = sns.barplot(
            x=x,
            y=y,
            data=barplot_dat,
            palette=["grey" if (x!="France") and (x!="Lyon (your hospital)") else "b" if (x=="France") else "orange" for
                     x in barplot_dat.Country],
            ci=None
        )
        for p in plot.patches:
            plot.annotate(format(p.get_height(), '.1f'),
                           (p.get_x() + p.get_width() / 2., p.get_height()),
                           ha='center', va='center',
                           size=15,
                           xytext=(0, -20),
                           textcoords='offset points')
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    @staticmethod
    def dnt_timeline(x, y, data, folder, plot_filter=None, filter_category=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        palette = {c: 'orange' if c == 'Lyon (your hospital)' else 'b' if c == "France" else "grey" for c in
                   timeline_dat.Country.unique()}
        plot = sns.lineplot(
            x=x,
            y=y,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False)
        plot.grid(axis='x')
        names = timeline_dat.groupby("Country")["Hospital"].apply(lambda x: list(np.unique(x)))
        mysanity = []
        for test in names:
            for test2 in test:
                mysanity.append(test2)

        for line, name in zip(plot.lines, mysanity):
            y = line.get_ydata()[-1]
            x = line.get_xdata()[-1]
            if not np.isfinite(y):
                y = next(reversed(line.get_ydata()[~line.get_ydata().mask]), float("nan"))
            if not np.isfinite(y) or not np.isfinite(x):
                continue
            plot.annotate(name,
                          xy=(x, y),
                          xytext=(0, 0),
                          color=line.get_color(),
                          xycoords=(plot.get_xaxis_transform(),
                                    plot.get_yaxis_transform()),
                                    textcoords="offset points")

        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

#plotting.boxPlot("Country","DNT (Mean)", plotting.df, plotting.i)




