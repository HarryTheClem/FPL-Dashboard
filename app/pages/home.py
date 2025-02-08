import numpy as np
import pandas as pd
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_csv("./players_data.csv")



dash.register_page(__name__, path = "/")

layout = dbc.Container([
    dbc.Row([
        dbc.Col([dcc.Dropdown(['Goalkeeper', 'Defender', "Midfielder", 'Forward'], 'Goalkeeper', id = 'position-dropdown'),
                 html.Br(),
                 dcc.Dropdown(['total_points', 'value'], 'total_points', id = 'metric-dropdown')], width = 2)
    ])
])



