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
                           textcoords='offset points',
                           fontsize=10)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()


    def dnt_timeline(self, x, y, data, folder, plot_filter=None, filter_category=None):
        plot = self.create_timeline_plot(x, y, data, plot_filter, filter_category)

        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    def annotate_timeline_event(self, x, y, data, folder, plot_filter=None, filter_category=None):
        plot = self.create_timeline_plot(x, y, data, plot_filter, filter_category)

        plot.axvline('2021 Q1', ls='--', linewidth=3, color='red')
        plot.annotate('Large intake of patients',
                    xy=('2021 Q1', 53),
                    xycoords='data',
                    xytext=(-200, 0),
                    textcoords='offset points',
                    arrowprops=dict(arrowstyle='->', color='black'),
                    ha='center',
                    va='center',
                    fontsize=15)

        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    @staticmethod
    def create_timeline_plot(x, y, data, plot_filter=None, filter_category=None):
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
        name_array = []
        for i in names:
            for j in i:
                name_array.append(j)

        for line, name in zip(plot.lines, name_array):
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
        return plot

    @staticmethod
    def create_international_timeline_plot(x, y, data, folder, plot_filter=None, filter_category=None, annotate=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        palette = {c: 'orange' if c == 'Lyon (your hospital)' else 'b' if c == "France" else "grey" for c in
                   timeline_dat.Country.unique()}
        plot = sns.lineplot(
            x=x,
            y=y,
            hue="Country",
            style="Country",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ci=None)
        plot.grid(axis='x')
        names = timeline_dat.Country.unique()
        for line, name in zip(plot.lines, names):
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

        if annotate:
            plot.axvline('2021 Q1', ls='--', linewidth=3, color='red')
            plot.annotate('Large intake of patients',
                          xy=('2021 Q1', 53),
                          xycoords='data',
                          xytext=(-200, 0),
                          textcoords='offset points',
                          arrowprops=dict(arrowstyle='->', color='black'),
                          ha='center',
                          va='center',
                          fontsize=15)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    def Plot_InVsOut_timeline(self, x, y, y2, data, folder, plot_filter=None, filter_category=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        plot = sns.lineplot(
            x=x,
            y=y,
            color="Red",
            data=timeline_dat,
            legend=False,
            ci=None)

        plot2 = sns.lineplot(
            x=x,
            y=y2,
            color="b",
            data=timeline_dat,
            legend=False,
            ci=None).grid(axis="x")
        plot.set_ylabel("Number of Patients")
        for line, name in zip(plot.lines, ["Patient intake", "Discharge"]):
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



