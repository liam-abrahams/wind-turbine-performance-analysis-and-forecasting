import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import timedelta

def plot_timeseries_single(df, x_column, y_column, y_label, title, xticks=None):
    '''
    Simple time series plotter for fleet / one turbine.
    (x_column will always be dates, y_column will be the variable and xticks must be a date range).
    '''
    fig, ax = plt.subplots(figsize=(15,5))

    ax.plot(df[x_column], df[y_column], label=y_column, color='skyblue')

    if xticks is not None:
        for i, start in enumerate(xticks[:-1]):
            end = xticks[i+1]
            if i % 2 == 0:
                ax.axvspan(start, end, color='lightgrey', alpha=0.25)
        
        ax.set_xticks(xticks)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.xticks(rotation=45)
    
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.25)

    plt.tight_layout()

    return fig, ax

def plot_timeseries_multiple(df, x_column, y_column, turbines, y_label, title, xticks=None):
    '''
    Simple time series plotter for multiple turbines.
    (x_column will always be dates, y_column will be the variable.
    turbines is a list of turbines named: WTGXX and ranging from WTG01 to WTG04. Finally, xticks must be a date range).
    '''
    n = len(turbines)
    fig, axes = plt.subplots(n, 1, figsize=(15, 3*n), sharex=True)

    if n == 1:
        axes = [axes]
    
    for ax, wtg in zip(axes, turbines):
        df_subset = df[df["WTG"] == wtg]
        ax.plot(df_subset[x_column], df_subset[y_column], label=wtg, color='skyblue')
        if xticks is not None:
            for i, start in enumerate(xticks[:-1]):
                end = xticks[i+1]
                if i % 2 == 0:
                    ax.axvspan(start, end, color='lightgrey', alpha=0.25)
        
        ax.set_ylabel(y_label)
        ax.set_title(wtg)
        ax.grid(True, alpha=0.25)

    if xticks is not None:
        axes[-1].set_xticks(xticks)
        axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        axes[-1].tick_params(axis='x', rotation=45)

    plt.tight_layout()

    return fig, axes