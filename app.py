import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Covid-19-Impact-Analysis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('./dash-255.csv') # replace with your own data source

    if n_clicks % 2 == 0:
        x, y = 'date', 'retail_and_recreation_percent_change_from_baseline'
    else:
        x, y = 'retail_and_recreation_percent_change_from_baseline', 'date'

    fig = px.line(df, x=x, y=y)   
     


    return fig


app.run_server(debug=True)