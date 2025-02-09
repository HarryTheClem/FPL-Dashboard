import numpy as np
import pandas as pd
import dash
from dash import html, dcc, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_csv("./players_data.csv")



dash.register_page(__name__, path = "/")

layout = dbc.Container([
    dbc.Row([
        html.H2("Top player statistics"),
        dbc.Col([html.Br(),
                 html.Br(),
                 html.Label(["Position:"], style= {"font-weight": "bold", "text-align": "center"}),
                 dcc.Dropdown(['Goalkeeper', 'Defender', "Midfielder", 'Forward'], 'Goalkeeper', id = 'position-dropdown'),
                 html.Br(),
                 html.Label(["Metric:"], style = {"font-weight": "bold", "text-align": "center"}),
                 dcc.Dropdown(['total_points', 'value'], 'total_points', id = 'metric-dropdown')], width = 3),

        dbc.Col(dcc.Graph(id = 'top-players-graph'), width = 7),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(id = 'top-players-table'), width = 10)
    ]),

    html.Br(),
    html.Br()

], fluid = True)





@callback(
    Output("top-players-graph", "figure"),
    Input("position-dropdown", "value"),
    Input("metric-dropdown", "value"))
def plot_top_players(position, metric):
    # Set the position using a dropdown
    position_df = df[df["position"] == position]
    # Decide which metric to look at with the dropdown - get the top 10 and put the values in reverse for plotting
    metric_df = position_df.sort_values(metric, ascending = False).head(10)[::-1]
    # Create a horizontal bar chart with the top players
    fig = px.bar(metric_df, x = metric, y = "second_name", orientation = "h")

    return fig


@callback(
    Output("top-players-table", "data"),
    Output("top-players-table", "columns"),
    Input("position-dropdown", "value"),
    Input("metric-dropdown", "value")
)
def create_top_table(position, metric):
    # Set position using dropdonw
    position_df = df[df["position"] == position]
    # Use metric to sort data and get same number of players for tabke
    metric_df = position_df.sort_values(metric, ascending = False).head(10)
    # Keep only relevant columns
    final_df = metric_df.loc[:, ["second_name", "team", "selected_by_percent", "now_cost", "minutes", "total_points", "value"]]

    data = final_df.to_dict('records')
    cols = [{"name": i, "id": i} for i in final_df.columns]

    return data, cols
    


