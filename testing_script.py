import pandas as pd
import numpy as np
import plotly.express as px




player_data = pd.read_csv("./comprehensive_players_data.csv")


fig = px.scatter(player_data, x = 'expected_goal_involvements_per_90', y = 'expected_goals_conceded_per_90')

fig.show()


def plot_scatter_metrics(metric_x, metric_x):

    fig = px.scatter(player_data, x = metric_x, y = metric_y)

    return fig


