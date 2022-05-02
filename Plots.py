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
    plt.rcParams['grid.color'] = "#DCDCDC"
    plt.rcParams['savefig.transparent'] = True



    # Plot the responses for different events and regions

    @staticmethod
    def dnt_barplot_bycountry(x, y, data, folder, title):
        barplot_dat = pd.DataFrame(data)
        barplot_dat = barplot_dat[barplot_dat["Dates"] == "2022 Q1"]
        barplot_dat.groupby("Country").mean()
        if (x == "Hospitals"):
            barplot_dat = barplot_dat[barplot_dat["Countries"] == "France" and barplot_dat["Countries"] == "Lyon" ]
        plot = sns.barplot(
            x=x,
            y=y,
            data=barplot_dat,
            palette=["grey" if (x!="France") and (x!="Lyon") else "b" if (x=="France") else "orange" for
                     x in barplot_dat.Country],
            ci=None
        )
        plot.set_title(title, y =0.97, fontdict= {'fontsize': 24, 'fontweight':'bold'})
        for p in plot.patches:
            plot.annotate(format(p.get_height(), '.1f'),
                           (p.get_x() + p.get_width() / 2., p.get_height()),
                           ha='center', va='center',
                           size=15,
                           xytext=(0, -20),
                           textcoords='offset points',
                           fontsize=10,)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()


    def dnt_timeline(self, x, y, data, folder, title, plot_filter=None, filter_category=None):
        plot = self.create_timeline_plot(x, y, data, plot_filter, filter_category)
        plot.set_title(title, y =0.97, fontdict= {'fontsize': 24, 'fontweight':'bold'})
        plt.ylim(min(data[y]), max(data[y]) + 10)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    def annotate_timeline_event(self, x, y, data, folder, plot_filter=None, filter_category=None):
        plot = self.create_timeline_plot(x, y, data, plot_filter, filter_category)
        plot.set_title("Mean DNT over time with international hospitals", y =0.97, fontdict= {'fontsize': 24, 'fontweight':'bold'})
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
        plt.ylim(min(data[y]), max(data[y]) + 10)
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

        palette = {c: 'orange' if c == 'Lyon' else (0, 0.5, 1, 0.3) if c == "France" else (0.8, 0.8, 0.8, 0.3) for c in
                   timeline_dat.Country.unique()}

        plot = sns.lineplot(
            x=x,
            y=y,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False,
            linewidth=3)

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
                          xytext=(4, 4),
                          color="#000000",
                          xycoords=(plot.get_xaxis_transform(),
                                    plot.get_yaxis_transform()),
                          textcoords="offset points")
        return plot

    @staticmethod
    def create_international_timeline_plot(x, y, data, folder, title, plot_filter=None, filter_category=None, annotate=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        palette = {c: 'orange' if c == 'Lyon' else (0, 0.5, 1, 0.3) if c == "France" else (0.8, 0.8, 0.8, 0.3) for c in
                   timeline_dat.Country.unique()}

        plot = sns.lineplot(
            x=x,
            y=y,
            hue="Country",
            style="Country",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ci=None,
            linewidth=3)
        plot.grid(axis='x')
        plt.ylim(min(timeline_dat[y]), max(timeline_dat[y]) + 10)
        plot.set_title(title, y =0.97, fontdict= {'fontsize': 24, 'fontweight':'bold'})

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
                          color="#000000",
                          xycoords=(plot.get_xaxis_transform(),
                                    plot.get_yaxis_transform()),
                          textcoords="offset points")

        if annotate == True:
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
            ci=None,
            linewidth=3)
        plot.set_title("Patient Intake compared to Discharge", y =0.97, fontdict= {'fontsize': 24, 'fontweight':'bold'})
        plot2 = sns.lineplot(
            x=x,
            y=y2,
            color="b",
            data=timeline_dat,
            legend=False,
            ci=None,
            linewidth=3).grid(axis="x")
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
                          color="#000000",
                          xycoords=(plot.get_xaxis_transform(),
                                    plot.get_yaxis_transform()),
                          textcoords="offset points")
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

    @staticmethod
    def Plot_InVsOut_notcombined_local(x_axis, y, y2, data, folder, plot_filter=None, filter_category=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        palette = {c: 'orange' if c == 'Lyon' else (0, 0.5, 1, 0.3) if c == "France" else (0.8, 0.8, 0.8, 0.3) for c in
                   timeline_dat.Country.unique()}
        fig, axs = plt.subplots(ncols=2)
        sns.lineplot(
            x=x_axis,
            y=y,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ax=axs[0],
            linewidth=3)
        axs[0].grid(axis='x')
        for ind, label in enumerate(axs[0].get_xticklabels()):
            if ind % 4 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)
        names = timeline_dat.groupby("Country")["Hospital"].apply(lambda x: list(np.unique(x)))
        name_array = []
        for i in names:
            for j in i:
                name_array.append(j)
        for line, name in zip(axs[0].lines, name_array):
            y = line.get_ydata()[-1]
            x = line.get_xdata()[-1]
            if not np.isfinite(y):
                y = next(reversed(line.get_ydata()[~line.get_ydata().mask]), float("nan"))
            if not np.isfinite(y) or not np.isfinite(x):
                continue
            axs[0].annotate(name,
                          xy=(x, y),
                          xytext=(0, 0),
                          color="#000000",
                          xycoords=(axs[0].get_xaxis_transform(),
                                    axs[0].get_yaxis_transform()),
                          textcoords="offset points")
        sns.lineplot(
            x=x_axis,
            y=y2,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ax=axs[1],
            linewidth=3)
        axs[1].grid(axis='x')
        for ind, label in enumerate(axs[1].get_xticklabels()):
            if ind % 4 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)
        names = timeline_dat.groupby("Country")["Hospital"].apply(lambda x: list(np.unique(x)))
        name_array = []
        for i in names:
            for j in i:
                name_array.append(j)
        for line, name in zip(axs[1].lines, name_array):
            y = line.get_ydata()[-1]
            x = line.get_xdata()[-1]
            if not np.isfinite(y):
                y = next(reversed(line.get_ydata()[~line.get_ydata().mask]), float("nan"))
            if not np.isfinite(y) or not np.isfinite(x):
                continue
            axs[1].annotate(name,
                            xy=(x, y),
                            xytext=(0, 0),
                            color="#000000",
                            xycoords=(axs[1].get_xaxis_transform(),
                                      axs[1].get_yaxis_transform()),
                            textcoords="offset points")
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plt.savefig(FigureID)
        plt.clf()

    @staticmethod
    def Plot_InVsOut_notcombined_international(x_axis, y, y2, data, folder, plot_filter=None, filter_category=None):
        timeline_dat = pd.DataFrame(data)

        if plot_filter is not None:
            timeline_dat = timeline_dat[timeline_dat[filter_category].isin(plot_filter)]

        palette = {c: 'orange' if c == 'Lyon' else (0, 0.5, 1, 0.3) if c == "France" else (0.8, 0.8, 0.8, 0.3) for c in
                   timeline_dat.Country.unique()}
        fig, axs = plt.subplots(ncols=2)
        sns.lineplot(
            x=x_axis,
            y=y,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ax=axs[0],
            linewidth=3)
        axs[0].grid(axis='x')
        for ind, label in enumerate(axs[0].get_xticklabels()):
            if ind % 4 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)
        names = timeline_dat.groupby("Country")["Hospital"].apply(lambda x: list(np.unique(x)))
        name_array = []
        for i in names:
            for j in i:
                name_array.append(j)
        for line, name in zip(axs[0].lines, name_array):
            y = line.get_ydata()[-1]
            x = line.get_xdata()[-1]
            if not np.isfinite(y):
                y = next(reversed(line.get_ydata()[~line.get_ydata().mask]), float("nan"))
            if not np.isfinite(y) or not np.isfinite(x):
                continue
            axs[0].annotate(name,
                            xy=(x, y),
                            xytext=(0, 0),
                            color="#000000",
                            xycoords=(axs[0].get_xaxis_transform(),
                                      axs[0].get_yaxis_transform()),
                            textcoords="offset points")
        sns.lineplot(
            x=x_axis,
            y=y2,
            hue="Country",
            style="Hospital",
            data=timeline_dat,
            palette=palette,
            legend=False,
            ax=axs[1],
            linewidth = 3)
        axs[1].grid(axis='x')
        for ind, label in enumerate(axs[1].get_xticklabels()):
            if ind % 4 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)
        names = timeline_dat.groupby("Country")["Hospital"].apply(lambda x: list(np.unique(x)))
        name_array = []
        for i in names:
            for j in i:
                name_array.append(j)
        for line, name in zip(axs[1].lines, name_array):
            y = line.get_ydata()[-1]
            x = line.get_xdata()[-1]
            if not np.isfinite(y):
                y = next(reversed(line.get_ydata()[~line.get_ydata().mask]), float("nan"))
            if not np.isfinite(y) or not np.isfinite(x):
                continue
            axs[1].annotate(name,
                            xy=(x, y),
                            xytext=(0, 0),
                            color="#000000",
                            xycoords=(axs[1].get_xaxis_transform(),
                                      axs[1].get_yaxis_transform()),
                            textcoords="offset points")

        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plt.savefig(FigureID)
        plt.clf()

    def annotate_goal(self, x, y, data, folder, goal, plot_filter=None, filter_category=None):
        plot = self.create_timeline_plot(x, y, data, plot_filter, filter_category)

        plot.axhline(goal, ls='--', linewidth=3, color='red')
        plot.text(-1,
                  goal + 1,
                  "GOAL",
                  fontsize=18,
                  color="red")
        plt.ylim(min(data[y]), max(data[y]) + 10)
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        FigureID = folder + dt + ' figure.png'
        plot.figure.savefig(FigureID)
        plt.clf()

