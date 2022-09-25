import pandas as pd
import plotly.express as px
import os
import plotly.figure_factory as ff

print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
print(np.pi)

app = Dash(__name__)

#HTML layout
app.layout = html.Div(children=[
    # All elements from the top of the page
    
    html.Div([
        html.Div([
            html.H1(children='Covid19 Mobility report and there Impact'),
            html.H2( 'The graph visualization reports movement trends over time by geography, across different categories of places such as retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential'),
            html.H3('1.Retail & Recreation Impact'),
            html.H4(' Visualization of percentage impact on retail and recreation from a baseline level.The beginning of the pandemic, there was a percentage increase which is when people started stocking up food supplies to prepare for lockdowns. Subsequently, there was a significant decrease in retail and recreation business for long periods.'),
             html.Button("Switch Axis", n_clicks=0, 
                id='button'),
                 dcc.Graph(id="graph"),

        ],  className="six columns"),
     ]),
    

    html.Div([
            html.H3('2.Residential Impact'),
            html.H4('Visualization of percentage residential change during the pandemic times. The change is generally positive which suggests that people mostly stayed home during the pandemic.'),
               dcc.Graph(id="bar"),
               ], className="six columns"),
    
    html.Div([
        html.Div([
        html.H3(['Retail and Recreation impact world Map']),
        html.H4('Visualization map plot of retail and recreation impacts on world wide different countries.')
      ]),

    html.Div([
        dcc.Graph(id='map')
    ]),
    ])
], className="row")

#callback for visualization of graph

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
    #fig.update_layout(yaxis_range=[10,50])
  
    return fig

@app.callback(
    Output("bar", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('./dash-255.csv')
    if n_clicks % 2 == 0:
        y, x = 'residential_percent_change_from_baseline', 'sub_region_2'
    else:
        y, x = 'residential_percent_change_from_baseline', 'sub_region_2'
    fig1 = px.bar(df, x=x, y=y)   
    #fig1.update_layout(xaxis_range=[10,1000])
    fig1.update_layout(yaxis_range=[0,10])
 
    return fig1



@app.callback(
     Output("map", "figure"), 
    Input("button", "n_clicks"))

def update_graph(my_dropdown):
     data = pd.read_csv('./map.csv')  
     fig2 = px.choropleth(data, locations='country_region',
                     locationmode="country names", color='retail_and_recreation_percent_change_from_baseline', scope="world") 
     #fig2.show()    
     return fig2

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True,port=8051)


