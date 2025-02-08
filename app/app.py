import numpy as np
import pandas as pd
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


app = Dash(__name__, use_pages = True, external_stylesheets = [dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        # dbc.NavItem(dbc.NavLink("Data upload", href="/data_upload")),
    ],
    brand="FPL Analysis",
    color="dark",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container([
    dbc.Row([
        navbar,
        dash.page_container
    ])
], fluid = True)



if __name__ == "__main__":
    app.run_server(debug = True)



