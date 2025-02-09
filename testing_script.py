import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv("./players_data.csv")

fwd_df = df[df["position"] == 'Forward']

fwd_points = fwd_df.sort_values('total_points', ascending = False).head(10)[::-1]


fig = px.bar(fwd_points, x = "total_points", y = "second_name", orientation = 'h')



def plot_top_players(df):

    plt.figure(figsize = (10, 7))
    plt.barh(df["second_name"], df["total_points"])
    plt.show()




def plot_top_players(df, position, metric):

    position_df = df[df["position"] == position]

    metric_df = position_df.sort_values(metric, ascending = False).head(10)[::-1]

    fig = px.bar(metric_df, x = metric, y = "second_name", orientation = "h")

    return fig



